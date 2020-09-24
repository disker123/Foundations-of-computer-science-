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
def DFA_test(dfa, start, accepting, x):
    state = start
    for c in x:
        state = dfa[state][c]
    return state in accepting

'''
#print(DFA_test(dfa, 0, {1}, "01100110001"))
	
print(DFA_test(dfa, 0, {0}, ''))#this DFA accepts the empty string
print(DFA_test(dfa, 0, {0}, '1'))
print(DFA_test(dfa, 0, {0}, '0'))
'''

'''
x = 'a'

x = input("enter a single character ")
dfa = {0:{x:1},
       1:{x:2},
       2:{x:2}}

print(DFA_test(dfa, 0, {1}, x))#accepts a string of 1 char
x+=x
print(x)
print(DFA_test(dfa, 0, {1}, x))#fails on 'aa'
'''

dfa_even = {0:{'0':1, '1':1},
       1:{'0':0, '1':0}}

dfa_even_binary_number = {0:{'0':0, '1':1},
       1:{'0':0, '1':1}}

dfa_odd_binary_number = {0:{'1':0, '0':1},
       1:{'1':0, '0':1}}

dfa_name = {0:{'g':1, 'r':0, 'e':0},
       1:{'r':2, 'e':0, 'g':0},
       2:{'e':3, 'g':0, 'r':0},
       3:{'g':4, 'r':0, 'e':0},
       4:{'g':0, 'r':0, 'e':0}}
       
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



print(DFA_test(dfa_even, 0, {0}, "00000000"))#even lengthed dfa  #1
print(DFA_test(dfa_even, 0, {0}, "11111111"))
print(DFA_test(dfa_even, 0, {0}, "0000000"))
print(DFA_test(dfa_even, 0, {0}, "1111111"))
print(DFA_test(dfa_even, 0, {0}, "000000001"))
print(DFA_test(dfa_even, 0, {0}, "111111110"))
print("\n")
print(DFA_test(dfa_even_binary_number, 0, {0}, "11010"))#even number dfa #2
print(DFA_test(dfa_even_binary_number, 0, {0}, "11011"))
print(DFA_test(dfa_even_binary_number, 0, {0}, "110101"))
print(DFA_test(dfa_even_binary_number, 0, {0}, "011010"))
print(DFA_test(dfa_even_binary_number, 0, {0}, "11010"))
print(DFA_test(dfa_even_binary_number, 0, {0}, "11010"))
print("\n")
print(DFA_test(dfa_odd_binary_number, 1, {0}, "110101"))#odd number dfa #3
print(DFA_test(dfa_odd_binary_number, 1, {0}, "110100"))#odd number dfa #3
print(DFA_test(dfa_odd_binary_number, 1, {0}, "1101010"))#odd number dfa #3
print(DFA_test(dfa_odd_binary_number, 1, {0}, "1101000010101"))#odd number dfa #3
print(DFA_test(dfa_odd_binary_number, 1, {0}, "001110101"))#odd number dfa #3
print(DFA_test(dfa_odd_binary_number, 1, {0}, "100011101010"))#odd number dfa #3
print("\n")
print(DFA_test(dfa_name, 0, {4}, "greg"))#my name #4
print(DFA_test(dfa_name, 0, {4}, "gregg"))
print(DFA_test(dfa_name, 0, {4}, "gre"))
print(DFA_test(dfa_name, 0, {4}, "grege"))
print(DFA_test(dfa_name, 0, {4}, "rgreg"))
print(DFA_test(dfa_name, 0, {4}, "ggegegreg"))
print("\n")
print(DFA_test(dfa_abst, 0, {1}, "0010001"))#abstract dfa from sec 1.4 #5
print(DFA_test(dfa_abst, 0, {1}, "0010000"))
print(DFA_test(dfa_abst, 0, {1}, "0011000010"))
print(DFA_test(dfa_abst, 0, {1}, "0000000"))
print(DFA_test(dfa_abst, 0, {1}, "001000111111111111110"))
print(DFA_test(dfa_abst, 0, {1}, "10101010101010101"))#0-1-2-1-2-1-2-1...
print("\n")
print(DFA_test(dfa_element_to_state, 0, {0}, "000000"))#goes to the state of the element 0->0 1->1 #6
print(DFA_test(dfa_element_to_state, 0, {0}, "11111"))
print(DFA_test(dfa_element_to_state, 0, {1}, "00000"))
print(DFA_test(dfa_element_to_state, 0, {1}, "11111"))
print(DFA_test(dfa_element_to_state, 0, {1}, "0001101011101"))
print(DFA_test(dfa_element_to_state, 0, {1}, "00011010111010"))
print("\n")
print(DFA_test(dfa_traffic_light, 0, {0}, "000011100001110"))#stays green when no cars are waiting then turns yellow for a tick then stays red while there are cars waiting and turns green when there are none #8
print(DFA_test(dfa_traffic_light, 0, {0}, "1100000"))
print(DFA_test(dfa_traffic_light, 0, {0}, "000011"))
print(DFA_test(dfa_traffic_light, 0, {0}, "11111"))#rush hour
print(DFA_test(dfa_traffic_light, 0, {0}, "000000000"))#2 A.M.
print(DFA_test(dfa_traffic_light, 0, {0}, "011001010001"))
print("\n")
print(DFA_test(dfa_001, 0, {3}, "001"))#accepts if there is 001 in the string #10
print(DFA_test(dfa_001, 0, {3}, "0000000"))
print(DFA_test(dfa_001, 0, {3}, "011011100"))
print(DFA_test(dfa_001, 0, {3}, "0110010101"))
print(DFA_test(dfa_001, 0, {3}, "111111111111111001"))
print(DFA_test(dfa_001, 0, {3}, "0000000000000001"))
