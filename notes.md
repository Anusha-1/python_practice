# Python practice
best practices:
1. use the built in modules to the maximum rather than installing evrything. 
2. use named tuples instead of dict
3. class instantiate using dataclasses instead of conventional
4. map filter reduce use rather than for loops
5. for big data: numpy , pandas ,scipy  are going to help ,consider them even in django, flask application not just for data science ,ai ,ml
6. sometimes we should do the wrong things to know wt are wrong things: anti patterns
7. dont iterate over dictionary keys or list , instead use set  , set has hashing dict.get() also has hashing but it is done at that instance , set has pre existing
8. always close the files which are opened to prevent unnecessary memory leaks , resource manager is hanging in there if it is nt closed  
9. with is a context manager , use with keyword so that python will take care of memory leaks
10. orm is more professional (object relational management) than using select , insert, delete update etc..  ORM is mapping a table and columns to class and its  properties
11. 

"""
dos command : this will compile all python files 
python -m compileall

-m :module
python -m venv venv/  : 

activate.bat
deactivate.bat will be used for venv

npm install(js) == pip install (in pytohn)
"""
