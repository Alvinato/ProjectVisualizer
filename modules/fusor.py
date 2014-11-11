#!/usr/bin/env python

import filehelper as FH
import authormapper as AM
import pylintanalzyer as PA
import json as JS

def fuse(path_to_code_base):
    # retrieves a list of all .py files inside the specified code_base
    files = FH.find_python_files_in_project(path_to_code_base)

    # iterate through list of .py files
    for file in files:

        # initialize 'solution' dictionary and 'lines' list
        solution, lines = {}, []
        solution["path"] = file

        # GIT ANALYSIS
        git_results = AM.create_author_mappings_for_file(path_to_code_base, file)

        # PYLINT ANALYSIS
        pylint_results = PA.pylint_analyzer(file)

        # FUSION
        max_lines = git_results["size"] + 1
        fusion = combine_results(git_results[file], pylint_results[file], max_lines)

        # add result to 'lines' list
        lines.append(fusion)

        # add 'lines' list to 'solution' dictionary
        solution["lines"] = lines

        # convert 'solution' dictionary into JSON object
        solution = JS.dumps(solution)

        #change name of file
        file_to_save = file.replace(".py", ".json")

        # save fusion to file
        with open(file_to_save, 'w') as saving_to_file:
            saving_to_file.write(solution)

    return solution

def fuse_file(path_to_file):
    

def combine_results(git_results, pylint_results, max_lines):

    # setup list to hold solution
    solution = []

    # for each line in the python code
    for line_number in range(1, max_lines):

        # setup dictionary to hold specific line information
        component = {}

        # add GIT METRICS
        component["line"] = str(line_number)
        component["author"] = git_results[line_number]["author"]

        if (line_number in pylint_results):
            # There is an pylint error on this line
            component["colour"] = pylint_results[line_number]["color"]
            component["error"] = pylint_results[line_number]["category"]
        else:
            # There is no pylint error on this line
            component["colour"] = "black"
            component["error"] = "none"

        # add line component to 'solution' list
        solution.append(component)

    return solution

if __name__ == "__main__":
    import config

    info = config.create_preferences()
    path = info['arjun']['plumbum']

    solution = fuse(path)
    #print solution
