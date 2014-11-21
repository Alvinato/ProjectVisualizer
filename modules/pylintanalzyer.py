import subprocess

WARNING = 'No config file found, using default configuration'
IGNORE_LINE = '*'
COLOR = {'E':'red', 'R':'blue', 'W':'green', 'N':'white'}

def get_pylint_analysis(code_base):
    """ Given a list of code bases, iterate through 
		each one and use pylint to analyze them
	"""
    solution = {}
    for python_file in code_base:
        solution.update(pylint_analyzer(python_file))
    return solution

def pylint_analyzer(path_to_file):
    """ Given a path to a python module, run pylint analysis and
		save results in a dictionary
	"""
    print 'COMPUTING: ', path_to_file
 
    message = ['pylint', '-rn', '--msg-template="{line}:{C}"', path_to_file]
	
	# using sub process to do pylint. The provided module doesn't seem to work well for our use case
    command = subprocess.Popen(message, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = command.communicate()

    stderr_as_list = stderr.splitlines()
	
	# ignoring usual warning of no config file.
    if (len(stderr_as_list) == 1 and stderr_as_list[0] == WARNING):
        solution = parse_pylint_output(stdout.splitlines())
        return {path_to_file : solution}
    else:
        raise Exception(stderr)

def parse_pylint_output(pylint_output):
    """ Given an analysis, we now parse through the
		results and only take the values we use 
		in our visualization
	"""
    solution = {}
    bubble_colour = {'E': 0, 'R': 0, 'W': 0}

	# the first line is the name of the python module
	# we don't need it
    if (pylint_output[0].startswith(IGNORE_LINE)):
        pylint_output = pylint_output[1:]

    for pylint_line in pylint_output:
        line_number, category = parse_pylint_line(pylint_line)
		
		# we decided to factor our Conventions and Failure categories.
		# more info: https://piazza.com/class/hwbl1suhmd5c4?cid=233
        if (category == 'C' or category == 'F'):
            pass
        else:
            bubble_colour[category] += 1
            solution[line_number] = {'category':category, 'colour':COLOR[category]}
	# printing so show that back-end is making progress
    print bubble_colour
	
	# find the colour with the max number of errors. Becomes the colour of the module
    max_category = max(bubble_colour.iterkeys(), key=(lambda key: bubble_colour[key]))
    if (bubble_colour[max_category] == 0):
       solution["category"] = 'N'
    else:
        solution["category"] = max_category
    solution["colour"] = COLOR[solution["category"]]

    return solution

def parse_pylint_line(pylint_line):
    """ Where the actual parsing of the pylint results occur"""
    try:
        line_number, category = pylint_line.split(":")
    except ValueError:
		# legacy code. Needed when our requirements were in flux
        print "ERROR in parse_pylint_line: ", pylint_line
        raise ValueError()
    else:
        return int(line_number), category

if __name__ == '__main__':
    pass
