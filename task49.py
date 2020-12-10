
#task48regex equality
def dfa_equality(dfa_1, dfa_2, starta, startb, FSa, FSb, alph):
	#print("---------------")
	if (starta in FSa and startb not in FSb):
		print("FALSE-1")
		return False
	if (starta not in FSa and startb in FSb):
		print("FALSE-1")
		return False
	found_set = set()
	found_set.add("00")
	run_set = set()

	j = set()
	k = set()
	#
	for a in dfa_1:
		if a in dfa_2:
			for keys in alph:
				key1a = dfa_1[a][keys]
				key2a = dfa_2[a][keys]
				key1achar = str(key1a)
				key2achar = str(key2a)
				if(key1achar in FSa and key2achar not in FSb):
					print("FALSE-2")
					return False
				if(key1achar not in FSa and key2achar in FSb):
					print("FALSE-3")
					return False
				if(key1a != key2a):
					j.add(key1a)
					k.add(key2a)
	
	for i in j:
		for a in k:
			for keys in alph:	
				#print(a)
				key1a = dfa_1[i][keys]
				key2a = dfa_2[a][keys]
				if(key1achar in FSa and key2achar not in FSb):
					print("FALSE-6")
					return False
				if(key1achar not in FSa and key2achar in FSb):
					print("FALSE-7")
					return False

	print("TRUE flag")
	#print(found_set)
	return True


def regex_equal(reg_a, reg_b):
	reg_a_nfa = reg_a.convert_to_nfa()
	reg_b_nfa = reg_b.convert_to_nfa()
	reg_a_dfa = convert_to_DFA(reg_a_nfa)
	reg_b_dfa = convert_to_DFA(reg_b_nfa)

	return dfa_equality(reg_a_dfa.dict, reg_b_dfa.dict, reg_a_dfa.start_state, reg_b_dfa.start_state, reg_a_dfa.accept_state, reg_b_dfa.accept_state, ['0', '1','2','3','4','5'])

x = regex_char('5')
y = regex_char('5')
regex_equal(x,y)#true

x = regex_char('0')
y = regex_char('5')
regex_equal(x,y)#false

x = regex_char('3')
y = regex_char('4')
regex_equal(x,y)#false

x = regex_char('2')
y = regex_char('2')
regex_equal(x,y)#true

#--------------------
x = regex_char('5')
y = regex_char('5')
a = regex_concat(x,y)
b = regex_concat(x,y)
regex_equal(a,b)#true
i = regex_char('2')
j = regex_char('3')
#------------------
star1 = regex_star(x)
star2 = regex_star(y)
regex_equal(star1,star2)#true
star3 = regex_star(i)
star4 = regex_star(j)
regex_equal(star3, star4)#false
