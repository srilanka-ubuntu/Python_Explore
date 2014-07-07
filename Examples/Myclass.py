class MyClass(object):
	"""A simple example class"""
	r="instance"
	def __init__(self):
		print("initialized")
		self.r = "test"
	def fi(self,some):
		print("hello world %s >>> %s", self.r,some)


