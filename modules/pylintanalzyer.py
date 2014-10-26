import subprocess

WARNING = 'No config file found, using default configuration'
IGNORE_LINE = '*'

def get_pylint_analysis(code_base):
    """ """
    solution = {}
    for python_file in code_base:
        solution.update(pylint_analyzer(python_file))
    return solution

def pylint_analyzer(path_to_file):
    """ """
    #print 'COMPUTING: ', path_to_file
    message = ['pylint', '-rn', '--msg-template="{line}:{C}"', path_to_file]
    command = subprocess.Popen(message, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = command.communicate()

    stderr_as_list = stderr.splitlines()
    if (len(stderr_as_list) == 1 and stderr_as_list[0] == WARNING):
        solution = parse_pylint_output(stdout.splitlines())
        #print "RETURNING: ", solution
        return {path_to_file : solution}
    else:
        raise Exception(stderr)

def parse_pylint_output(pylint_output):
    """ """
    solution = {}
    if (pylint_output[0].startswith(IGNORE_LINE)):
        pylint_output = pylint_output[1:]

    for pylint_line in pylint_output:
        line_number, category = parse_pylint_line(pylint_line)
        solution[line_number] = {'category':category}
    return solution

def parse_pylint_line(pylint_line):
    """ """
    try:
        line_number, category = pylint_line.split(":")
    except ValueError:
        print "ERROR: ", pylint_line
        raise ValueError()
    else:
        return line_number, category

if __name__ == '__main__':
    "Testing functions"

    from sys import argv
    from settings import load_project_properties
    from filehelper import find_python_files_in_project

    try:
        script, user, code_base = argv
    except ValueError:
        print "Incorrect number of arguments"
    else:
        config = load_project_properties()

        file_path = config[user][code_base]
        files = find_python_files_in_project(file_path)
        solution = get_pylint_analysis(files)
