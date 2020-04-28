===================================
Config enviroment run test automation:
download robot-framework
download pip
download seleniumlibrary
download pyyaml
pip install pyyaml

if system using python and ironpython:
    - IronPython:
    ipy -m pip install ....
    - Python:
    py -m pip install ....
====================================
Run robot framework with ironpython:
    ipy -m robot .....
Run robot framework with python:
    py -m robot ....
====================================
Run command line all folder test suite:
    robot -P ./Libs -d Report -i 1_1_2 "Test Suites"
Run command line only folder in folder Test Suite:
    robot -P ../Libs -d Report -i 1_1_2 Google/Google.robot  *Edit path to folder report*
Run command line only test suite:
    robot -P ../../Libs -d Report -i 1_1_2 Google.robot  *Edit path to folder report*
====================================
Command line options for post-processing outputs:
-P, --pythonpath <path>
 	Additional locations to add to the module search path.
-r, --report <file>
 	Sets the path to the generated report file.
-i, --include <tag>
 	Selects the test cases by tag.
-e, --exclude <tag>
 	Selects the test cases by tag.
-d, --outputdir <dir>
 	Defines where to create output files.

========
link website demo: https://phptravels.com/demo/