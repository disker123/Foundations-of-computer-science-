
#task 33

#union you create a new start state that points to the two nfa on epsilon
def union(nfa_1, nfa_2):
	union_dict = {}#the union dictionary 
	union_dict[0] = {'':[1, 2]}
	union_dict[1] = nfa_1.dict
	union_dict[2] = nfa_2.dict
	#print(union_dict)
	return NFA(nfa_1.states + nfa_2.states, nfa_1.alph, union_dict, {0}, nfa_1.accepting_state + nfa_2.accepting_state)

nfa_u1 = NFA([0, 1, 2], ['0', '1'], example, [0], [2])
nfa_u2 = NFA([0, 1, 2, 3], ['0', '1'], better_example, [0], [3])
x = union(nfa_u1, nfa_u2)
print(x.dict)

'''
{0: {'': [1, 2]}, 
 1: {0: {'0': [0, 1]}, 1: {'0': [0], '1': [2]}, 2: {'1': [1, 2]}},
 2: {0: {'0': [0], '1': [0, 1]}, 1: {'0': [2], '': [2]}, 2: {'1': [3]}, 3: {'0': [3], 1: [3]}}}
'''
