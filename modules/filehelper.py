from collections import OrderedDict
import subprocess

def convert_file_to_json(filename):
    """ For each file_name, associate code with line number.
    filelines = {'filename' : {'1' : {'code' : 'start of file'},
                               ...
                               'n' : {'code' : 'end of file}
                              }
                }"""

    file_lines = {}
    file_lines[filename] = {}
    with open(filename) as file:
        line_num = 1
        for line in file:
            file_lines[filename][line_num] = {'code':line}
            line_num = line_num + 1
    return file_lines

def find_python_files_in_project(filepath):
    """ Given a code base, find all the python files. Return as a list """

    output = subprocess.check_output("find {} -name '*.py'".format(filepath),shell=True, cwd=r'{}'.format(filepath))
    output_array = output.splitlines()
	
	#filtering out __init__.py files as they are not in our scope
    filtered = [i for i in output_array if '__init__' not in i]
    return filtered

if __name__ == '__main__':
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
        file_name = file_path + '/setup.py'
        print "List of Python Files\n", find_python_files_in_project(file_path)
        print "Code by Line number for 1 file\n", convert_file_to_json(file_name)
