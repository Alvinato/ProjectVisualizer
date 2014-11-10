#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from gluon import *
import os

class Code_Structure(object):
    """ Contains the file structure of a code base
    """

    def __init__(self, name, root):
        self.name = name
        self.root = root
        #self.path = self.create_path(root)

    def get_path(self):
        return self.path

    def print_file_structure(self):
         """ print out the code structure
             http://stackoverflow.com/questions/9727673/
             list-directory-tree-structure-using-python
         """
         startpath = self.root
         for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    def get_name(self):
        """ Return the name of the
            code structure
        """
        return self.name

    def get_root(self):
        """ Return the path of the
            code structure
        """
        return self.root

    def create_path(self, path):
        """ Given the root directory, this function will return
            The file structure of the code base.
        """
        structure = {}
        root, subdirs, files = next(os.walk(path))
        #print "root: %s\n subirs: %s\n files: %s\n" % (root, subdirs, files)
        structure.update({"name" : root})

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
        return structure

if __name__ == "__main__":
    import json

    structure = Code_Structure("Plumbum", "/home/asumal/git/cs410/plumbum/plumbum")
    print structure.get_name()
    print structure.get_root()

    path = structure.create_path(structure.get_root())
    temp = open("sample_output.json", "w")
    json.dump(path, temp)
    temp.close()
    print path
