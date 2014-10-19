#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *

class Pylint_Analyzer(object):
    """ Functions related to pylint analyzer
    """

    def __init__(self, name, root):
        self.name = name
        self.root = root
        self.analysis = self.begin_analysis(self.root)

    def get_name(self):
        """ Return the name of this object
        """
        return self.name

    def get_root(self):
        """ Return the file path to the code base
        """
        return self.root

    def get_analysis(self):
        """ Return the analysis related to this object
        """
        return self.analysis

    def begin_analysis(self, root):
        """ Obtain the pylint analysis of code base
        """
        pass
