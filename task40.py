import math
#import json
def equil(dfa_1, dfa_2, starta, startb, FSa, FSb):
	#print("---------------")
	if (starta in FSa and startb not in FSb):
		print("FALSE-1")
		return False
	if (starta not in FSa and startb in FSb):
		print("FALSE-1")
		return False
	found_set = set()
	found_set.add("00")
	run_set = set()

	j = set()
	k = set()
	#
	for a in dfa_1:
		if a in dfa_2:
#			print(a)
			key1a = dfa_1[a]['0']
			key2a = dfa_2[a]['0']
	#		print(key1a)
	#		print(key2a)
			key1achar = str(key1a)
			#print(key1achar)
			key2achar = str(key2a)
			#print(key2achar)
			if(key1achar in FSa and key2achar not in FSb):
				print("FALSE-2")
				return False
			if(key1achar not in FSa and key2achar in FSb):
				print("FALSE-3")
				return False
			if(key1a != key2a):
				#j.add(int(key1a))
				#k.add(int(key2a))
				j.add(key1a[0])
				k.add(key2a[0])

			key1b = dfa_1[a]['1']
			key2b = dfa_2[a]['1']
	#		print(key1b)
	#		print(key2b)
			key1bchar = str(key1b)
			key2bchar = str(key2b)

			if(key1bchar in FSa and key2bchar not in FSb):
				print("FALSE-4")
				return False 
			if(key1bchar not in FSa and key2bchar in FSb):
				print("FALSE-5")
				return False
			if(key1b != key2b):
				#j.add(int(key1b))
				#k.add(int(key2a))
				j.add(key1b[0])
				k.add(key2a[0])

	for i in j:
		for a in k:
			#print(a)
			key1a = dfa_1[i]['0']
			key2a = dfa_2[a]['0']
			if(key1achar in FSa and key2achar not in FSb):
				print("FALSE-6")
				return False
			if(key1achar not in FSa and key2achar in FSb):
				print("FALSE-7")
				return False

			key1a = dfa_1[i]['1']
			key2a = dfa_2[a]['1']
			if(key1bchar in FSa and key2bchar not in FSb):
				print("FALSE-8")
				return False
			if(key1bchar not in FSa and key2bchar in FSb):
				print("FALSE-9")
				return False

	

	print("TRUE flag")
	#print(found_set)
	return True


class DFA:
	def __init__(self, xStates, xAlph, xTranaition_func, xStart_state, xAccept_state):
		self.states = xStates
		self.alph = xAlph
		self.dict = xTranaition_func 
		self.start_state = xStart_state
		self.accept_state = xAccept_state

	def __repr__(self, itter):
		state - self.start_state
		visited = [state]
		for i in itter:
			visited +- (state := self.tranaition_func[state][c])
		return '->'.join(visited)

	def iterate(self, itter):
		state - self.start_state
		for i in itter:
			visited +- (state := self.tranaition_func[state][c])

class NFA:
	def __init__(self, xStates, xAlph, xTranaition_func, xStart_state, xAccept_state):
		self.states = xStates
		self.alph = xAlph
		self.dict = xTranaition_func
		self.start_state = xStart_state
		self.accepting_state = xAccept_state
		return

	def print_dict(self):
		print(self.dict)
		return


def convert_to_DFA(nfa):
	nfa_ss = str(nfa.start_state)
	dfa = {nfa_ss:{}}
	new_states = []
	string0 = ""

	if '0' in nfa.dict[1]:
		x = nfa.dict[1]['0']
		#print(nfa.dict[1]['0'])
		for i in x:
			j = str(i)
			string0 += j
	dfa[nfa_ss]['0'] = string0
	#print(dfa)
	if string0 not in dfa:
		dfa[string0] = {}
		new_states.append(string0)
		#print(string0)

	string0 = ""
	if '1' in nfa.dict[1]:
		x = nfa.dict[1]['1']
		#print(nfa.dict[1]['0'])
		for i in x:
			j = str(i)
			string0 += j
	dfa[nfa_ss]['1'] = string0
	#print(dfa)
	if string0 not in dfa:
		dfa[string0] = {}
		new_states.append(string0)
		#print(string0)



	#print(dfa)
	#print(new_states)
	#count = 0
	for states in new_states:
		#print(states)
		#print("flag")
		
		string1 = ""
		for char in states:
			#print(char)
			c = int(char)
			if '0' in nfa.dict[c]:
				x = nfa.dict[c]['0']
				#print(nfa.dict[1]['0'])
				for i in x:
					j = str(i)
					if j not in string1:
						string1 += j
						#print(string1)

		#print(string1)
		dfa[states]['0'] = string1
		if string1 not in dfa:
			dfa[string1] = {}
			new_states.append(string1)	

		string2 = ""
		for char in states:
			c = int(char)
			if '1' in nfa.dict[c]:
				#print(nfa.dict[1]['1'])
				x = nfa.dict[c]['1']
				for i in x:
					j = str(i)
					if j not in string2:
						string2 += j

		#print(string2)
		dfa[states]['1'] = string2
		if string2 not in dfa:
			dfa[string2] = {}
			new_states.append(string2)
		

		#if(count==1):
		#	break
		#count+=1

	dfa_as = []
	AS = str(nfa.accepting_state)
	for states in dfa:#check for the accepting state
		for char in states:
			if(char == AS):
				dfa_as.append(states)

	#print(dfa)
#	print(new_states)
	new_states.append(nfa.start_state)
	#print(dfa_as)
	new_dfa = DFA(new_states, nfa.alph, dfa, str(nfa.start_state), dfa_as)
#	print(dfa)
	return new_dfa

#flag = convert_to_DFA(test_nfa)
#print(flag.dict)
'''
{'1': {'0': '12', '1': '1'}, 
'12': {'0': '12', '1': '13'}, 
'13': {'0': '12', '1': '1'}}
'''

#task39

def accepts(dfa, st):
	#print(st)
	#print(dfa.accept_state)
	state = dfa.start_state
	for i in st:
		#print(i)
		state = dfa.dict[state][i]
		#print(state)
	#print(state)
	return state in dfa.accept_state
	'''
	if state == dfa.accept_state:
		return True
	return False
	'''

#print(accepts(flag, "01"))#true
#print(accepts(flag, "11"))#false
#print(accepts(flag, "0101"))#true

k1 = {1:{'0':[2,3]},
      2:{'1':[4]},
      3:{'0':[4]},
      4:{'0':[4]}}
K1 = NFA([1,2,3,4], ['0','1'], k1, 1, 4)

k2 = {1:{'0':[2,3], '1':[1]},
      2:{'0':[2], '1':[3]},
      3:{'0':[4]},
      4:{'0':[4]}}
K2 = NFA([1,2,3,4], ['0','1'], k2, 1, 4)

k3 = {1:{'0':[1], '1':[2]},
      2:{'0':[2], '1':[3]},
      3:{'0':[3]}}
K3 = NFA([1,2,3], ['0','1'], k3, 1, 3)


x1 = convert_to_DFA(K1)
x2 = convert_to_DFA(K2)
x3 = convert_to_DFA(K3)
'''
print(accepts(x1, "01"))#true
print(accepts(x1, "1"))#false
print(accepts(x2, "010"))#true
print(accepts(x2, "111"))#false
print(accepts(x3, "11"))#true
print(accepts(x3, "111"))#false
'''

#task 40

nfa_ex1 = {1:{'0':[1], '1':[2]},
      	   2:{'0':[2,3], '1':[2]},
      	   3:{'0':[3], '1':[2,3]}}
nex1 = NFA([1,2,3], ['0','1'], nfa_ex1, 1, 3)

dfa_ex1 = {'1':{'0':['1'], '1':['2']},
      	   '2':{'0':['23'], '1':['2']},
      	  '23':{'0':['23'], '1':['23']},
      	   '3':{'0':['3'], '1':['2,3']}}
dex1 = DFA([1,2,23,3], ['0','1'], dfa_ex1, 1, 23)

y1 = convert_to_DFA(nex1)
equil(y1.dict, dex1.dict, '1', '1', ['3'], ['23'])

nfa_ex2 = {1:{'0':[1,2], '1':[2]},
      	   2:{'1':[1,2]}}
nex2 = NFA([1,2], ['0','1'], nfa_ex2, 1, 2)

dfa_ex2 = {'1':{'0':'12', '1':'2'},
		  '12':{'0':'12', '1':'12'},
		   '2':{'0':'', '1':'12'},
 		    '':{'0':'', '1':''}}
dex2 = DFA([1,2,12], ['0','1'], dfa_ex2, '1', ['2', '12'])

y2 = convert_to_DFA(nex2)
equil(y2.dict, dex2.dict, '1', '1', ['12', '2', '21'], ['12','2'])

dfa_ex3 = {'1': {'0': '23', '1': ''}, 
			'23': {'0': '4', '1': '4'}, 
			'': {'0': '', '1': ''}, 
			'4': {'0': '4', '1': ''}}
equil(x1.dict, dfa_ex3, '1', '1', ['4'], ['4'])
dfa_ex4 = {'1': {'0': '23', '1': '1'}, 
			'23': {'0': '24', '1': '3'}, 
			'24': {'0': '24', '1': '3'}, 
			'3': {'0': '4', '1': ''}, 
			'4': {'0': '4', '1': ''}, 
			'': {'0': '', '1': ''}}
equil(x2.dict, dfa_ex4, '1', '1', x2.accept_state,['24','4'])
dfa_ex5 = {'1': {'0': '1', '1': '2'}, 
			'2': {'0': '2', '1': '3'}, 
			'3': {'0': '3', '1': ''}, 
			'': {'0': '', '1': ''}}
equil(x3.dict, dfa_ex5, '1', '1', x3.accept_state,['3'])

