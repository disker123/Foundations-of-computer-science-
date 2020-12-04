
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
		'''if(states == ''):
			print("flag")
			dfa['']['0'] = ''
			dfa['']['1'] = ''
			continue'''

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
	#print(new_states)
	new_states.append(nfa.start_state)
	new_dfa = DFA(new_states, nfa.alph, dfa, str(nfa.start_state), dfa_as)
	return new_dfa

flag = convert_to_DFA(test_nfa)
#print(flag.dict)
'''
{'1': {'0': '12', '1': '1'}, 
'12': {'0': '12', '1': '13'}, 
'13': {'0': '12', '1': '1'}}
'''

#task39

def accepts(dfa, st):
	#print(st)
	#print(dfa.accept_state)
	state = dfa.start_state
	for i in st:
		#print(i)
		state = dfa.dict[state][i]
		#print(state)
	#print(state)
	if state == dfa.accept_state:
		return True
	return False

#print(accepts(flag, "01"))#true
#print(accepts(flag, "11"))#false
#print(accepts(flag, "0101"))#true

k1 = {1:{'0':[2,3]},
      2:{'1':[4]},
      3:{'0':[4]},
      4:{'0':[4]}}
K1 = NFA([1,2,3,4], ['0','1'], k1, 1, 4)

k2 = {1:{'0':[2,3], '1':[1]},
      2:{'0':[2], '1':[3]},
      3:{'0':[4]},
      4:{'0':[4]}}
K2 = NFA([1,2,3,4], ['0','1'], k2, 1, 4)

k3 = {1:{'0':[1], '1':[2]},
      2:{'0':[2], '1':[3]},
      3:{'0':[3]}}
K3 = NFA([1,2,3], ['0','1'], k3, 1, 3)

x1 = convert_to_DFA(K1)
x2 = convert_to_DFA(K2)
x3 = convert_to_DFA(K3)
print(x3.dict)
print(accepts(x1, "01"))#true
print(accepts(x1, "1"))#false
print(accepts(x2, "010"))#true
print(accepts(x2, "111"))#false
print(accepts(x3, "11"))#true
print(accepts(x3, "111"))#false
