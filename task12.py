
def find_accepting(dfa, start, accepting, alph):
	path = ""
	state_list = []
	state = start
	state_list.append(state)
	if state in accepting:
		return path
	while state not in accepting and state_list != list(dfa):
		#first move
		if dfa[state][alph[0]] in state_list:
			state = dfa[state][alph[1]]
			#print("flaging at the first element for adding 1")
			path = path + alph[1]
			state_list.append(state)
		else:
			state = dfa[state][alph[0]]
			#print("flaging at the first element for adding 0")
			path = path + alph[0]
			state_list.append(state)
		
		if state in accepting:
			print(state_list)
			return path
		if(len(state_list) > 10 * len(dfa_num)):
			break


	print(state_list)
	return "failed"



dfa_num = {0:{'0':3, '1':1},
       1:{'0':0, '1':2},
       2:{'0':1, '1':2},
       3:{'0':0, '1':0}}

dfa_al = {0:{'a':3, 'b':1},
      	1:{'a':0, 'b':2},
      	2:{'a':1, 'b':2},
       	3:{'a':0, 'b':0}}

dfa_large = {0:{'0':3, '1':1},
       1:{'0':4, '1':2},
       2:{'0':6, '1':4},
       3:{'0':2, '1':0},
       4:{'0':3, '1':7},
       5:{'0':4, '1':7},
       6:{'0':7, '1':0},
       7:{'0':0, '1':0}}

dfa_large_failure = {0:{'0':3, '1':1},
       1:{'0':5, '1':2},
       2:{'0':6, '1':7},
       3:{'0':2, '1':0},
       4:{'0':3, '1':7},
       5:{'0':3, '1':7},
       6:{'0':7, '1':0},
       7:{'0':0, '1':0}}

print(find_accepting(dfa_num, 0, {2}, ['0', '1']));
print(find_accepting(dfa_al, 0, {2}, ['a', 'b']));
print(find_accepting(dfa_large, 0, {4}, ['0', '1']));
print(find_accepting(dfa_large_failure, 0, {4}, ['0', '1']));

#print(len(dfa_num))
