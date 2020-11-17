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

#task 23

class NFA:
	def __init__(self, xStates, xAlph, xTranaition_func, xStart_state, xAccept_state):
		self.states = xStates
		self.alph = xAlph
		self.dict = xTranaition_func
		self.start_state = xStart_state
		self.accepting_state = xAccept_state
		return
#task 24
def dfa_to_nfa(DFA):
	transfer = {}
	for a in DFA.dict:
		temp = {}
		for b in DFA.dict[a]:
			temp[b] = [DFA.dict[a][b]]
		transfer[a] = temp	
	x = NFA(DFA.states, DFA.alph, transfer, DFA.start_state, DFA.accept_state)
	return x

#x = DFA({0, 1, 2}, ['0', '1'], dic_1, {0}, {1})
#y = dfa_to_nfa(x)

#task 25

dic_1 = {1:{'0':{'1'}, '1':{'1', '2'}},
         2:{'0':{'3'}, 'epsilon':{'1'}},
         3:{'0':'2', '1':'2'},
         4:{'0':'4', '1':'4'}}
nfa_1 = NFA({1, 2, 3, 4}, ['0', '1'], dic_1, {1}, {4})

dic_2 = {1:{'0':{'1'}, '1':{'1', '2'}},
         2:{'0':{'3'}, '1':{'3'}},
         3:{'0':{'2'}, '1':{'2'}},
         4:{'0':{'4'}, '1':{'4'}}}
nfa_2 = NFA({1, 2, 3, 4}, ['0', '1'], dic_2, {1}, {4})

dic_3 = {1:{'0':{'1', '2'}, '1':{'1', '3'}},
         2:{'0':{'4'}},
         3:{'1':{'4'}},
         4:{'0':{'4'}, '1':{'4'}}}
nfa_3 = NFA({1, 2, 3, 4}, ['0', '1'], dic_3, {1}, {4})
dic_4 = {1:{'0':{'1'}, '1':{'1', '2'}},
         2:{'0':{'2'}, '1':{'2'}}}
nfa_4 = NFA({1, 2}, ['0', '1'], dic_4, {1}, {2})
dic_5 = {1:{'0':{'1', '2'}},
         2:{'0':{'1'}, '1':{'3'}},
         3:{'1':{'2', '3'}}}
nfa_5 = NFA({1, 2, 3}, ['0', '1'], dic_5, {1}, {1})
