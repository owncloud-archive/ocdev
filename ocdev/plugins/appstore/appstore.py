from os import getcwd
from os.path import join, basename
from ocdev.plugins.plugin import Plugin
from tarfile import open as tar_open
from xml.etree import ElementTree

import requests

from ocdev.plugins.errors import DependencyError


class Arguments:

    def __construct__(self, archivedir, action='update'):
        self.action = action
        self.archivedir = archivedir


class AppStore(Plugin):

    def __init__(self):
        super().__init__('appstore')
        self.categories = {
            'multimedia': 920,
            'pim': 921,
            'productivity': 922,
            'game': 923,
            'tool': 924,
            'other': 925
        }
        self.licenses = {
            'AGPL': 16
        }


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

        tree = ElementTree.parse(info_xml)
        root = tree.getroot()

        name = root.findtext('./name', '').strip()
        category = root.findtext('./category', '').strip()
        requiremin = root.findtext('./requiremin | ./require', '').strip()
        requiremax = root.findtext('./requiremax', '').strip()
        description = root.findtext('./description', '').strip()
        author = root.findtext('./author', '').strip()
        license = root.findtext('./licence', '').strip()
        homepage = root.findtext('./website', '').strip()
        repository = root.findtext('./repository', '').strip()
        bugs = root.findtext('./bugs', '').strip()
        ocsid = root.findtext('./ocsid', '').strip()
        version = root.findtext('./version', '').strip()

        # required attributes
        self.require_not_empty(name, 'name')
        self.require_not_empty(category, 'category')
        self.require_not_empty(description, 'description')
        self.require_not_empty(author, 'author')
        self.require_not_empty(license, 'licence')
        self.require_not_empty(version, 'version')

        # no ocsid present means not yet in the appstore so let's upload it
        params = {
            'name': name,
            'type': self.categories[category],
            'depend': requiremin,
            'downloadtype1': 0,
            'licensetype': self.licenses.get(license, 6),  # default to BSD
            'version': version
        }

        if homepage != '':
            params['homepage'] = homepage
            params['homepagetype'] = 'Homepage'
        if repository != '':
            params['homepage2'] = repository
            params['homepagetype2'] = 'Version Control'
        if bugs != '':
            params['homepage3'] = bugs
            params['homepagetype3'] = 'Issue Tracker'
        if requiremax != '':
            pass

        from pprint import pprint
        pprint(params)

        if ocsid == '':
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
            update_url = '%s/content/edit/%s' % (url, ocsid)
            response = requests.post(update_url, params=params, auth=(user, password))
            code = self.get_status_code(response)

            if code == '102':
                raise Exception('Not authorized! Check your credentials.')

        upload_file_url = '%s/content/uploaddownload/%s' % (url, ocsid)
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


    def require_not_empty(self, value, name):
        if value.strip() == '':
            raise DependencyError('Error: field %s not found or empty' % name)
