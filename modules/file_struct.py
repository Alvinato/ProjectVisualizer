#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *

class File_Struct:
    "Contains the file structure of a code base"

    def __init__(self, name, root, path):
        self.name = name
        self.root = root
        self.path = getPath(root)

    def get_name():
        return self.name

    def get_root():
        return self.root

    def get_path(root):
        """ Given the root directory, this function will return
            The file structure of the code base. It will be a
            dictionary, with directories as the keys and a list
            of string python files
        """
        pass
