****************
***  GENERAL ***
****************

About
-----
We are Team JAAT

Requirements
------------
1. Must have FireFox 33+
2. Run code on MAC OS X and Ubuntu 14.04 
	a. Code dependant on UNIX commands, so no Windows. 
	b. Unable to test on Undergrad account as I was unable to install pylint
3. Have Python 2 (2.7.6+)
4. Steps assume that python package manager (pip) is installed

History
-------
2010.05.24 Taranbir and Arjun met in CPSC 111 Tutorial
2012.03.14 Arjun and Jason met through a mutual friend in CPSC 213
2014.02.26 Jason and Taranbir met in CPSC 319
2014.09.14 Jason found Alvin looking for a group

Inspiration
------------
https://www.youtube.com/watch?v=b_ILDFp5DGA

****************
*** RUN CODE ***
****************

Visualization
-------------
1. clone 410 project JAAT - https://v0o7@stash.ugrad.cs.ubc.ca:8443/scm/cs_410/jaat.git
2. go to directory ../jaat/views/default/
3. open plumbum.html or pattern.html

Back-end
-------------
1. clone 410 project JAAT - https://v0o7@stash.ugrad.cs.ubc.ca:8443/scm/cs_410/jaat.git
2. clone codebase pattern - https://github.com/clips/pattern.git
3. clone codbase plumbum - https://github.com/tomerfiliba/plumbum.git
4. Install pylint python package (sudo apt-get pip install pylint)
5. goto directory ../jaat/
6. run command "python run.py A B", where A = pattern or plumbum, and B = FULL path to codebase

NOTE: We are only analyzing the actual source code, not miscellaneous directories (examples, test, etc.), so for the B, specify plumbum/plumbum or pattern/pattern
[e.g. on linux undergrad, full path for me is: /home/v/v0o7/git/plumbum/plumbum or /home/v/v0o7/git/pattern/pattern:

****************
*** TESTING  ***
****************

Back End
-------------
1. Install nose python package (sudo apt-get pip install nose)
2. Go to ../jaat/modules directory, and type 'nosetests'
3. Output is displayed on console

Unit Tests
-----------------
test_filehelper.py
test_gitmetrics.py
test_pylintanalyzer.py
test_savejson.py

Integration Tests
-----------------
test_fusor.py
- tests overall fusion algorithm

test_authormapper.py
- tests grabbing results from gitmetrics.py and filehelper.py

Visualization
--------------

TESTS													EXPECTED										ACTUAL
-----------------------------------------------------------------------------------------------------------------
General:
01	Click on a Bubble									Move further into directory						PASS
02	Click outside range of bubble						N/A												PASS
03	Click two bubbles above current directory			Go back to top level							PASS
04	Switch Focus 										Focus on clicked bubble							PASS
05	Click a file										Show file										PASS
06	Scroll through file									See lines of code								PASS
07	Hover over bubble									Darker Black outline appears					PASS
08	Name is centre of project

Plumbum:
09	Colour of fs directory								Blue and Red module colour, Purple colour		PASS
10	Number of directories visible at start				5 directories, 2 modules						PASS

Pattern:
11	Colour of Bubble tree.py							green											PASS
12	Colour of vector directory							light green, mostly green						PASS
13	Colour of overall project							light green, mostly green						PASS
