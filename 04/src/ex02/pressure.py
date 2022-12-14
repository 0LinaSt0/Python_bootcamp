#include <
from random import uniform

FLIP_FLAG = "flip_flag"

def emit_gel(step):
	initial_pressure = uniform(50, 100)
	while True:
		initial_pressure += uniform(0, step)
		# Better way if there be 0 in this case 
		if initial_pressure < 50:
			initial_pressure = 50
		if initial_pressure > 100:
			initial_pressure = 100
		flag = (yield initial_pressure)
		if flag is not None:
			step *= -1
			print("STEP SIGNE WAS CHENGED")
		
if "__main__" == __name__:
	step = 4
	substitute = emit_gel(step)
	for pressure in substitute:
		print("on step: {}".format(pressure))
		if pressure < 20 or pressure > 80:
			substitute.send(FLIP_FLAG)
		if pressure < 10 or pressure > 90:
			substitute.close()
			print("SUCCESS EXIT")