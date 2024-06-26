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
#first test DFA  
'''

'''
dfa = {0:{'0':1, '1':1},
       1:{'0':1, '1':1}}  
'''
def accepts(dfa, start, accepting, st):
    state = start
    for i in st:
        state = dfa[state][i]
    return state in accepting
'''
#print(accepts(dfa, 0, {1}, "01100110001"))
	
print(accepts(dfa, 0, {0}, ''))#this DFA accepts the empty string
print(accepts(dfa, 0, {0}, '1'))
print(accepts(dfa, 0, {0}, '0'))
'''

'''
x = 'a'

x = input("enter a single character ")
dfa = {0:{x:1},
       1:{x:2},
       2:{x:2}}

print(accepts(dfa, 0, {1}, x))#accepts a string of 1 char
x+=x
print(x)
print(accepts(dfa, 0, {1}, x))#fails on 'aa'
'''

dfa_even = {0:{'0':1, '1':1},
       1:{'0':0, '1':0}}

dfa_even_binary_number = {0:{'0':0, '1':1},
       1:{'0':0, '1':1}}

dfa_odd_binary_number = {0:{'1':0, '0':1},
       1:{'1':0, '0':1}}

dfa_name = {0:{'g':1},
       1:{'r':1, 'e':1, 'g':1}}
       
dfa_abst = {0:{'0':0, '1':1},
       1:{'0':2, '1':1},
       2:{'0':1, '1':1}}

dfa_element_to_state = {0:{'0':0, '1':1},
       1:{'0':0, '1':1}}

dfa_three_states = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}

dfa_traffic_light = {0:{'0':0, '1':1},#green
       1:{'0':2, '1':2},#yellow
       2:{'0':0, '1':2}}#red

dfa_thermostat = {0:{'1':1, '0':0},
       1:{'1':1, '0':0}}

dfa_001 = {0:{'1':0, '0':1},
       1:{'0':2, '1':0},
       2:{'0':2, '1':3},
       3:{'0':3, '1':3}}


'''
print(accepts(dfa_even, 0, {0}, "00000000"))#even lengthed dfa  #1
print(accepts(dfa_even_binary_number, 0, {0}, "11010"))#even number dfa #2
print(accepts(dfa_odd_binary_number, 1, {0}, "110101"))#odd number dfa #3
print(accepts(dfa_name, 0, {1}, "greg"))#my name #4
print(accepts(dfa_abst, 0, {1}, "0010001"))#abstract dfa from sec 1.4 #5
print(accepts(dfa_element_to_state, 0, {1}, "0001101"))#goes to the state of the element 0->0 1->1 #6
print(accepts(dfa_element_to_state, 0, {1}, "0001101"))#three states #7
print(accepts(dfa_traffic_light, 0, {0}, "00001110000"))#stays green when no cars are waiting then turns yellow for a tick then stays red while there are cars waiting and turns green when there are none #8
print(accepts(dfa_thermostat, 0, {1}, "0011001"))#thermostat on when hot (1) and off when not (0) goal is to be on #9
print(accepts(dfa_001, 0, {3}, "0110010101"))#accepts if there is 001 in the string #10
'''





#print("This marks the start of checkpoint 2 task 11")
#task11

def trace(dfa, start, accepting, st, ):
	tracelist = [start]
	state = start
	for i in st:
		state = dfa[state][i]
		tracelist.append(state);
	print(tracelist)
	return state in accepting

trace(dfa_even, 0, {0}, "00111000")
trace(dfa_abst, 0, {1}, "0010001")
trace(dfa_traffic_light, 0, {0}, "00001110000" )


