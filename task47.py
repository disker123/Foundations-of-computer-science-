import math

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


def union(nfa_1, nfa_2):
	union_dict = {}#the union dictionary 
	union_dict['0'] = {'':['1', '2']}
	union_dict['1'] = nfa_1.dict
	union_dict['2'] = nfa_2.dict
	#print(union_dict)
	return NFA(nfa_1.states + nfa_2.states, nfa_1.alph, union_dict, '0', nfa_1.accepting_state + nfa_2.accepting_state)


def reg_concat(nfa_1, nfa_2):
	for state in nfa_1.accepting_state:
		nfa_1.dict[state][''] = 'b'+nfa_2.start_state
	for state in nfa_2.dict:
		new_state = 'b'+ state
		keys = nfa_2.dict[state]
		nfa_1.dict[new_state] = {}
		for key in keys:
			new_key = 'b'+ keys[key][0]
			nfa_1.dict[new_state][key] = new_key	
	count = 0
	for state in nfa_2.accepting_state:
		nfa_2.accepting_state[count] = 'b' + nfa_2.accepting_state[count]
		count += 1
	new_nfa = NFA(nfa_1.states, nfa_1.alph, nfa_1.dict, nfa_1.start_state, [nfa_2.accepting_state])
	return new_nfa

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

	def __repr__(self):
		return { 'start state: ':self.start_state, 'accepting state: ':self.accepting_state, 'transition functions: ':self.dict}

	def print_dict(self):
		print(self.dict)
		return

#task36 Kleene star

def kleene_star(nfa):
	nfa.dict[0] = {'': [nfa.start_state]}
	#print(nfa.accepting_state)
	for states in nfa.accepting_state: 
		nfa.dict[states][''] = [0]
	return nfa

#task 38


def convert_to_DFA(nfa):
	nfa_ss = str(nfa.start_state)
	dfa = {nfa_ss:{}}
	new_states = []
	string0 = ""
	for key in nfa.alph:
		string0 = ""
		if key in nfa.dict[nfa_ss]:
			x = nfa.dict[nfa_ss][key]
			#print(nfa.dict[1]['0'])
			for i in x:
				j = str(i)
				string0 += j
		dfa[nfa_ss][key] = string0
		#print(dfa)
		if string0 not in dfa:
			dfa[string0] = {}
			new_states.append(string0)
			#print(string0)


	for states in new_states:
		#print(states)
		#print("flag")
		for key in nfa.alph:
			string1 = ""
			for char in states:
				#print(char)
				c = char
				if key in nfa.dict[c]:
					x = nfa.dict[c][key]
					#print(nfa.dict[1]['0'])
					for i in x:
						j = str(i)
						if j not in string1:
							string1 += j
							#print(string1)

			#print(string1)
			dfa[states][key] = string1
			if string1 not in dfa:
				dfa[string1] = {}
				new_states.append(string1)	


	dfa_as = []
	AS = str(nfa.accepting_state)
	for states in dfa:#check for the accepting state
		for char in states:
			if(char in nfa.accepting_state):
				dfa_as.append(states)
#	print(new_states)
	new_states.append(nfa.start_state)
	new_dfa = DFA(new_states, nfa.alph, dfa, str(nfa.start_state), dfa_as)
	return new_dfa

nfa = {'1':{'0':['1','2'], '1':['1']},
       '2':{'1':['3']},
       '3':{}}

test_nfa = NFA(['1','2','3'], ['0','1'], nfa, '1', ['3'])
flag = convert_to_DFA(test_nfa)
#print(flag.dict)

'''
{'1': {'0': '12', '1': '1'}, 
'12': {'0': '12', '1': '13'}, 
'13': {'0': '12', '1': '1'}}
'''

#task39

def accepts(dfa, st):
	state = dfa.start_state
	for i in st:
		state = dfa.dict[state][i]
	return state in dfa.accept_state


'''
print(accepts(flag, "01"))#true
print(accepts(flag, "11"))#false
print(accepts(flag, "0101"))#true
'''

#task41 regular expression

language = "012345"#hijklmnopqrstuvwxyz
class regex:
	def compile(self):#when inheriting form subclasses make sure they all can compile a regex
		pass

class regex_empty(regex):
	def __init__(self):
		pass

	def compile(self):
		dic = {'1': {}}		
		return NFA(['1'], language, dic, '1', [])

	def convert_to_nfa(self):
		return self.compile()


class regex_epsilon(regex):
	def __init__(self):
		pass

	def compile(self):
		nfa = {'1':{}}
		for i in language:
			nfa['1'][i] = ['2']#create a transition form the accepting state to the dead state
		nfa['2'] = {}

		return NFA(['1','2'], language, nfa, '1', ['1'])

	def convert_to_nfa(self):
		return self.compile()

class regex_char(regex):
	def __init__(self, char):
		self.char = char

	def compile(self):
		nfa = {}
		nfa['1'] = {self.char:'2'}
		nfa['2'] = {}
		for i in language:
			if i != self.char:
				nfa['2'][i] = ['3']#create a transition form the accepting state to the dead state
		nfa['3'] = {}
		return NFA(['1','2','3'], language, nfa, '1', ['2'])

	def convert_to_nfa(self):
		return self.compile()


class regex_union(regex):
	def __init__(self, reg_a, reg_b):
		self.a = reg_a
		self.b = reg_b

	def compile(self):
		return union(self.a.compile(), self.b.compile())

	def convert_to_nfa(self):
		return self.compile()


class regex_star(regex):
	def __init__(self, reg_a):
		self.a = reg_a

	def compile(self):
		return kleene_star(self.a.compile())#runs the kleen star operation which creates an epsilon transition from the accepting states of the nfa to the starting state
	def convert_to_nfa(self):
		return self.compile()


class regex_concat(regex):
	def __init__(self, reg_a, reg_b):
		self.a = reg_a
		self.b = reg_b

	def compile(self):
		return reg_concat(self.a.compile(), self.b.compile())

	def convert_to_nfa(self):
		return self.compile()



#task45 generator for random accepted string

def generator(dfa, start, accepting, alph):
	path = ""
	state_list = ['']
	state = start
	state_list.append(state)
	if state in accepting:
		return path	
	while state not in accepting and state_list != list(dfa):
		#first move
		for key in alph:
			if dfa[state][key] not in state_list:
				state = dfa[state][key]
				#print("flaging at the first element for adding 1")
				path = path + key
				state_list.append(state)
			'''
			else:
				state = dfa[state][alph[0]]
				#print("flaging at the first element for adding 0")
				path = path + alph[0] + ""
				state_list.append(state)
			'''
			if state in accepting:
				#print(state_list)
				return path
			if(len(state_list) > pow(len(dfa), 2)):
				print("failed")
				return


	#print(state_list)
	print("failed")
	return


#task 47

empty = regex_empty()
x = empty.convert_to_nfa()
x = convert_to_DFA(x)
ex1 = {'1': {}}
ex_nfa1 = NFA(['1'], ['0', '1','2','3','4','5'], ex1, '1', []) 
ex1_dfa = convert_to_DFA(ex_nfa1)
equil(x.dict, ex1_dfa.dict, x.start_state, ex1_dfa.start_state, x.accept_state, ex1_dfa.accept_state)

x = regex_char('2')
y = regex_char('3')
z = regex_concat(x,y)
circ_nfa = z.convert_to_nfa()

circ_dfa = convert_to_DFA(circ_nfa)
ex2 = {'1': {'2': '2'}, 
	   '2': {'0': ['3'], '1': ['3'], '3': ['3'], '4': ['3'], '5': ['3'], '': 'b1'}, 
	   '3': {}, 
	   'b1': {'3': 'b2'}, 
	   'b2': {'0': 'b3', '1': 'b3', '2': 'b3', '4': 'b3', '5': 'b3'}, 
	   'b3': {}}

ex_nfa2 = NFA(['1', '2', '3', 'b1', 'b2', 'b3'], ['0', '1','2','3','4','5'], ex1, '1', []) 
ex2_dfa = convert_to_DFA(ex_nfa2)
equil(circ_dfa.dict, ex2_dfa.dict, circ_dfa.start_state, ex2_dfa.start_state, circ_dfa.accept_state, ex2_dfa.accept_state)
