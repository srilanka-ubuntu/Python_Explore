ord_list = [ 1,2,3,4,5,6,7]

for ol in ord_list:
	print(ol)

print("----------------- ");

gen_list = (1,2,3,4,5,6,7)

for gl in gen_list:
	print(gl)

def test():
	for gl in gen_list:
		yield gl*2

y_list = test()

for yl in y_list:
	print(yl)
