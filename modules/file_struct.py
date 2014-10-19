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

    def get_name(self):
        return self.name

    def get_root(self):
        return self.root

    def create_path(self, root):
        """ Given the root directory, this function will return
            The file structure of the code base. It will be a
            dictionary, with directories as the keys and a list
            of string python files
        """
        rootdir = self.get_root()
        print "****Start***"
        for subdir, dirs, files in os.walk(rootdir):
            print subdir
            #print dirs
            for file in files:
                print file
                #print dirs
                #print os.path.join(subdir, file)
        return "path"
