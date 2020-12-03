#task 34 concat incomplete

def concat(nfa_1, nfa_2):
	nfa_1.dict[nfa_1.accepting_state][''] = nfa_2.dict
	new_nfa = NFA(nfa_1.states, nfa_1.alph, nfa_1.dict, [nfa_1.start_state], [nfa_2.accepting_state])
	return new_nfa

#task35 test concat
C1 = {1:{'0':[2,3]},
      2:{'1':[4]},
      3:{'0':[4]},
      4:{'0':[4]}}

C2 = {1:{'0':[2,3], '1':[1]},
      2:{'0':[2], '1':[3]},
      3:{'0':[4]},
      4:{'0':[4]}}

C3 = {1:{'0':[1], '1':[2]},
      2:{'0':[2], '1':[3]},
      3:{'0':[3]}}

C4 = {1:{'1':[2]},
      2:{'1':[3]},
      3:{'1':[3]}}

Co1 = NFA([1,2,3,4], [0,1], C1, 1, 4)
Co2 = NFA([1,2,3,4], [0,1], C2, 1, 4)
Co3 = NFA([1,2,3], [0,1], C3, 1, 3)
Co4 = NFA([1,2,3], [0,1], C3, 1, 3)

Coa = concat(Co1, Co2)
Cob = concat(Co1, Co3)
Coc = concat(Co1, Co4)
Cod = concat(Co2, Co3)
Coe = concat(Co2, Co4)
Cof = concat(Co3, Co4)


Coa.print_dict()
Cob.print_dict()
Coc.print_dict()
Cod.print_dict()
Coe.print_dict()
Cof.print_dict()
