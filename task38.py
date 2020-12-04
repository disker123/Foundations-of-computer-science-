
#task 38

nfa = {1:{'0':[1,2], '1':[1]},
       2:{'1':[3]},
       3:{}}

test_nfa = NFA([1,2,3], [0,1], nfa, 1, 3)

def convert_to_DFA(nfa):
	nfa_ss = str(nfa.start_state)
	dfa = {nfa_ss:{}}
	new_states = []
	string0 = ""

	if '0' in nfa.dict[1]:
		x = nfa.dict[1]['0']
		#print(nfa.dict[1]['0'])
		for i in x:
			j = str(i)
			string0 += j
	dfa[nfa_ss]['0'] = string0
	#print(dfa)
	if string0 not in dfa:
		dfa[string0] = {}
		new_states.append(string0)

	string0 = ""
	if '1' in nfa.dict[1]:
		x = nfa.dict[1]['1']
		#print(nfa.dict[1]['0'])
		for i in x:
			j = str(i)
			string0 += j
	dfa[nfa_ss]['1'] = string0
	#print(dfa)
	if string0 not in dfa:
		dfa[string0] = {}
		new_states.append(string0)



	#print(dfa)
	#print(new_states)

	for states in new_states:
		string1 = ""
		for char in states:
			c = int(char)
			if '0' in nfa.dict[c]:
				x = nfa.dict[c]['0']
				#print(nfa.dict[1]['0'])
				for i in x:
					j = str(i)
					string1 += j
			
		#print(string1)
		dfa[states]['0'] = string1
		if string1 not in dfa:
			dfa[string1] = {}
			new_states.append(string1)	

		string2 = ""
		for char in states:
			c = int(char)
			if '1' in nfa.dict[c]:
				#print(nfa.dict[1]['1'])
				x = nfa.dict[c]['1']
				for i in x:
					j = str(i)
					string2 += j

		#print(string2)
		dfa[states]['1'] = string2
		if string2 not in dfa:
			dfa[string2] = {}
			new_states.append(string2)

	dfa_as = 'flag'
	AS = str(nfa.accepting_state)
	for states in dfa:#check for the accepting state
		for char in states:
			if(char == AS):
				dfa_as = states

	#print(dfa)
	new_dfa = DFA(5, nfa.alph, dfa, nfa.start_state, dfa_as)
	return new_dfa

flag = convert_to_DFA(test_nfa)
print(flag.dict)
'''
{'1': {'0': '12', '1': '1'}, 
'12': {'0': '12', '1': '13'}, 
'13': {'0': '12', '1': '1'}}
'''
