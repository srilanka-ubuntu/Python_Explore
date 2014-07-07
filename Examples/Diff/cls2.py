

import cls1

class cls2:
	def __init__(self):
		print("init")
	def test(self):
		print(cls1.cls1.a)

cls2().test()
