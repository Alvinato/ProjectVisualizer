import modules.filehelper as FH
import modules.savejson as SJ

import modules.authormapper as AM
import modules.pylintanalzyer as PY

import modules.fusor as FR
import modules.filestructure as FS

import json
import os
import webbrowser

def code_base(name, path):
    """ Enter a code base and path. If the results are cached,
		open visualizer. If not, then call back-end
	"""
    if (not validate_parameters(name, path)):
        return "Exiting Analysis"

    directory = os.getcwd()
    pattern_json = "%s/views/default/%s/%s.json" % (directory, name, name)
    
	# check if output file exists. Saves time if it does exist
    if (not os.path.exists(pattern_json)):
        visualization = get_visualization(name, path)
        solution = SJ.save_code_structure(pattern_json, visualization)
    
    path_to_html = "%s/views/default/%s.html" % (directory, name)
    return webbrowser.open(path_to_html)

def validate_parameters(name, path):
	""" Checks to see if parameters are correct.
		Attempting at robustness
	"""
    if (name not in ["pattern", "plumbum"]):
        print "ERROR: please enter 'pattern' or 'plumbum' as first parameter"
        return False
    
    split = path.split("/")
    try:
		# checking to see if accepted code base
        path_test = (name == split[-1] and name == split[-2])
    except IndexError:
        print "ERROR: incorrect directory. Please use ../plumbum/plumbum or ../pattern/pattern"
        return False
    else:
        if (not path_test):
            print "ERROR: incorrect directory. Please use ../plumbum/plumbum or ../pattern/pattern"
            return False
        return True
    

def get_visualization(name_of_code_base, path_to_code_base):
    """ """
    print "***begin %s analysis***" % (name_of_code_base)

    if (not validate_parameters(name_of_code_base, path_to_code_base)):
        return "Exiting Analysis"
    try:
		# find all python modules
		list_of_python_files = FH.find_python_files_in_project(path_to_code_base)
		print list_of_python_files
    except OSError:
	    return "ERROR: No such file or directory: %s" % (path_to_code_base)
	
    # pylint analysis
    pylint_analysis = PY.get_pylint_analysis(list_of_python_files) 
    
	# git analysis
	git_analysis = AM.get_git_analysis(path_to_code_base, list_of_python_files)

    for python_file in list_of_python_files:
		# fusion of results
        result = FR.fuse_file(path_to_code_base, python_file,
                              pylint_analysis[python_file], git_analysis[python_file])
		# save results for future queries. Caching
        SJ.save_file(result, python_file, path_to_code_base, name_of_code_base)

	# create structure to show
    solution = FS.create_structure(path_to_code_base, name_of_code_base,
                                   pylint_analysis, git_analysis, name_of_code_base, path_to_code_base)

    return solution
   
if __name__ == "__main__":
	from sys import argv
	
	if (len(argv) != 3):
		print "USAGE: python default.py <name_of_code_base> <path_to_code_base>"
	else:
		name = argv[1]
		path = argv[2]
		
		code_base(name.lower(), path.lower())
	
