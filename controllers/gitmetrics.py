import subprocess
from collections import OrderedDict
import git
import sys
import os


def get_contributors_for_file(file_path, filename):
    """Returns an ordered dictionary that represents the author for every single
    line of code in a file. Mapping is line_number:author email"""
    output = subprocess.check_output("git blame  --show-email {} "
                                     "| grep -o -p '<.*>' "
                                     "| cut -d '>' -f1"
                                     "| cut -d '<' -f2".format(filename),
                                     shell=True,
                                     cwd=r'{}'.format(file_path))
    output_array = output.split('\n')
    num_lines = len(output_array)
    line_number = 1
    line_contributors = OrderedDict()
    while line_number != num_lines:
        line_contributors[str(line_number)] = output_array[line_number]
        line_number = line_number + 1
    return line_contributors

def get_contributor_for_line(file_path, filename, line_number):
    "Get the email for an author of a specific line of code"
    contributor = subprocess.check_output("git blame -L {},{} --show-email {} "
                                     "| grep -o -p '<.*>' "
                                     "| cut -d '>' -f1"
                                     "| cut -d '<' -f2".format(line_number,line_number, filename),
                                     shell=True,
                                     cwd=r'{}'.format(file_path))
    return contributor

if __name__ == "__main__":
    "NOTE: Just use for testing purposes"
    print get_contributor_for_line('/Users/jasonpinto/plumbum/plumbum', '/Users/jasonpinto/plumbum/plumbum/version.py', 1)