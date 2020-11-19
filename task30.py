
class t_tree:
	def __init__(self, xdict):
		self.dict = xdict

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
