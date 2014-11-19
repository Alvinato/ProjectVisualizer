import filehelper as FH
import savejson as SJ

import authormapper as AM
import pylintanalzyer as PY

import fusor as FR
import filestructure as FS

import json

def plumbum():
    """ """
    plumbum = "plumbum"
    path_to_plumbum = "/home/asumal/git/cs410/plumbum/plumbum"
    solution = get_visualization(plumbum, path_to_plumbum)

    return dict(plumbum = solution)

def pattern():
    """ """
    pattern = "pattern"
    path_to_pattern = "/home/asumal/git/cs410/pattern/pattern"
    solution = get_visualization(pattern, path_to_pattern)

    return dict(pattern = solution)

def get_visualization(name_of_code_base, path_to_code_base):
    """ """
    print "***begin %s analysis***" % (name_of_code_base)

    list_of_python_files = FH.find_python_files_in_project(path_to_code_base)
    pylint_analysis = PY.get_pylint_analysis(list_of_python_files)
    git_analysis = AM.get_git_analysis(path_to_code_base, list_of_python_files)

    for python_file in list_of_python_files:
        result = FR.fuse_file(path_to_code_base, python_file, pylint_analysis[python_file], git_analysis[python_file])
        SJ.save_file(result, python_file, name_of_code_base)

    solution = FS.create_structure(path_to_code_base, name_of_code_base, pylint_analysis, git_analysis, name_of_code_base)

    solution_as_json = json.dumps(solution)
    return solution_as_json
