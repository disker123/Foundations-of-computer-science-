def union(nfa_1, nfa_2):
	union_dict = {}#the union dictionary 
	union_dict[0] = {'':[1, 2]}
	union_dict[1] = nfa_1.dict
	union_dict[2] = nfa_2.dict
	#print(union_dict)
	return NFA(nfa_1.states + nfa_2.states, nfa_1.alph, union_dict, {0}, nfa_1.accepting_state + nfa_2.accepting_state)

def concat(nfa_1, nfa_2):
	print(nfa_1.dict)
	nfa_1.dict[nfa_1.accepting_state][''] = nfa_2.dict
	new_nfa = NFA(nfa_1.states, nfa_1.alph, nfa_1.dict, [nfa_1.start_state], [nfa_2.accepting_state])
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
	new_nfa = NFA(nfa_1.states, nfa_1.alph, nfa_1.dict, [nfa_1.start_state], [nfa_2.accepting_state])
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


language = "abcdefg"#hijklmnopqrstuvwxyz
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



#task 43 regex examples 

empty = regex_empty()
empty_nfa = empty.compile()
print(empty_nfa.dict)

eps = regex_epsilon()
eps_nfa = eps.compile()
print(eps_nfa.dict)

x = regex_char('d')
char = x.compile()
print(char.dict)

x = regex_char('d')
y = regex_char('a')
union = regex_union(x,y)
print(union.compile())

a = regex_char('a')
star = regex_star(a)
kle = star.compile()
print(kle.dict)

b = regex_char('b')
c = regex_char('c')
circ = regex_concat(b,c)
con = circ.compile()
print(con.dict)
