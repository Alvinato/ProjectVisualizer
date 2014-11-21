import re as RE
import os as OS

import json

def save_file(result, path_to_file, path, code_base):
    """ """
	# get path that leads to current directory
    directory = OS.getcwd()
    pattern_json = "%s/views/default/%s" % (directory, code_base)
    
    name = get_name(path_to_file, path, code_base)

	# name of .json file, will be used by front end to render code
    fullpath = OS.path.join(pattern_json, name)

    # save fusion to file
    with open(fullpath, 'w') as saving_to_file:
         saving_to_file.write(result)

def get_name(file_name, path, code_base):
    """ """
	# make multiple modifications to string, all in one pass!
    replacements = (path + "/", ""), ("/", "-"), (".py", ".json")
    name = multiple_replace(file_name, *replacements)

    return name

# http://stackoverflow.com/a/15221068
def multiple_replace(string, *key_values):
    return multiple_replacer(*key_values)(string)

# http://stackoverflow.com/a/15221068
def multiple_replacer(*key_values):
    replace_dict = dict(key_values)
    replacement_function = lambda match: replace_dict[match.group(0)]
    pattern = RE.compile("|".join([RE.escape(k) for k, v in key_values]), RE.M)
    return lambda string: pattern.sub(replacement_function, string)

def save_code_structure(file_path, code_base_structure):
    with open(file_path, 'w') as file_:
		# simply saves output as json file for front end to use
        solution = json.dumps(code_base_structure)
        file_.write(solution)

if __name__ == "__main__":
    pass
