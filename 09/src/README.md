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

Command for rebuilding library:
```shell
$ ../../../../rm.sh; rm -rf build/ Calculator.egg-info/; CC=gcc python3 setup.py install
```

##### Execution:
###### 1. Create module calculator [in folder ex00/]:
```shell
$ CC=gcc python3 setup.py install
```

#### EX02
##### Information:
Building a Python C Extension Module with Cython:
1. [In documentation](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html)

Command for rebuilding library:
```shell
rm -rf matrix.cpython-310-darwin.so, multiply.c; python3 setup.py build_ext --inplace
```

##### Execution:
###### 1. Create module matrix [in folder ex02/]:
```shell
$ python3 setup.py build_ext --inplace
```


