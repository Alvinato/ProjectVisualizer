import subprocess
from collections import OrderedDict
import sys
import os


def get_contributors_for_file(filename):
    """Returns an ordered dictionary that represents the author for every single
    line of code in a file. Mapping is line_number:author email"""
    output = subprocess.check_output("git blame  --show-email {} "
                                     "| grep -o -p '<.*>' "
                                     "| cut -d '>' -f1"
                                     "| cut -d '<' -f2".format(filename), shell=True)
    output_array = output.split('\n')
    num_lines = len(output_array)
    line_number = 1
    line_contributors = OrderedDict()
    while line_number != num_lines:
        line_contributors[str(line_number)] = output_array[line_number]
        line_number = line_number + 1
    return line_contributors

def get_contributor_for_line(filename, line_number):
    "Get the email for an author of a specific line of code"
    contributor = subprocess.check_output("git blame -L {},{} --show-email {} "
                                     "| grep -o -p '<.*>' "
                                     "| cut -d '>' -f1"
                                     "| cut -d '<' -f2".format(line_number,line_number, filename), shell=True)
    return contributor

if __name__ == "__main__":
    #contributors = get_contributors_for_file('/Users/jasonpinto/Downloads/web2py/applications/jaat/controllers/appadmin.py')
    get_contributor_for_line('/Users/jasonpinto/Downloads/web2py/applications/jaat/controllers/appadmin.py', 1)