
class NFA:
	def __init__(self, xStates, xAlph, xTranaition_func, xStart_state, xAccept_state):
		self.states = xStates
		self.alph = xAlph
		self.dict = xTranaition_func
		self.start_state = xStart_state
		self.accepting_state = xAccept_state
		return


'''
Take 1, tried to create a stack in an itterative function, this was a mistake
def back(nfa, st):
	#print(st)
	trace = []

	#x = tree(nfa, nfa.start_state[0], trace)
	state = nfa.start_state[0]
	retn = False

	#print(state)
	for i in st:
		if i in nfa.dict[state]:#death test
			#print(nfa.dict[state])
			for alpha in nfa.dict[state][i]:
				state = alpha
				temp_nfa = NFA(nfa.states, nfa.alph, nfa.dict, [state], nfa.accepting_state)
				temp_str = st[1:]
				#print(temp_str)
				if(len(temp_str) > 0):
					if(temp_str[0] in temp_nfa.dict[state]):	
						if(back(temp_nfa, temp_str) == True):
							retn = True
		else:
			print("Dead")
			#y = 5
			return "---"
	#print(state)
	#print(state)
	return state in nfa.accepting_state
'''
#take 2 using an actual recursive call that makes a new call of the NFA for each state transition 
#to continue the computation with the reamining string
def back(nfa, state, trace, st):
	if(st == ""):
		return state in nfa.accepting_state
	i = st[0]
	if i in nfa.dict[state]:
		for states in nfa.dict[state][i]:
			if(back(nfa, states, [], st[1:len(st)])):
				return True
	
	epsilon = ""
	if epsilon in nfa.dict[state]:
		print("flag epsilon")
		for states in nfa.dict[state][epsilon]:
			if states not in trace:
				if(back(nfa, states, trace, st)):
					return True
	return False


#task 32

better_example = {0:{'0':[0,1]},
         		  1:{'0':[0], '1':[2]},
         		  2:{'1':[1,2]}}

dfa = {0:{'0':[1]},
       1:{'0':[0], '1':[2]},
       2:{'1':[2]}}

trace_5 = [1, 2, 2, 2, 2, 2, 2] #"0" 
nfa = NFA([1, 2, 3], ['0', '1'], better_example, [0], [2])
trace = []
print(back(nfa, 0, trace, "0111001"))
#for alpha in nfa.dict[0]['0']:
#	print(alpha)

better_example = {0:{'0':[0], '1':[0, 1]},
         		  1:{'0':[2], '':[2]},
         		  2:{'1':[4]},
         		  3:{'0':[4], 1:[4]}}


nfa = NFA([1, 2, 3], ['0', '1', '2', '3'], better_example, [0], [3])
print(back(nfa, 0, trace, "11"))

