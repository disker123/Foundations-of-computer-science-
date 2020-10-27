import math
import json

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




'''The originol accepts function replaced during task 16 (the intersection)
def accepts(dfa, start, accepting, st):
	state = start
	for i in st:
		state = dfa[state][i]
	return state in accepting
'''


#new accepts function designed during task16 (the intersection)
def accepts(dfa, start, accepting, st):
	#print(st)
	state = start
	for i in st:
		#print("before state change")
		#print(state)
		#print(i)
		state = dfa[state][i]
		#print("after state change")
		#print(state)
		state = (int(state))
	return state in accepting




'''
dfa = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}


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

def trace(dfa, start, accepting, st):
	tracelist = [start]
	state = start
	for i in st:
		state = dfa[state][i]
		tracelist.append(state);
	print(tracelist)
	return state in accepting
'''
trace(dfa_even, 0, {0}, "00111000")
trace(dfa_abst, 0, {1}, "0010001")
trace(dfa_traffic_light, 0, {0}, "00001110000" )
'''

#task 12
'''

def find_accepting(dfa, start, accepting, alph, path):
	visited = set()
	state = start
	if state in accepting:
		print("found")
		return path
	for i in alph:
		if state not in visited:
			path.add(i)

	find_accepting(dfa, dfa[state][i], accepting, alph)
	state = dfa[state][i]



	print("not found)")
	return false
'''


def find_accepting(dfa, start, accepting, alph):
	path = ""
	state_list = []
	state = start
	state_list.append(state)
	if state in accepting:
		return path
	while state not in accepting and state_list != list(dfa):
		#first move
		if dfa[state][alph[0]] in state_list:
			state = dfa[state][alph[1]]
			#print("flaging at the first element for adding 1")
			path = path + alph[1]
			state_list.append(state)
		else:
			state = dfa[state][alph[0]]
			#print("flaging at the first element for adding 0")
			path = path + alph[0] + ""
			state_list.append(state)
		
		if state in accepting:
			#print(state_list)
			return path
		if(len(state_list) > pow(len(dfa), 2)):
			break


	print(state_list)
	print("failed")



dfa_num = {0:{'0':3, '1':1},
       1:{'0':0, '1':2},
       2:{'0':1, '1':2},
       3:{'0':0, '1':0}}

dfa_al = {0:{'a':3, 'b':1},
      	1:{'a':0, 'b':2},
      	2:{'a':1, 'b':2},
       	3:{'a':0, 'b':0}}

dfa_large = {0:{'0':3, '1':1},
       1:{'0':4, '1':2},
       2:{'0':6, '1':4},
       3:{'0':2, '1':0},
       4:{'0':3, '1':7},
       5:{'0':4, '1':7},
       6:{'0':7, '1':0},
       7:{'0':0, '1':0}}

dfa_large_failure = {0:{'0':3, '1':1},
       1:{'0':5, '1':2},
       2:{'0':6, '1':7},
       3:{'0':2, '1':0},
       4:{'0':3, '1':7},
       5:{'0':3, '1':7},
       6:{'0':7, '1':0},
       7:{'0':0, '1':0}}
'''
print(find_accepting(dfa_num, 0, {2}, ['0', '1']));
print(find_accepting(dfa_al, 0, {2}, ['a', 'b']));
print(find_accepting(dfa_large, 0, {4}, ['0', '1']));
print(find_accepting(dfa_large_failure, 0, {4}, ['0', '1']));
'''
#print(len(dfa_num))

#task 13
'''
print (dfa_num)
print(dfa_num[0])
print(dfa_num[0]["0"])
temp = dfa_num[0]["0"]
print(temp)
dfa_num[0]["0"] = dfa_num[0]["1"]
dfa_num[0]["1"] = temp
print(dfa_num[0])
'''


def new_dfa(dfa, alph):
	print ("given dfa", dfa)
	#print(len(dfa))
	for i in range(0, len(dfa)):		
		#print("flag", i)
		temp = dfa[i][alph[0]]		
		dfa[i][alph[0]] = dfa[i][alph[1]]
		dfa[i][alph[1]] = temp
		#print(dfa[i])
	return dfa
'''
comp = new_dfa(dfa_num, ['0', '1'])
print("comp  dfa",comp)
'''


#task 14
#print(dfa_num)
#print(dfa_001)

def union_accept(dfa, start, st):
		state = start
		for i in st:
			state = dfa[state][i]
		#print(state)
		return state 

def union(dfa_a, dfa_b, start_a, start_b, acc_a, acc_b, alph):#(dfa, dfa, 0, 0, {1}, {2}, ['0', '1'])
	x = find_accepting(dfa_a, start_a, acc_a, alph)#0111
	y = find_accepting(dfa_b, start_b, acc_b, alph)#001
	dfa_u = {**dfa_num, **dfa_001}
	#print(dfa_u)
	a =union_accept(dfa_u, start_a, x)
	b =union_accept(dfa_u, start_b, y)
	accepting_list = {a, b}
	#print(accepting_list)
	#print(dfa_u)
	#print(accepts(dfa_u, start_a, accepting_list, x))#even lengthed dfa  #1
	return dfa_u

#task 15
def union_test(dfa_a, dfa_b, start_a, start_b, acc_a, acc_b, alph):#ex(dfa, dfa, 0, 0, {1}, {2}, ['0', '1'])
	x = find_accepting(dfa_a, start_a, acc_a, alph)
	y = find_accepting(dfa_b, start_b, acc_b, alph)
	dfa_u = {**dfa_num, **dfa_001}
	#print(dfa_u)
	a =union_accept(dfa_u, start_a, x)
	b =union_accept(dfa_u, start_b, y)
	accepting_list = {a, b}
	#print(accepting_list)
	#print(dfa_u)
	print(accepts(dfa_u, start_a, accepting_list, x))
	print(accepts(dfa_u, start_b, accepting_list, y))
	return 

'''
union_test(dfa_num, dfa_001, 0, 0, {2}, {3}, ['0', '1'])
union_test(dfa_even, dfa_even_binary_number, 0, 0, {0}, {0}, ['0', '1'])
union_test(dfa_odd_binary_number, dfa_abst, 0, 0, {0}, {1}, ['0', '1'])
union_test(dfa_element_to_state, dfa_traffic_light, 0, 0, {1}, {0}, ['0', '1'])
union_test(dfa_thermostat, dfa_even, 0, 0, {1}, {0}, ['0', '1'])
union_test(dfa_abst, dfa_element_to_state, 0, 0, {1}, {1}, ['0', '1'])
'''
#task 16
def intersect(dfa_1, dfa_2):
	dfa = {}
	for i in range(0, len(dfa_1)):
		for j in range(0, len(dfa_2)):
			#for k in alph:
			#print(i)
			keya = dfa_1[i]['0']
			#print(keya)
			key2a = dfa_2[j]['0']
			#print(key2a)
			key3a = keya + key2a
			#print(key3a)
						
			keyb = dfa_1[i]['1']
			#print(keyb)
			key2b = dfa_2[j]['1']
			#print(key2b)
			key3b = keyb + key2b
			#print(key3b)
			
			x = str(i)
			y = str(j)
			z = x + y
			#print(z)
			
			a = {'0':key3a}
			b = {'1':key3b}
			dfa[z] = (a, b)
			#dfa = {z:{'0':key3a, '1':key3b}}
			#dfa[z]['0'] = key3a
			#dfa[z]['1'] = key3a
			
			#print(dfa)
	return dfa

def accepts_inter(dfa, start, accepting, st):
	state = start
	for i in st:
		if(i == '0'):
			state = dfa[state][(0)]['0']
			#print("flagA")
			#print(state)
			#print("flag1")
		else:
			state = dfa[state][(1)]['1']
			#print("flagB")
			#print(state)
			#print("bla")
	return state in accepting


dfa_1 = {0:{'0':'1', '1':'0'},
       1:{'0':'2', '1':'1'},
       2:{'0':'2', '1':'2'}}

dfa_2 = {0:{'0':'0', '1':'1'},
       1:{'0':'1', '1':'2'},
       2:{'0':'2', '1':'2'}}

dfa_inter = (intersect(dfa_1, dfa_2))
#print(dfa_inter)

'''
{'00': ({'0': '10'}, {'1': '01'}), 
 '01': ({'0': '11'}, {'1': '02'}), 
 '02': ({'0': '12'}, {'1': '02'}), 
 '10': ({'0': '20'}, {'1': '11'}), 
 '11': ({'0': '21'}, {'1': '12'}), 
 '12': ({'0': '22'}, {'1': '12'}), 
 '20': ({'0': '20'}, {'1': '21'}), 
 '21': ({'0': '21'}, {'1': '22'}), 
 '22': ({'0': '22'}, {'1': '22'})}
'''


print("originol DFAs true")
print(accepts(dfa_1, 0, {1}, "111011111"))
print(accepts(dfa_2, 0, {1}, "000010000"))
print("originol DFAs false")
print(accepts(dfa_1, 0, {1}, "1110111011"))
print(accepts(dfa_2, 0, {1}, "0010010000"))

print("intersect DFA")
#print(dfa_inter)
print(accepts_inter(dfa_inter, '00', {'11'}, "01"))#true
print(accepts_inter(dfa_inter, '00', {'11'}, "10"))#true
print(accepts_inter(dfa_inter, '00', {'11'}, "101"))#false
print(accepts_inter(dfa_inter, '00', {'11'}, "100"))#false
