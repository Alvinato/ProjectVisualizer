import filehelper as FH
import authormapper as AM
import pylintanalzyer as PA
import json as JS

import re as RE
import os as OS

SAVE_TO = {"plumbum" : "/home/asumal/web2py/applications/jaat/views/plumbum",
           "pattern" : "/home/asumal/web2py/applications/jaat/views/pattern"}

PATH_TO = {"plumbum" : "/home/asumal/git/cs410/plumbum/plumbum/",
           "pattern" : "/home/asumal/git/cs410/pattern/pattern/"}

# http://stackoverflow.com/a/15221068
def multiple_replace(string, *key_values):
    return multiple_replacer(*key_values)(string)

# http://stackoverflow.com/a/15221068
def multiple_replacer(*key_values):
    replace_dict = dict(key_values)
    replacement_function = lambda match: replace_dict[match.group(0)]
    pattern = RE.compile("|".join([RE.escape(k) for k, v in key_values]), RE.M)
    return lambda string: pattern.sub(replacement_function, string)

def get_name(file_name, code_base):
    replacements = (PATH_TO[code_base], ""), ("/", "-"), (".py", ".json")
    name = multiple_replace(file_name, *replacements)
    return name

def save_file(result, path_to_file, code_base):
    name = get_name(path_to_file, code_base)
    path = SAVE_TO[code_base]
    fullpath = OS.path.join(path, name)

    # save fusion to file
    with open(fullpath, 'w') as saving_to_file:
         saving_to_file.write(result)

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
            component["colour"] = "white"
            component["error"] = "none"

        # add line component to 'solution' list
        solution.append(component)

    return solution

if __name__ == "__main__":
    import config

    info = config.create_preferences()

    path_to_code_base = info['arjun']['plumbum']
    path_to_file = path_to_code_base + "/docs/conf.py"
    solution = fuse_file(path_to_code_base, path_to_file,)
    print solution
