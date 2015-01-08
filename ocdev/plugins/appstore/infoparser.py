from xml.etree import ElementTree

from ocdev.plugins.appstore.invalidconfigerror import InvalidConfigError


class InfoParser:

    def __init__(self):
        self.categories = {
            'multimedia': 920,
            'pim': 921,
            'productivity': 922,
            'game': 923,
            'tool': 924,
            'other': 925
        }
        self.licences = {
            'AGPL': 16,
            'BSD': 6
        }

    def parse(self, info_xml):
        root = ElementTree.fromstring(info_xml)

        result = {
            'name': root.findtext('./name', '').strip(),
            'category': root.findtext('./category', '').strip(),
            'description': root.findtext('./description', '').strip(),
            'author': root.findtext('./author', '').strip(),
            'licence': root.findtext('./licence', 'BSD').strip(),
            'homepage': root.findtext('./website', '').strip(),
            'repository': root.findtext('./repository', '').strip(),
            'bugs': root.findtext('./bugs', '').strip(),
            'ocsid': root.findtext('./ocsid', '').strip(),
            'version': root.findtext('./version', '').strip(),
            'requiremax': root.findtext('./requiremax', '').strip(),
            'requiremin': root.findtext('./require', '').strip(),
        }

        # handle different owncloud requirements
        requiremin = root.findtext('./requiremin', '').strip()
        owncloud = root.findall('./dependencies/owncloud')

        if len(requiremin) > 0:
            result['requiremin'] = requiremin

        if len(owncloud) == 1:
            requiremin = owncloud[0].get('min-version', '').strip()
            requiremax = owncloud[0].get('max-version', '').strip()
            if len(requiremin) > 0:
                result['requiremin'] = requiremin
            if len(requiremax) > 0:
                result['requiremax'] = requiremax

        # required attributes
        self._require_not_empty(result['requiremin'], 'owncloud', 'min-version')
        self._require_not_empty(result['name'], 'name')
        self._require_not_empty(result['category'], 'category')
        self._require_not_empty(result['description'], 'description')
        self._require_not_empty(result['author'], 'author')
        self._require_not_empty(result['licence'], 'licence')
        self._require_not_empty(result['version'], 'version')

        # map ids
        try:
            result['category'] = self.categories[result['category']]
        except KeyError:
            raise InvalidConfigError('Unknown category type %s' % result['category'])

        try:
            result['licence'] = self.licences[result['licence']]
        except KeyError:
            raise InvalidConfigError('Unknown licence type %s' % result['licence'])


        return result


    def _require_not_empty(self, value, name, tag=None):
        if value.strip() == '':
            if tag:
                msg = 'Error: tag %s of field %s not found or empty' % (tag, name)
            else:
                msg = 'Error: field %s not found or empty' % name
            raise InvalidConfigError(msg)
