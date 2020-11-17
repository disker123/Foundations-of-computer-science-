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

#task 24
	def __init__(self, DFA):
		transfer = {}
		for a in DFA.dict:
			temp = {}
			for b in DFA.dict[a]:
				temp[b] = [DFA.dict[a][b]]
			transfer[a] = temp
		self.dict = transfer
		self.states = DFA.states
		self.alph = DFA.alph
		#self.tranaition_func = {state:{Key_at_state:[value] for Key_at_state}}
		self.start_state = DFA.start_state
		self.accepting_state = DFA.accept_state
		return
