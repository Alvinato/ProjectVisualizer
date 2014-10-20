from gitmetrics import get_contributors_for_file
from filehelper import convert_file_to_json
from filehelper import find_python_files_in_project
import os


def create_author_mappings_for_file(filepath, filename):
    authors = get_contributors_for_file(filepath, filename)
    file_dict = convert_file_to_json(filename)
    for key in file_dict[filename].keys():
        file_dict[filename][key]['author'] = authors[key]
    return file_dict



if __name__ == '__main__':
    files = find_python_files_in_project('/Users/jasonpinto/pattern')
    for file in files:
        if file != '':
            file_path = os.path.dirname(file)
            print create_author_mappings_for_file(file_path, file)
            print '/n'
