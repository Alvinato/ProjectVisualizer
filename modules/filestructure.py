#!/usr/bin/env python
import os
import json

def create_path(path):
    """ Given the root directory, this function will return
        The file structure of the code base.
    """
    structure = {}
    root, subdirs, files = next(os.walk(path))
    #print "root: %s\n subirs: %s\n files: %s\n" % (root, subdirs, files)
    structure.update({"name" : root})
    # http://stackoverflow.com/a/18435
    files = [file for file in files if (not file.endswith(".json"))]
    if (subdirs or files):
        children = []
        if (subdirs):
            for subdir in subdirs:
                new_path = "%s/%s" % (path, subdir)
                children.append(self.create_path(new_path))

        if (files):
            for file in files:
                temp_file_dict = {}
                temp_file_dict["name"] = file
                temp_file_dict["path"] = "%s/%s" % (path, file)
                temp_file_dict["size"] = ""
                temp_file_dict["colour"] = ""
                children.append(temp_file_dict)
        structure.update({"children" : children})
    return json.dumps(structure)

if __name__ == '__main__':
    print create_path("/home/asumal/git/cs410/plumbum/plumbum/cli")
