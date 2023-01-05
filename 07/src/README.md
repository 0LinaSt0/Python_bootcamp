## PREPARING STEPS
#### 1. Install venv:
	$ python -m pip install virtualenv
	$ virtualenv venv

#### 2. Activate venv:
	$ source venv/bin/activate OR . venv/bin/activate

#### 3. Install requiements:
	$ pip3 install -r requirements.txt

---
## EXERCISES

#### EX00 information:

###### 1. Start server [in folder "ex00/"]:
```shell
$ python3 main.py
```

#### EX01 information:

###### 1. Change permission [in folder "ex01/tests/srcs_tests"]:
```shell
$ chmod 000 without_permission.json
$ chmod 000 without_permission_answers.json
```

###### 2. Start tests with next command [in folder "ex01/tests/"]:
```shell
$ coverage run -m --source=../../ex00/ pytest -v
```

###### 3. Check which files were tested [in folder "ex01/tests/"]:
```shell
$ coverage report -m
```

#### EX02 information:
Creating documentation with sphinx:
```shell
$ sphinx-quickstart docs
```

Create html file with documentation
```shell
$ sphinx-build -b html docs/source/ docs/build/html
```

Start server and look at documetation [in folder "ex02/"] in way: http://localhost:8000/docs/build/html/index.html

