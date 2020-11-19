
#task 30
def fork(tree, state, trace):
	retn = {}
	#print(state)
	for key in tree.dict[state]:#
		#print(key)
		try:
			for alph in tree.dict[state][key]:#
				#print(alph)
				if(alph not in trace):#
					sub_dic = fork(tree, alph, trace +[alph])
					if sub_dic != None:
						#print(sub_dic)
						retn[alph] = sub_dic 
					else:
						retn[alph] = {}
				else:
					retn[state] = "loop"
			#print(tree.dict[state][key])
		except:
			pass
	if(len(retn) == 0):
		#print("none flag")
		return None
	#print("flag")

	return retn





	if(len(retn) == 0):
		print("none flag")
		return None
	#print("flag")
	#print(state,retn)
	return retn


better_example = {1:{'0':[1,2]},
         		  2:{'0':[3], '1':[1]},
         		  3:{'1':[2,3]}}

tree = t_tree(better_example)
trace_5 = [1, 2, 2, 2, 2, 2, 2] #"0" 

trace = []
#state = [1,2,3,4]
#print(fork(tree, 1, trace))


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

#task 31 fork test

better_example = {1:{'0':[1,2]},
         		  2:{'0':[3], '1':[1]},
         		  3:{'1':[2,3]}}

tree = t_tree(better_example)
trace_5 = [1, 2, 2, 2, 2, 2, 2] #"0" 

trace = []
#state = [1,2,3,4]

#print("fork 1:",fork(tree, 1, trace))


dic_1 = {0:{'0':[0,1]},
         1:{'0':[0], '1':[2]},
         2:{'1':[1,2]}}
tree_1 = t_tree(dic_1)
#print("fork 2:",fork(tree_1, 1, trace))

dic_2 = {1:{'0':[1], '1':[1, 2]},
         2:{'0':[3], '1':[3]},
         3:{'0':[4], '1':[4]},
         4:{}}
tree_2 = t_tree(dic_2)
#print("fork 3:",fork(tree_2, 1, trace))

dic_3 = {1:{'0':[1, 2], '1':[1, 3]},
         2:{'0':[4]},
         3:{'1':[4]},
         4:{'0':[4], '1':[4]}}
tree_3 = t_tree(dic_3)
#print("fork 4:",fork(tree_3, 1, trace))

dic_4 = {1:{'0':[1, 2], '1':[1]},
         2:{'0':[2], '1':[2]}}
tree_4 = t_tree(dic_4)
#print("fork 5:",fork(tree_4, 1, trace))

dic_5 = {1:{'0':[1, 2]},
         2:{'0':[1], '1':[3]},
         3:{'1':[2, 3]}}
tree_5 = t_tree(dic_5)
#print("fork 6:",fork(tree_5, 1, trace))
'''
print("fork 1:",fork(tree, 1, trace))
print("fork 2:",fork(tree_1, 1, trace))
print("fork 3:",fork(tree_2, 1, trace))
print("fork 4:",fork(tree_3, 1, trace))
print("fork 5:",fork(tree_4, 1, trace))
print("fork 6:",fork(tree_5, 1, trace))
'''
