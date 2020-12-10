for a in dfa_1:
		if a in dfa_2:
#			print(a)
			key1a = dfa_1[a]['0']
			key2a = dfa_2[a]['0']
	#		print(key1a)
	#		print(key2a)
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
				#j.add(int(key1a))
				#k.add(int(key2a))
				j.add(key1a[0])
				k.add(key2a[0])

			key1b = dfa_1[a]['1']
			key2b = dfa_2[a]['1']
	#		print(key1b)
	#		print(key2b)
			key1bchar = str(key1b)
			key2bchar = str(key2b)

			if(key1bchar in FSa and key2bchar not in FSb):
				print("FALSE-4")
				return False 
			if(key1bchar not in FSa and key2bchar in FSb):
				print("FALSE-5")
				return False
			if(key1b != key2b):
				#j.add(int(key1b))
				#k.add(int(key2a))
				j.add(key1b[0])
				k.add(key2a[0])

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
