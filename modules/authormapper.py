from gitmetrics import get_contributors_for_file
from filehelper import convert_file_to_json
from filehelper import find_python_files_in_project
import os

def get_git_analysis(path, files):
    """ wrapper function that takes full code base and creates
		structure that gets size of file and author name"""
    solution = {}
    for python_file in files:
        git_results = create_author_mappings_for_file(path, python_file)
        solution.update(git_results)
    return solution

def create_author_mappings_for_file(filepath, filename):
    """ Get the authors for each line of the filename.
    Convert the file into a JSON object. Augment the JSON
    object by adding an author value to each line number."""

    authors = get_contributors_for_file(filepath, filename)
    file_dict = convert_file_to_json(filename)
    for key in file_dict[filename].keys():
        file_dict[filename][int(key)]['author'] = authors[int(key)]
    file_dict[filename]["size"] = len(file_dict[filename])
    return file_dict

if __name__ == '__main__':
    pass