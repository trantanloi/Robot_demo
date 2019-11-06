===================================
Config enviroment run test automation:
download robot-framework
download pip
download seleniumlibrary
download pyyaml
pip install pyyaml
====================================
Run command line all folder test suite:
    robot -P ./Libs -d Report -i 1_1_2 "Test Suites"
Run command line only folder in folder Test Suite:
    obot -P ../Libs -d Report -i 1_1_2 Google/Google.robot  *Edit path to folder report*
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