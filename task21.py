def equil(dfa_1, dfa_2, starta, startb, FSa, FSb):
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
	for a in range(0, len(dfa_1)):
		key1a = dfa_1[a]['0']
		key2a = dfa_2[a]['0']
		key1achar = str(key1a)
		#print(key1achar)
		key2achar = str(key2a)
		#print(key2achar)
		if(key1achar in FSa and key2achar not in FSb):
			print("FALSE-2")
			return False
		if(key1achar not in FSa and key2achar in FSb):
			print("FALSE-3")
			return False
		if(key1a != key2a):
			j.add(int(key1a))
			k.add(int(key2a))

		key1b = dfa_1[a]['1']
		key2b = dfa_2[a]['1']
		key1bchar = str(key1b)
		key2bchar = str(key2b)

		if(key1bchar in FSa and key2bchar not in FSb):
			print("FALSE-4")
			return False 
		if(key1bchar not in FSa and key2bchar in FSb):
			print("FALSE-5")
			return False
		if(key1b != key2b):
			j.add(int(key1b))
			k.add(int(key2a))

	for i in j:
		for a in k:
			#print(a)
			key1a = dfa_1[i]['0']
			key2a = dfa_2[a]['0']
			if(key1achar in FSa and key2achar not in FSb):
				print("FALSE-6")
				return False
			if(key1achar not in FSa and key2achar in FSb):
				print("FALSE-7")
				return False

			key1a = dfa_1[i]['1']
			key2a = dfa_2[a]['1']
			if(key1bchar in FSa and key2bchar not in FSb):
				print("FALSE-8")
				return False
			if(key1bchar not in FSa and key2bchar in FSb):
				print("FALSE-9")
				return False

	

	print("TRUE flag")
	#print(found_set)
	return True


def equil_inter_union(dfa_1, dfa_2, starta, startb, FSa, FSb):
	print("---------------")
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
	for a in range(0,int(math.sqrt(len(dfa_1)))):
		for b in range(0,int(math.sqrt(len(dfa_1)))):
			index = str(a) + str(b)
			#print(index)
			#index = int(index)
			key1a = dfa_1[index]['0']
			key2a = dfa_2[index]['0']
			key1achar = str(key1a)
			#print(key1achar)
			key2achar = str(key2a)
			#print(key2achar)
			if(key1achar in FSa and key2achar not in FSb):
				print("FALSE-2")
				return False
			if(key1achar not in FSa and key2achar in FSb):
				print("FALSE-3")
				return False
			if(key1a != key2a):
				j.add(int(key1a))
				k.add(int(key2a))

			key1b = dfa_1[index]['1']
			key2b = dfa_2[index]['1']
			key1bchar = str(key1b)
			key2bchar = str(key2b)

			if(key1bchar in FSa and key2bchar not in FSb):
				print("FALSE-4")
				return False 
			if(key1bchar not in FSa and key2bchar in FSb):
				print("FALSE-5")
				return False
			if(key1b != key2b):
				j.add(int(key1b))
				k.add(int(key2a))

	for i in j:
		for a in k:
			#print(a)
			key1a = dfa_1[i]['0']
			key2a = dfa_2[a]['0']
			if(key1achar in FSa and key2achar not in FSb):
				print("FALSE-6")
				return False
			if(key1achar not in FSa and key2achar in FSb):
				print("FALSE-7")
				return False

			key1a = dfa_1[i]['1']
			key2a = dfa_2[a]['1']
			if(key1bchar in FSa and key2bchar not in FSb):
				print("FALSE-8")
				return False
			if(key1bchar not in FSa and key2bchar in FSb):
				print("FALSE-9")
				return False


	print("TRUE flag")
	#print(found_set)
	return True
  
  dfa_q = {0:{'0':'0', '1':'1'},
         1:{'0':'2', '1':'1'},
         2:{'0':'1', '1':'2'}}
#SS:0, fs:0

dfa_r = {0:{'0':'0', '1':'1'},
         1:{'0':'2', '1':'1'},
         2:{'0':'3', '1':'2'},
         3:{'0':'2', '1':'0'}}
#SS:0, fs:0


dfa_a = {0:{'0':'0', '1':'1'},
         1:{'0':'2', '1':'0'},
         2:{'0':'1', '1':'2'}}
#SS:0, fs:0

dfa_b = {0:{'0':'0', '1':'1'},
         1:{'0':'3', '1':'2'},
         2:{'0':'3', '1':'2'},
         3:{'0':'0', '1':'1'}}
#SS:0, fs:0
dfa_three = {0:{'0':0, '1':2},
       		1:{'0':2, '1':0},
       		2:{'0':1, '1':2}}
#SS:0, fs:0

'''
equil(dfa_q, dfa_r, "0", "0", {'0'}, {'0'})#true
equil(dfa_q, dfa_r, "0", "1", {'0'}, {'1'})#false
equil(dfa_a, dfa_b, "0", "0", {'0'}, {'0'})#false
equil(dfa_even, dfa_even_binary_number, "0", "0", {'0'}, {'0'})#false
equil(dfa_odd_binary_number, dfa_abst, "0", "0", {'0'}, {'0'})#false
equil(dfa_three_states, dfa_three, "0", "0", {'0'}, {'0'})#true
equil(dfa_three_states, dfa_three, "1", "1", {'1'}, {'1'})#false
'''


'''
dfa_three_states = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}
'''
