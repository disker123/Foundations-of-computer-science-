import math

class alphabet:
	#list of strings
	
	def __init__(self, elements):
		self.alphabet = elements
	def __repr__(self):
		return str(self.alphabet)
	#print function
	def output(self):
		print(self.alphabet)
	def size(self):
		return len(self.alphabet)
	def elements(self, index: int):
		return self.alphabet[index]
#alphabet test1
'''
alph = [5, 7, "hello", "world"]
x = alphabet(alph)
print(x)
alph2 = [1, 2, "this is the second"]
x = alphabet(alph2)
#x.output()
print(x)
print(x.size())
'''

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
	def append(self, elem):
		self.string.append(elem)
#string test
'''
a = char("5")
b = char("7")
c = char("hello")
d = char("world")
y = [a, b, c, d]
x = string(y)
print(x)
'''

'''def Ngen(alphabet: alpha, int: n):
	collum = log(n+1, alpha.size())
	row = n - alpha.size()**collum
'''
'''
class cart_pro:
	def __init__(self, lst, rep):
		self.lst,	self.rep = rep

	def __iter__(self):
		self.pos = 0
		return self
	
	def __next__(self):
		#if(self.pos >= len(self.lst)**self.rep)
		#	raise StopIteraion
		n = self.pos
		product = []
		self.pos +=1
		for i in range(self.rep -1, -1, -1):
			position = int(n / len(self.lst)**i)
			product.append(self.lst[position])
			n %= leng(self.lst)**i
		return product 



for j in cart_pro([0,1,2,3],4):
		print(j)
'''

def Nthstr(alpha: alphabet, n: int):
	depth = math.floor(math.log(n+1, alpha.size()))#solve for the collum in the LExi order drawing
	#print("the depth is: ", depth)
	n = n - alpha.size()**(depth) + 1#get the index of the elemt
	n = math.floor(n)
	#print("and the n is: ", n)
	
	#print(n)
	lexi = []
	for pos in range(depth-1, -1, -1):
		lexi.append(alpha.alphabet[math.floor(n / alpha.size()**pos)])
		n = n % alpha.size()**pos
	return lexi

'''
n=12
alpha = alphabet(['0', '1'])
for n in range(n):#show all elements to test
	print(n, "	", end=":")
	print(Nthstr(alpha, n,))#shows the Nth 
#	print("flag")
'''


'''dfa = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}
'''#first test DFA  

dfa = {0:{'0':1, '1':1},
       1:{'0':1, '1':1}}  

def DFA_test(dfa, start, accepting, x):
    state = start
    for c in x:
        state = dfa[state][c]
    return state in accepting


#print(accepts(dfa, 0, {1}, "01100110001"))
	
print(DFA_test(dfa, 1, {0}, ''))#this DFA accepts the nostring
