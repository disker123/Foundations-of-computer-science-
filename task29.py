
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


class t_tree:
	def __init__(self, xdict):
		self.dict = xdict




def tree(nfa, state, trace):
	retn = {}
	#print(state)
	for k in nfa.dict[state]:#
		#print(k)
		try:
			for alph in nfa.dict[state][k]:#
				#print(alph)
				if(alph not in trace):#
					value = tree(nfa, alph, trace +[alph])
					if value != None:
						#print(value)
						retn[alph] = value 
					else:
						retn[alph] = {}
				else:
					retn[state] = "loop"
			#print(nfa.dict[state][k])
		except:
			pass
	if(len(retn) == 0):
		print("none flag")
		return None
	#print("flag")

	return retn





	if(len(retn) == 0):
		print("none flag")
		return None
	#print("flag")
	#print(state,retn)
	return retn


better_example = {1:{'0':[1,2,3]},
         		  2:{'0':[3], '1':[1]},
         		  3:{'1':[2,3]}}

trace_5 = [1, 2, 2, 2, 2, 2, 2] #"0" 
nfa = NFA([1, 2], ['0', '1'], better_example, [1], [3])
trace = []
#state = [1,2,3,4]
print(tree(nfa, 1, trace))


'''
state=1
for k in nfa.dict[state]:
	for states in nfa.dict[state][k]:
		print(states)
'''

'''
 {1: {1: 'loop', 2: {3: {3: 'loop'}, 2: 'loop'}},
 2: {3: {3: 'loop'}, 1: {1: 'loop'}}}


 {1: {1: 'loop', 2: {3: {3: 'loop'}, 2: 'loop'}, 3: {2: {2: 'loop'}, 3: 'loop'}}, 
  2: {3: {3: 'loop'}, 1: {1: 'loop', 3: {3: 'loop'}}}, 
  3: {2: {2: 'loop', 1: {1: 'loop'}}, 3: 'loop'}}
'''
