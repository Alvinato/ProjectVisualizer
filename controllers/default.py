import filehelper as FH

import authormapper as AM
import pylintanalzyer as PY

import fusor as FR
import filestructure as FS

PLUMBUM = "plumbum"
PATTERN = "pattern"

def final():
    path_to_plumbum = "/home/asumal/git/cs410/plumbum/plumbum"
    path_to_pattern = "/home/asumal/git/cs410/pattern/pattern"

    list_of_files = FH.find_python_files_in_project(path_to_pattern)
    pylint_analysis = PY.get_pylint_analysis(list_of_files)
    git_analysis = AM.get_git_analysis(path_to_pattern, list_of_files)

    for python_file in list_of_files:
        result = FR.fuse_file(path_to_pattern, python_file, pylint_analysis[python_file], git_analysis[python_file])
        FR.save_file(result, python_file, PATTERN)

    solution = FS.create_structure(path_to_plumbum, PATTERN, pylint_analysis, git_analysis, PATTERN)

    return dict(solution = solution)
