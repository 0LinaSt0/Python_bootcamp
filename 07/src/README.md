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

###### 1. Change permission [in folder "ex01/tests/srcs_quiestions"]:
```shell
$ chmod 000 without_permission.json
```

###### 2. Start tests with next command [in folder "ex01/tests/"]:
```shell
$ coverage run -m pytest -v
```

###### 3. Check wich files were tested [in folder "ex01/tests/"]:
```shell
$ coverage report
```

#### EX02 information:

