from gitmetrics import get_contributors_for_file
from filehelper import convert_file_to_json
from filehelper import find_python_files_in_project
import os

def create_author_mappings_for_file(filepath, filename):
    """ Get the authors for each line of the filename.
    Convert the file into a JSON object. Augment the JSON
    object by adding an author value to each line number."""

    authors = get_contributors_for_file(filepath, filename)
    file_dict = convert_file_to_json(filename)
    for key in file_dict[filename].keys():
        file_dict[filename][key]['author'] = authors[key]
    return file_dict

if __name__ == '__main__':
    "Testing functions"

    from sys import argv
    from settings import load_project_properties

    try:
        script, user, code_base = argv
    except ValueError:
        print "Incorrect number of arguments"
    else:
        config = load_project_properties()
        #print 'config', config

        file_path = config[user][code_base]
        file_name = file_path + '/setup.py'

        print create_author_mappings_for_file(file_path, file_name)
