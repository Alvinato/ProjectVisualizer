from collections import OrderedDict
import subprocess

def convert_file_to_json(filename):
    file_lines = {}
    file_lines[filename] = {}
    with open(filename) as file:
        line_num = 1
        for line in file:
            file_lines[filename][str(line_num)] = {'code':line}
            line_num = line_num + 1
    return file_lines

def find_python_files_in_project(filepath):
    output = subprocess.check_output("find {} -name '*.py'".format(filepath),shell=True, cwd=r'{}'.format(filepath))
    output_array = output.split('\n')
    return output_array


if __name__ == '__main__':
    print find_python_files_in_project('/Users/jasonpinto/plumbum/')


