import filehelper as FH
import authormapper as AM
import pylintanalzyer as PA
import json as JS

import re as RE
import os as OS

def fuse_file(path_to_code_base, path_to_file, pylint_results, git_results):
    # initialize 'solution' dictionary and 'lines' list
    solution, lines = {}, []
    solution["path"] = path_to_file

    # FUSION
    max_lines = git_results["size"] + 1
    fusion = combine_results(git_results, pylint_results, max_lines)

    # add result to 'lines' list
    lines.append(fusion)

    # add 'lines' list to 'solution' dictionary
    solution["lines"] = lines

    # convert 'solution' dictionary into JSON object
    solution = JS.dumps(solution)

    return solution

def combine_results(git_results, pylint_results, max_lines):

    # setup list to hold solution
    solution = []

    # for each line in the python code
    for line_number in range(1, max_lines):

        # setup dictionary to hold specific line information
        component = {}

        # add GIT METRICS
        component["index"] = str(line_number)
        component["author"] = git_results[line_number]["author"]
        component["code"] = git_results[line_number]["code"]

        if (line_number in pylint_results):
            # There is an pylint error on this line
            component["colour"] = pylint_results[line_number]["colour"]
            component["error"] = pylint_results[line_number]["category"]
        else:
            # There is no pylint error on this line
            component["colour"] = "orange"
            component["error"] = "none"

        # add line component to 'solution' list
        solution.append(component)

    return solution

if __name__ == "__main__":
    pass
