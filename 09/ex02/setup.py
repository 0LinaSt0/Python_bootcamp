#!/usr/bin/env python3

from setuptools import Extension, setup
from Cython.Build import cythonize

def main():
	cython_ext = Extension("matrix", ["multiply.pyx"])
	setup(
		name="Matrix",
		description="Module for multiplying matrices",
		author="Msalena",
		ext_modules=cythonize(cython_ext)
	)

if __name__ == "__main__":
	main()