class alphabet:
	#list of strings
	
	def __init__(self, elements):
		self.alphabet = elements
	def __repr__(self):
		return str(self.alphabet)
	#print function
	def output(self):
		print(self.alphabet)

#alphabet test1

alph = [5, 7, "hello", "world"]
x = alphabet(alph)
print(x)
alph2 = [1, 2, "this is the second"]
x = alphabet(alph2)
#x.output()
print(x)

class char:
	#a thing
	def __init__(self, thing):
		self.thing = thing

	def __repr__(self):
		return self.thing

#character test
'''
c = "hello world"
x = char(c)
print(x)
'''

class string:
	# a list of char
	def __init__(self, elements):
		self.string = elements
	def __repr__(self):
		return str(self.string)
	def output(self):
		print(self.string)
#string test

a = char("5")
b = char("7")
c = char("hello")
d = char("world")
y = [a, b, c, d]
x = string(y)
print(x)


