from os import getcwd
from os.path import join, basename
from ocdev.plugins.plugin import Plugin
from tarfile import open as tar_open
from xml.etree import ElementTree

import requests

from ocdev.plugins.appstore.infoparser import InfoParser


class Arguments:

    def __construct__(self, archivedir, action='release'):
        self.action = action
        self.archivedir = archivedir


class AppStore(Plugin):

    def __init__(self):
        super().__init__('appstore')


    def add_sub_parser(self, main_parser):
        default_path = getcwd()
        default_app_name = basename(default_path)
        parser = main_parser.add_parser('appstore', help='Lets you release and \
                                        update apps on the appstore. Settings \
                                        are read from ~/.ocdevrc')
        parser.set_defaults(which='appstore')

        parser.add_argument('action', choices=['release'])
        parser.add_argument('archive', help='Full path to the release \
                            arcchive.')


    def run(self, arguments, directory, settings):
        url = settings.get_value('appstore', 'url').rstrip('/')
        user = settings.get_value('appstore', 'user')
        password = settings.get_value('appstore', 'password')
        archive_dir = arguments.archive
        app_name = basename(archive_dir).split('.')[0]

        # parse the appinfo/info.xml from the archive to fill in stuff required
        # for the release
        archive = tar_open(archive_dir)

        # TODO: we need app validation like:
        # * name of the folder is the same as the id in info.xml
        # * no private api usage
        # * all needed fields for info.xml present
        # * size not bigger than allowed to upload
        info_xml = archive.extractfile(
            dict(zip(
                archive.getnames(),
                archive.getmembers()
            ))['%s/appinfo/info.xml' % app_name]
        )

        parser = InfoParser()
        result = parser.parse(info_xml.read())

        # no ocsid present means not yet in the appstore so let's upload it
        params = {
            'name': result['name'],
            'type': result['category'],
            'depend': result['requiremin'],
            'downloadtype1': 0,
            'licensetype': result['licence'],
            'version': result['version']
        }

        if result['homepage'] != '':
            params['homepage'] = result['homepage']
            params['homepagetype'] = 'Homepage'
        if result['repository'] != '':
            params['homepage2'] = result['repository']
            params['homepagetype2'] = 'Version Control'
        if result['bugs'] != '':
            params['homepage3'] = result['bugs']
            params['homepagetype3'] = 'Issue Tracker'
        if result['requiremax'] != '':
            params['depend2'] = result['requiremax']

        if result['ocsid'] == '':
            create_url = '%s/content/add ' % url
            response = requests.post(create_url, params=params, auth=(user, password))
            code = self.get_status_code(response)

            if code == '102':
                raise Exception('Not authorized! Check your credentials.')

            # get ocsid
            tree = ElementTree.fromstring(response.text)
            ocsid = tree.findtext('.//data/content/id')

            print('Please add <ocsid>%s</ocsid> to your appinfo/info.xml to ' +
                  'be able to update the uploaded app' % ocsid)
        else:
            update_url = '%s/content/edit/%s' % (url, result['ocsid'])
            response = requests.post(update_url, params=params, auth=(user, password))
            code = self.get_status_code(response)

            if code == '102':
                raise Exception('Not authorized! Check your credentials.')

        upload_file_url = '%s/content/uploaddownload/%s' % (url, result['ocsid'])
        file = {'localfile': open(archive_dir, 'rb')}
        response = requests.post(files=file)
        code = self.get_status_code(response)

        if code == '101':
            raise Exception('Could not upload file. Is the archive bigger ' +
                            'than 10Mb?')
        elif code == '103':
            raise Exception('Not authorized! Check your credentials.')


    def get_status_code(self, response):
        tree = ElementTree.fromstring(response.text)
        return tree.findtext('.//meta/statuscode')
