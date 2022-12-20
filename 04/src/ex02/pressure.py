from random import uniform

FLIP_FLAG = "flip_flag"
MIN_PRESSURE = 0 #should be 0 in this case
MAX_PRESSURE = 100
STEP = 4


def emit_gel(step):
	initial_pressure = uniform(MIN_PRESSURE, MAX_PRESSURE)
	while True:
		initial_pressure += uniform(0, step)
		if initial_pressure < MIN_PRESSURE:
			initial_pressure = MIN_PRESSURE
		if initial_pressure > MAX_PRESSURE:
			initial_pressure = MAX_PRESSURE
		flag = (yield initial_pressure)
		if flag is not None:
			step = -step
			print("---> NOW STEP ", step)


if "__main__" == __name__:
	substitute = emit_gel(STEP)
	for pressure in substitute:
		print("on step: ", pressure)
		if pressure < 20 or pressure > 80:
			substitute.send(FLIP_FLAG)
		if pressure < 10 or pressure > 90:
			substitute.close()
			print("---> SUCCESS EXIT")
