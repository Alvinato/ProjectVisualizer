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
        self.path = self.create_path_04(root)
        print self.path

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

    def create_path_04(self, path):
        structure = {}
        root, subdirs, files = next(os.walk(path))
        for file in files:
            structure.update({file : None})
        for subdir in subdirs:
            new_path = "%s\%s" % (path, subdir)
            structure.update({subdir : self.create_path_04(new_path)})
        return structure

    def create_path_03(self, path):
        structure = {}
        root, subdirs, files = next(os.walk(path))
        print "PATH", path
        print "SUBDIR", subdirs
        print "FILES", files
        print ""

        for subdir in subdirs:
            new_path = "%s\%s" % (path, subdir)
            structure.update({subdir : self.create_path_03(new_path)})
        file_structure = {}
        for file in files:
            file_structure.update({file : None})
        structure.update({path : file_structure})
        return structure

    def create_path_02(self, root):
        print "****START****"
        code_structure = {}
        for path, subdirs, files in os.walk(root):
            print "PATH", path
            print "SUBDIR", subdirs
            print "FILES", files
            print ""

    def create_path(self, root):
        """ Given the root directory, this function will return
            The file structure of the code base. It will be a
            dictionary, with directories as the keys and a list
            of string python files
        """
        print "****inside %s***" % (root)
        roots = {}
        for subdir, dirs, files in os.walk(root):
            print dirs
            if (dirs):
                for dirz in dirs:
                    new_root =  "%s\%s" % (root, dirz)
                    roots.update({dirz:self.create_path(new_root)})
            #print subdir
            #print dirs
            file_dict = {}
            for file in files:
                file_dict.update({file:None})
                #print file
                #print dirs
                #print os.path.join(subdir, file)
            roots.update({subdir:file_dict})
        return roots
