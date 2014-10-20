#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gluon import *
import subprocess

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
        """ brief - Runs pylint on the specified file
            param path_to_root - the file to run pylint on
            return - the errors associated with the specified file
        """
        message = ['pylint', '-rn', '--msg-template="{line}:{C}:{msg}"', root]
        print "root", root

        p1 = subprocess.Popen(message, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_value, stderr_value = p1.communicate()

        list_of_errors = stderr_value.splitlines()

        if (len(list_of_errors) == 1):
            list_of_arguments = stdout_value.splitlines()
            analyzer_results = self.parse_pylint_results(list_of_arguments)
        else:
            print list_of_errors
        return analyzer_results

    def parse_pylint_results(self, results):
        pylint_results = {}
        for item in results:
            if item.startswith('*************'):
                name = self.get_file_name(item)
                pylint_results.update({name: {}})
            else:
                try:
                    line_number, error_type, message = self.get_error_and_message_per_line(item)
                except IndexError:
                    pass
                else:
                    pylint_results[name].update({line_number : {"category" : error_type, "desc" : message}})
        return pylint_results

    def get_file_name(self, item):
        split_by_space = item.split(" ")
        file_name = split_by_space[-1]
        return file_name.replace(".", "/")

    def get_error_and_message_per_line(self, line):
        split_by_colon = line.split(":")
        try:
            return split_by_colon[0], split_by_colon[1], split_by_colon[2]
        except IndexError:
            raise
