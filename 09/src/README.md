## PREPARING STEPS
#### 1. Install venv:
```shell
$ python -m pip install virtualenv
$ virtualenv venv
```

#### 2. Activate venv:
```shell
$ source venv/bin/activate OR . venv/bin/activate
```

#### 3. Install requiements:
```shell
$ pip3 install -r requirements.txt
```

---
## EXERCISES

#### EX00 
##### Information:

Building a Python C Extension Module:
1. [Real Python](https://realpython.com/build-python-c-extension-module/#raising-exceptions)

2. [In documentation](https://python.readthedocs.io/en/v2.7.2/extending/extending.html)

Command for rebuilding library and starting TEST.py:
```shell
$ ../../../../rm.sh; rm -rf build/ Calculator.egg-info/; CC=gcc python3 setup.py install; python3 TEST.py
```

##### Execution:
###### 1. []:
```shell
$ 
```

#### EX01
##### Information:

##### Execution:
###### 1. []:
```shell
$ 
```

#### EX02
##### Information:
Building a Python C Extension Module with Cython:
1. [In documentation](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html)

Command for rebuilding library and starting TEST.py:
```shell
rm -rf matrix.cpython-310-darwin.so, multiply.c build; python3 setup.py build_ext --inplace; python3 TEST.py
```

##### Execution:
###### 1. []:
```shell
$ 
```


