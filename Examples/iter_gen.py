
class itgen():

	li = [78,23,2,3,5,6,7,5]

    def __init__(self):
		print(self)
		print("intialized")
	def __iter__(self):
		for t in li:
			print(t)

