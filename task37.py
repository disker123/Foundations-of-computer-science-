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

#task36 Kleene star

def kleene_star(nfa):
	nfa.dict[0] = {'': [nfa.start_state]}
	nfa.dict[nfa.accepting_state][''] = [0]
	return nfa

#task 37 Kleene test
k1 = {1:{'0':[2,3]},
      2:{'1':[4]},
      3:{'0':[4]},
      4:{'0':[4]}}

Kleene1 = NFA([1,2,3,4], [0,1], k1, 1, 4)
x1 = kleene_star(Kleene1)
#x1.print_dict()
k2 = {1:{'0':[2,3], '1':[1]},
      2:{'0':[2], '1':[3]},
      3:{'0':[4]},
      4:{'0':[4]}}
Kleene2 = NFA([1,2,3,4], [0,1], k2, 1, 4)
x2 = kleene_star(Kleene2)
#x2.print_dict()
k3 = {1:{'0':[1], '1':[2]},
      2:{'0':[2], '1':[3]},
      3:{'0':[3]}}
Kleene3 = NFA([1,2,3], [0,1], k3, 1, 3)
x3 = kleene_star(Kleene3)
#x3.print_dict()

