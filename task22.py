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


artificial_comp = {0:{'0':3, '1':1},
       	   1:{'0':0, '1':2},
       	   2:{'0':1, '1':2},
       	   3:{'0':0, '1':0}}

FS = comp_dfa(dfa_num, {'0'})
equil(dfa_num, artificial_comp, "0", "0", {'0'}, FS)#false


dfa_true_intersect = {'00': {'0': '10', '1': '01'}, 
 					  '01': {'0': '11', '1': '02'}, 
 					  '02': {'0': '12', '1': '02'}, 
 					  '10': {'0': '20', '1': '11'}, 
 					  '11': {'0': '21', '1': '12'}, 
  					  '12': {'0': '22', '1': '12'}, 
  					  '20': {'0': '20', '1': '21'}, 
 					  '21': {'0': '21', '1': '22'}, 
 					  '22': {'0': '22', '1': '22'}}
#SS:0, FS:11

dfa_true_union =   {'00': {'0': '10', '1': '01'}, 
					'01': {'0': '11', '1': '02'}, 
					'02': {'0': '12', '1': '02'}, 
					'10': {'0': '20', '1': '11'}, 
					'11': {'0': '21', '1': '12'}, 
					'12': {'0': '22', '1': '12'}, 
					'20': {'0': '20', '1': '21'}, 
					'21': {'0': '21', '1': '22'}, 
					'22': {'0': '22', '1': '22'}}
#SS:00, FS:01, 11, 21, 10, 12

dfa_1 = {0:{'0':'1', '1':'0'},
       1:{'0':'2', '1':'1'},
       2:{'0':'2', '1':'2'}}
#SS:0, FS:1

dfa_2 = {0:{'0':'0', '1':'1'},
       1:{'0':'1', '1':'2'},
       2:{'0':'2', '1':'2'}}
#SS:0, FS:1

dfa_inter = (intersect(dfa_1, dfa_2))
dfa_union = (intersect(dfa_1, dfa_2))
print(dfa_union)
equil_inter_union(dfa_inter, dfa_true_intersect, "00", "00", {'11'}, {'11'})
equil_inter_union(dfa_union, dfa_true_intersect, "00", "00", {'01', '11', '21', '10', '12'}, {'01', '11', '21', '10', '12'})
