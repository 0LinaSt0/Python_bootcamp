#!/usr/bin/env python

from distutils.core import setup, Extension

def main():
	modulel = Extension('calculator', sources = ['calculator.c'])

	setup(
		name='Calculator',
		version='0.0',
		description='A simple calculator module for Python',
		author="Msalena",
		ext_modules=[modulel]
	)

if __name__ == "__main__":
	main()