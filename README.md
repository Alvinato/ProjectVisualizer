STEPS TO RUN VISUALIZATION

to see visualization:
1. clone 410 project JAAT - https://v0o7@stash.ugrad.cs.ubc.ca:8443/scm/cs_410/jaat.git

2. go to directory ../jaat/views/default/
3. open plumbum.html or pattern.html

STEPS TO RUN BACKEND
1. clone 410 project JAAT - https://v0o7@stash.ugrad.cs.ubc.ca:8443/scm/cs_410/jaat.git
2. clone codebase pattern - https://github.com/clips/pattern.git
3. clone codbase plumbum - https://github.com/tomerfiliba/plumbum.git
3. download python 2 (2.7.6+)
4. install pylint library

4. goto directory ../jaat/
5. run command "python run.py A B", where A = pattern or plumbum, and B = FULL path to codebase

NOTE: We are only analyzing the actual source code, not miscellaneous directories (examples, test, etc.), so for the B, specify plumbum/plumbum or pattern/pattern
[e.g. on linux undergrad, full path for me is: /home/v/v0o7/git/plumbum/plumbum or /home/v/v0o7/git/pattern/pattern: