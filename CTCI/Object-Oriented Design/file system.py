class Directory(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.files = {}
        self.subdirectories = {}

    def addDirectory(self, directory):
        if directory.parent:
            del directory.parent.subdirectories[directory.name]
        directory.parent = self
        self.subdirectories[directory.name] = directory

    def addFile(self, file):
        self.files[file.name] = file

    def get(self, path):
        parts = path.split("/")
        directory = self
        for part in parts:
            if part == '..':
                directory = directory.parent
                if not directory:
                    return None
            elif part in directory.subdirectories:
                directory = directory.subdirectories[part]
            elif part in directory.files:
                return directory.files[part]
            else:
                return None
        return directory


class File(object):
    def __init__(self, name, content):
        self.name = name
        self.content = content


class NoneHash(dict):
    def __missing__(self, key):
        return None