from os.path import dirname, realpath, join

def get_version():
    current_dir = dirname(realpath(__file__))
    version_file = join(current_dir, 'version.txt')

    with open(version_file, 'r') as infile:
        # remove spaces, tabs and new lines
        return ''.join(infile.read().split())

