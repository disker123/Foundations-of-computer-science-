class NFA:
	def __init__(self, xStates, xAlph, xTranaition_func, xStart_state, xAccept_state):
		self.states = xStates
		self.alph = xAlph
		self.dict = xTranaition_func
		self.start_state = xStart_state
		self.accepting_state = xAccept_state
		return
    
    
#task 27


def oracle(nfa, trace, string, accept):
	state = nfa.start_state[0]
	count = 1
	#string = "00011"
	for i in string:
		#print(state)
		if(i in nfa.dict[state]):
			print(state)
			#print("flag")
			state = nfa.dict[trace[count]][i]
			#print(state)
			state = int(state[0])
			#print(state)
			count+= 1
		#print("after state change")
		#print(state)
		#state = (int(state))
	if(accept):
		print("good")
		return state in nfa.accepting_state
	if(not accept):
		print("bad")
		return state not in nfa.accepting_state





dic_oracle = {1:{'0':['2']},
         2:{'0':['2'], '1':['2']}}
trace_5 = [1, 2, 2, 2, 2, 2, 2] #"0" 
nfa = NFA([1, 2], ['0', '1'], dic_oracle, [1], [2])

oracle(nfa, trace_5, "001010", True)

