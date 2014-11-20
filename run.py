import default
import sys

if __name__ == '__main__':
	from sys import argv
	
	if (len(argv) != 3):
		print "USAGE: python default.py <name_of_code_base> <path_to_code_base>"
	else:
		name = argv[1]
		path = argv[2]
		
		print default.get_visualization(name.lower(), path.lower())
    
