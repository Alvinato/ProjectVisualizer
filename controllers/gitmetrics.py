import subprocess
from collections import OrderedDict

FILE_COMMAND = "git blame --show-email {} | grep '<.*>' | cut -d '>' -f1 | cut -d '<' -f2"
LINE_COMMAND = "git blame -L {},{} --show-email {} | grep '<.*>' | cut -d '>' -f1 | cut -d '<' -f2"

def get_contributors_for_file(file_path, filename):
    """Returns an ordered dictionary that represents the author for every single
    line of code in a file. Mapping is line_number:author email"""
    output = subprocess.check_output(FILE_COMMAND.format(filename), shell=True,
                                     cwd=r'{}'.format(file_path))
    output_array = output.split('\n')
    num_lines = len(output_array)
    line_number = 1
    line_contributors = OrderedDict()
    while line_number != num_lines:
        line_contributors[str(line_number)] = output_array[line_number - 1]
        line_number = line_number + 1
    return line_contributors

def get_contributor_for_line(file_path, filename, line_number):
    "Get the email for an author of a specific line of code"
    contributor = subprocess.check_output(LINE_COMMAND.format(line_number, line_number, filename),
                                          shell=True, cwd=r'{}'.format(file_path))
    return contributor

if __name__ == "__main__":
    "Testing functions"

    jason = {'file_path' : '/Users/jasonpinto/plumbum/plumbum',
             'file_name' : '/Users/jasonpinto/plumbum/plumbum/build.py',
             'line_number' : '1'}

    arjun = {'file_path' : '/home/asumal/git/cs410/plumbum',
             'file_name' : '/home/asumal/git/cs410/plumbum/build.py',
             'line_number' : '1'}

    print "File\n", get_contributors_for_file(arjun['file_path'], arjun['file_name'])
    #print "File\n", get_contributors_for_file(jason['file_path'], jason['file_name'])

    print "Line\n", get_contributor_for_line(arjun['file_path'], arjun['file_name'], arjun['line_number'])
    #print "Line\n", get_contributor_for_file(jason['file_path'], jason['file_name'], jason['line_number'])
