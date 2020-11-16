
class NFA:
	def __init__(self, States, Alph, Tranaition_func, Start_state, Accept_state):
		self.states = States
		self.alph = Alph
		self.tranaition_func = Tranaition_func
		self.start_state = Start_state
		self.accepting_state = Accept_state
