#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gluon import *
import os

class Code_Structure(object):
    """ Contains the file structure of a code base
    """

    def __init__(self, name, root):
        self.name = name
        self.root = root
        self.path = self.create_path(root)

    def print_file_structure(self, startpath):
         """ http://stackoverflow.com/questions/
             9727673/list-directory-tree-structure-using-python
         """
         for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    def get_name(self):
        return self.name

    def get_root(self):
        return self.root

    def create_path(self, path):
        """ Given the root directory, this function will return
            The file structure of the code base.
        """
        structure = {}
        root, subdirs, files = next(os.walk(path))
        for file in files:
            structure.update({file : None})
        for subdir in subdirs:
            new_path = "%s\%s" % (path, subdir)
            structure.update({subdir : self.create_path_04(new_path)})
        return structure
