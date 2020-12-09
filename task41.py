
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
empty = regex_empty()
empty_nfa = empty.compile()
#print(empty_nfa.dict)

class regex_epsilon(regex):
	def __init__(self):
		pass

	def compile(self):
		nfa = {'1':{}}
		for i in language:
			nfa['1'][i] = ['2']#create a transition form the accepting state to the dead state
		nfa['2'] = {}

		return NFA(['1','2'], language, nfa, '1', ['1'])
eps = regex_epsilon()
eps_nfa = eps.compile()
#print(eps_nfa.dict)

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


x = regex_char('d')
char = x.compile()
#print(char.dict)

class regex_union(regex):
	def __init__(self, reg_a, reg_b):
		self.a = reg_a
		self.b = reg_b

	def compile(self):
		return union(self.a.compile(), self.b.compile())

x = regex_char('d')
y = regex_char('a')
union = regex_union(x,y)
#print(union.compile())

class regex_star(regex):
	def __init__(self, reg_a):
		self.a = reg_a

	def compile(self):
		return kleene_star(self.a.compile())#runs the kleen star operation which creates an epsilon transition from the accepting states of the nfa to the starting state

a = regex_char('a')
star = regex_star(a)
kle = star.compile()
#print(kle.dict)
class regex_concat(regex):
	def __init__(self, reg_a, reg_b):
		self.a = reg_a
		self.b = reg_b

	def compile(self):
		return reg_concat(self.a.compile(), self.b.compile())

b = regex_char('b')
c = regex_char('c')
circ = regex_concat(b,c)
con = circ.compile()
#print(con.dict)
