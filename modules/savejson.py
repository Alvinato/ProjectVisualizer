import re as RE
import os as OS

SAVE_TO = {"plumbum" : "/home/asumal/web2py/applications/jaat/views/plumbum",
           "pattern" : "/home/asumal/web2py/applications/jaat/views/pattern"}

PATH_TO = {"plumbum" : "/home/asumal/git/cs410/plumbum/plumbum/",
           "pattern" : "/home/asumal/git/cs410/pattern/pattern/"}

def save_file(result, path_to_file, code_base):
    """ """
    name = get_name(path_to_file, code_base)
    path = SAVE_TO[code_base]
    fullpath = OS.path.join(path, name)

    # save fusion to file
    with open(fullpath, 'w') as saving_to_file:
         saving_to_file.write(result)

def get_name(file_name, code_base):
    """ """
    replacements = (PATH_TO[code_base], ""), ("/", "-"), (".py", ".json")
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

if __name__ == "__main__":
    pass
