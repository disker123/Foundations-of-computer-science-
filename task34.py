
#task 34 concat incomplete

def concat(nfa_1, nfa_2):
	nfa_1.dict[nfa_1.accepting_state][''] = nfa_2.dict
	new_nfa = NFA(nfa_1.states, nfa_1.alph, nfa_1.dict, [nfa_1.start_state], [nfa_2.accepting_state])
	return new_nfa
