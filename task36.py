
#task36 Kleene star

def kleene_star(nfa):
	nfa.dict[0] = {'': [nfa.start_state]}
	nfa.dict[nfa.accepting_state] = {'': [0]}
	return nfa
