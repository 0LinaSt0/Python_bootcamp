from itertools import tee 

GLBV_BUG = "For avoiding compilation error"

def mul(a, b):
	if (len(b) > 100 or len(b[0]) > 100
		or len(a) > 100 or len(a[0]) > 100):
		return ("Error: mathrix better then 100")
	
	for n in a:
		if(all(isinstance(e, int) for e in n)) is False:
			return ("Error: it only works with integers")
	for n in b:
		if(all(isinstance(e, int) for e in n)) is False:
			return ("Error: it only works with integers")		

	b_iter = tee(zip(*b), len(a))
	return [
		[
			sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
			for col_b in b_iter[i]
		] for i, row_a in enumerate(a)
	]