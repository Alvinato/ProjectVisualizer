from collections import OrderedDict

def convert_file_to_json(filename):
    file_lines = {}
    file_lines[filename] = {}
    with open(filename) as file:
        line_num = 1
        for line in file:
            file_lines[filename][str(line_num)] = line
            line_num = line_num + 1
    return file_lines



if __name__ == '__main__':
    convert_file_to_json('/Users/jasonpinto/plumbum/plumbum/version.py')


