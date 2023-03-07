**QUICKSTART**
================================================
.. note::
    The description of how to work with the test.
    Follow this easy steps for starting test of **Voight-Kampff test**


1. Change permission [in folder "ex01/tests/srcs_tests"]:
    ``~$ chmod 000 without_permission.json``
    
    ``~$ chmod 000 without_permission_answers.json``



2. Start tests with next command [in folder "ex01/tests/"]:
    ``~$ coverage run -m --source=../../ex00/ pytest -v``



3. Check which files were tested [in folder "ex01/tests/"]:
    ``~$ coverage report -m``