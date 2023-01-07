import calculator

if __name__ == "__main__":
	a = 3
	b = 4
	c = 50
	d = 0

	# INTEGERS
	print("({} + {}): \n{}\n\n".format(a, b, calculator.add(a, b)))
	print("({} + {}): \n{}\n\n".format(a, c, calculator.add(a, c)))

	print("({} - {}): \n{}\n\n".format(c, b, calculator.sub(c, b)))
	print("({} - {}): \n{}\n\n".format(a, c, calculator.sub(a, c)))

	print("({} * {}): \n{}\n\n".format(d, b, calculator.mul(d, b)))
	print("({} * {}): \n{}\n\n".format(a, c, calculator.mul(a, c)))

	print("({} / {}): \n{}\n\n".format(c, b, calculator.div(c, b)))
	print("({} / {}): \n{}\n\n".format(a, d, calculator.div(a, d)))

	# FLOATS (doesn't work)

	x = 3.9
	y = 4.7
	print("({} + {}): \n{}\n\n".format(x, y, calculator.add(x, y)))