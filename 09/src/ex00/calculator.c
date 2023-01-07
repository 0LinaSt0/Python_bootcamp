#include <Python.h>
#include <stdio.h>

// Function is equivalent to the expression: 
//	1. (int)a + (int)b 
int add_int(int a, int b){
	return (a + b);
}

// Function is equivalent to the expression: 
//	1. (float)a + (float)b
//	2. (int)a + (float)b 
//	3. (float)a + (int)b 
float add_float(float a, float b){
	return (a + b);
}

#define add(X, Y) _Generic((X), \
	float: _Generic((Y), \
			default: add_float ), \
	int: _Generic((Y), \
			int: add_int, \
			default: add_float ),\
	default: add_float \
	) (X, Y)


static PyObject *method_add(PyObject *self, PyObject *args){
	int a, b;
	int result;

	//Parse arguments
	if(!PyArg_ParseTuple(args, "ii", &a, &b)){
		//PyErr_SetString(PyExc_ValueError, "TypeError: integer argument expected, got float");
		return (NULL);
	}

	result = add(a, b);

	//Excecute and return function's result
	return(PyLong_FromLong(result));
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


// Function is equivalent to the expression:
//	1. (int)a - (int)b
int sub_int(int a, int b){
	return (a - b);
}

// Function is equivalent to the expression:
//	1. (float)a - (float)b
//	2. (int)a - (float)b 
//	3. (float)a - (int)b 
float sub_float(float a, float b){
	return (a - b);
}

#define sub(X, Y) _Generic((X), \
	float: _Generic((Y),\
			default: sub_float ), \
	int: _Generic((Y), \
			int: sub_int, \
			default: sub_float ), \
	default: sub_float \
	) (X, Y)


static PyObject *method_sub(PyObject *self, PyObject *args){
	int a, b;
	int result;

	//Parse arguments
	if(!PyArg_ParseTuple(args, "ii", &a, &b)){
		return (NULL);
	}

	result = sub(a, b);

	//Excecute and return function's result
	return(PyLong_FromLong(result));
}


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


// Function is equivalent to the expression:
//	1. (int)a * (int)b 
int mul_int(int a, int b){
	return (a * b);
}

// Function is equivalent to the expression:
//	1. (float)a * (float)b 
//	2. (int)a * (float)b 
//	3. (float)a * (int)b
float mul_float(float a, float b){
	return (a * b);
}

#define mul(X, Y) _Generic((X), \
	float: _Generic((Y), \
			default: mul_float ), \
	int: _Generic((Y), \
			int: mul_int, \
			default: mul_float ),\
	default: mul_float \
	) (X, Y)


static PyObject *method_mul(PyObject *self, PyObject *args){
	int a, b;
	int result;

	//Parse arguments
	if(!PyArg_ParseTuple(args, "ii", &a, &b)){
		return (NULL);
	}

	result = mul(a, b);

	//Excecute and return function's result
	return(PyLong_FromLong(result));
}


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

/*
typedef void (*throw_t)(char *);
typedef int (*try_t)(int, int, throw_t);
typedef int (*catch_t)(char *);


int try_catch(try_t try, catch_t catch, int a, int b) {
	__label__ fail;
	// Throw exceptions function
	void throw(void){
		goto fail;
	}
	// Let's execute operation in try block
	return try(a, b, throw);
	
  fail:
	// If trow executed -> go catch block
	if(catch != 0){
		return catch(err);
	}
	return 0;
}

int try_div(int a, int b, throw_t throw){
	if (b == 0) {
		throw("F");
	}
	return(a / b);
}

int catch_error(char *err){
	fputs(err, stderr);
	return(0);
}
*/


typedef struct s_inform {
	int	result;
	int	fl_except;
} t_inform;



// Function is equivalent to the expression: 
//	1. a / b 
t_inform div_int(int a, int b){
	t_inform inform;

	if (b == 0){
		inform.result = 0;
		inform.fl_except = 1;
	} else {
		inform.result = (a / b);
		inform.fl_except = 0;
	}
	return (inform);
}

// Function is equivalent to the expression: 
//	1. (float)a / (float)b
//	2. (int)a / (float)b 
//	3. (float)a / (int)b 
float div_float(float a, float b){
	return (a / b);
}


#define div(X, Y) _Generic((X), \
	float: _Generic((Y), \
			default: div_float ), \
	int: _Generic((Y), \
			int: div_int, \
			default: div_float ), \
	default: div_float \
	) (X, Y)


static PyObject *method_div(PyObject *self, PyObject *args){
	int a, b;
	t_inform result;

	//Parse arguments
	if(!PyArg_ParseTuple(args, "ii", &a, &b)){
		return (NULL);
	}

	result = div(a, b);
	if (result.fl_except){
		/* Passing custom exception */
		PyErr_SetString(StringTooShortError, "String length must be greater than 10");
		return NULL;
	}

	//Excecute and return function's result
	return(PyLong_FromLong(result.result));
}


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


//Method add() description
static PyMethodDef CalculatorMethods[] = {
	{
		"add", 
		method_add, 
		METH_VARARGS, 
		"Function is equivalent to the expression (a + b)"
	},
	{
		"sub", 
		method_sub, 
		METH_VARARGS, 
		"Function is equivalent to the expression (a - b)"
	},
	{
		"mul", 
		method_mul, 
		METH_VARARGS, 
		"Function is equivalent to the expression (a - b)"
	},
	{
		"div", 
		method_div, 
		METH_VARARGS, 
		"Function is equivalent to the expression (a - b)"
	},
	{ NULL, NULL, 0, NULL }
} ;

//Module calculator description
static struct PyModuleDef calculatormodules = {
	PyModuleDef_HEAD_INIT,
	"calculator",
	"A simple calculator module for Python",
	-1,
	CalculatorMethods
} ;

//Defines module calculator
PyMODINIT_FUNC PyInit_calculator(void){
	return PyModule_Create(&calculatormodules);
}