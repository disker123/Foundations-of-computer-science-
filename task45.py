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

def union(nfa_1, nfa_2):
	union_dict = {}#the union dictionary 
	union_dict['0'] = {'':['1', '2']}
	union_dict['1'] = nfa_1.dict
	union_dict['2'] = nfa_2.dict
	#print(union_dict)
	return NFA(nfa_1.states + nfa_2.states, nfa_1.alph, union_dict, '0', nfa_1.accepting_state + nfa_2.accepting_state)

def concat(nfa_1, nfa_2):
	print(nfa_1.dict)
	nfa_1.dict[nfa_1.accepting_state][''] = nfa_2.dict
	new_nfa = NFA(nfa_1.states, nfa_1.alph, nfa_1.dict, nfa_1.start_state, [nfa_2.accepting_state])
	return new_nfa

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

def kleene_star(nfa):
	nfa.dict[0] = {'': [nfa.start_state]}
	#print(nfa.accepting_state)
	for states in nfa.accepting_state: 
		nfa.dict[states][''] = [0]
	return nfa

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

class regex_epsilon(regex):
	def __init__(self):
		pass

	def compile(self):
		nfa = {'1':{}}
		for i in language:
			nfa['1'][i] = ['2']#create a transition form the accepting state to the dead state
		nfa['2'] = {}

		return NFA(['1','2'], language, nfa, '1', ['1'])

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


class regex_union(regex):
	def __init__(self, reg_a, reg_b):
		self.a = reg_a
		self.b = reg_b

	def compile(self):
		return union(self.a.compile(), self.b.compile())


class regex_star(regex):
	def __init__(self, reg_a):
		self.a = reg_a

	def compile(self):
		return kleene_star(self.a.compile())#runs the kleen star operation which creates an epsilon transition from the accepting states of the nfa to the starting state

class regex_concat(regex):
	def __init__(self, reg_a, reg_b):
		self.a = reg_a
		self.b = reg_b

	def compile(self):
		return reg_concat(self.a.compile(), self.b.compile())
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









def convert_to_DFA_forreg(nfa):
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
			if(char == AS):
				dfa_as.append(states)

	#print(dfa)
#	print(new_states)
	new_states.append(nfa.start_state)
	#print(dfa_as)
	new_dfa = DFA(new_states, nfa.alph, dfa, str(nfa.start_state), dfa_as)
#	print(dfa)
	return new_dfa










x = regex_char('3')
char = x.compile()
dfa = convert_to_DFA_forreg(char)
print(generator(dfa.dict, '1', ['2'], ['0', '1','2','3','4','5']))


