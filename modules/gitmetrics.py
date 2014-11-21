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
	
	# need to iterate in order, and since this analyzer
	# is garunteed to have ALL lines of code, we use orderedDict()
    line_contributors = OrderedDict()
    while line_number != num_lines:
        line_contributors[line_number] = output_array[line_number - 1]
        line_number = line_number + 1
    return line_contributors

def get_contributor_for_line(file_path, filename, line_number):
    "Get the email for an author of a specific line of code"

	# heart of custom git script. subprocess call
    contributor = subprocess.check_output(LINE_COMMAND.format(line_number, line_number, filename),
                                          shell=True, cwd=r'{}'.format(file_path))
    return contributor



if __name__ == "__main__":
    "Testing functions"

    from sys import argv
    from config import load_project_properties

    try:
        script, user, code_base = argv
    except ValueError:
        print "Incorrect number of arguments"
    else:
        config = load_project_properties()
        #print 'config', config

        file_path = config[user][code_base]
        #print file_path
        file_name = file_path + '/setup.py'

        #print "File\n", get_contributors_for_file(file_path, file_name)
        #print "Line\n", get_contributor_for_line(file_path, file_name, '1')

        import os
        name = os.path.abspath("fusor.py")
        parent = os.path.abspath(os.path.join(name, os.pardir))
        print name, parent
        print "File\n", get_contributors_for_file(parent, name)
        #print "Line\n", get_contributor_for_line(file_path, file_name, '1')
