from gitmetrics import get_contributors_for_file
from filehelper import convert_file_to_json
from filehelper import find_python_files_in_project
import os

def get_git_analysis(path, files):
    """ """
    solution = []
    for python_file in files:
        git_results = create_author_mappings_for_file(path, python_file)
        solution.append(git_results)
    return solution

def create_author_mappings_for_file(filepath, filename):
    """ Get the authors for each line of the filename.
    Convert the file into a JSON object. Augment the JSON
    object by adding an author value to each line number."""

    authors = get_contributors_for_file(filepath, filename)
    file_dict = convert_file_to_json(filename)
    for key in file_dict[filename].keys():
        file_dict[filename][int(key)]['author'] = authors[int(key)]
    file_dict["size"] = len(file_dict[filename])
    return file_dict

if __name__ == '__main__':
    "Testing functions"

    from sys import argv
    from config import load_project_properties
    from filehelper import find_python_files_in_project

    try:
        script, user, code_base = argv
    except ValueError:
        print "Incorrect number of arguments"
    else:
        config = load_project_properties()
        #print 'config', config

        file_path = config[user][code_base]
        file_name = file_path + '/plumbum/cli'
        files = find_python_files_in_project(file_name)
        #print files
        git_results = create_author_mappings_for_file(file_path, file_name + "/application.py")
        print git_results
        #print get_git_analysis(file_path, files)
