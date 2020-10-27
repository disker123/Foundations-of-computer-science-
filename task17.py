def accepts(dfa, start, accepting, st):
	#print(st)
	state = start
	for i in st:
		#print("before state change")
		#print(state)
		#print(i)
		state = dfa[state][i]
		#print("after state change")
		#print(state)
		state = (int(state))
	return state in accepting

def intersect(dfa_1, dfa_2):
	dfa = {}
	for i in range(0, len(dfa_1)):
		for j in range(0, len(dfa_2)):
			#for k in alph:
			#print(i)
			keya = dfa_1[i]['0']
			#print(keya)
			key2a = dfa_2[j]['0']
			#print(key2a)
			key3a = keya + key2a
			#print(key3a)
						
			keyb = dfa_1[i]['1']
			#print(keyb)
			key2b = dfa_2[j]['1']
			#print(key2b)
			key3b = keyb + key2b
			#print(key3b)
			
			x = str(i)
			y = str(j)
			z = x + y
			#print(z)
			
			a = {'0':key3a}
			b = {'1':key3b}
			dfa[z] = (a, b)
			#dfa = {z:{'0':key3a, '1':key3b}}
			#dfa[z]['0'] = key3a
			#dfa[z]['1'] = key3a
			
			#print(dfa)
	return dfa

def accepts_inter(dfa, start, accepting, st):
	state = start
	for i in st:
		if(i == '0'):
			state = dfa[state][(0)]['0']
			#print("flagA")
			#print(state)
			#print("flag1")
		else:
			state = dfa[state][(1)]['1']
			#print("flagB")
			#print(state)
			#print("bla")
	return state in accepting


dfa_1 = {0:{'0':'1', '1':'0'},
       1:{'0':'2', '1':'1'},
       2:{'0':'2', '1':'2'}}

dfa_2 = {0:{'0':'0', '1':'1'},
       1:{'0':'1', '1':'2'},
       2:{'0':'2', '1':'2'}}

dfa_inter = (intersect(dfa_1, dfa_2))
#print(dfa_inter)

'''
{'00': ({'0': '10'}, {'1': '01'}), 
 '01': ({'0': '11'}, {'1': '02'}), 
 '02': ({'0': '12'}, {'1': '02'}), 
 '10': ({'0': '20'}, {'1': '11'}), 
 '11': ({'0': '21'}, {'1': '12'}), 
 '12': ({'0': '22'}, {'1': '12'}), 
 '20': ({'0': '20'}, {'1': '21'}), 
 '21': ({'0': '21'}, {'1': '22'}), 
 '22': ({'0': '22'}, {'1': '22'})}
'''
#task17 intersection test

print("originol DFAs true")
print(accepts(dfa_1, 0, {1}, "01"))
print(accepts(dfa_2, 0, {1}, "01"))
print("originol DFAs false")
print(accepts(dfa_1, 0, {1}, "101"))
print(accepts(dfa_2, 0, {1}, "101"))

print("intersect DFA")
#print(dfa_inter)
print(accepts_inter(dfa_inter, '00', {'11'}, "01"))#true
print(accepts_inter(dfa_inter, '00', {'11'}, "101"))#false




dfa_b1 = {0:{'0':'0', '1':'1'},
       	1:{'0':'2', '1':'0'},
       	2:{'0':'1', '1':'2'}}

dfa_b2 = {0:{'0':'2', '1':'1'},
		1:{'0':'2', '1':'0'},
		2:{'0':'1', '1':'2'}}


print("---originol DFAs true---2")
print(accepts(dfa_b1, 0, {2}, "10"))
print(accepts(dfa_b2, 0, {2}, "10"))
print("originol DFAs false")
print(accepts(dfa_b1, 0, {2}, "01"))
print(accepts(dfa_b2, 0, {2}, "01"))
dfa_inter = (intersect(dfa_b1, dfa_b2))
print("intersect DFA")
#print(dfa_inter)
print(accepts_inter(dfa_inter, '00', {'22'}, "10"))#true
print(accepts_inter(dfa_inter, '00', {'22'}, "01"))#false

dfa_c1 = {0:{'0':'2', '1':'1'},
       	1:{'0':'0', '1':'2'},
       	2:{'0':'1', '1':'1'}}

dfa_c2 = {0:{'0':'0', '1':'2'},
		1:{'0':'0', '1':'0'},
		2:{'0':'1', '1':'2'}}


print("---originol DFAs true---3")
print(accepts(dfa_c1, 0, {0}, "000"))
print(accepts(dfa_c2, 0, {0}, "000"))
print("originol DFAs false")
print(accepts(dfa_c1, 0, {0}, "101"))
print(accepts(dfa_c2, 0, {0}, "101"))
dfa_inter = (intersect(dfa_c1, dfa_c2))
print("intersect DFA")
#print(dfa_inter)
print(accepts_inter(dfa_inter, '00', {'00'}, "000"))#true
print(accepts_inter(dfa_inter, '00', {'00'}, "101"))#false

dfa_d1 = {0:{'0':'0', '1':'2'},
       	1:{'0':'1', '1':'1'},
       	2:{'0':'2', '1':'0'}}

dfa_d2 = {0:{'0':'0', '1':'1'},
		1:{'0':'2', '1':'0'},
		2:{'0':'1', '1':'2'}}


print("---originol DFAs true---4")
print(accepts(dfa_d1, 0, {2}, "10"))
print(accepts(dfa_d2, 0, {2}, "10"))
print("originol DFAs false")
print(accepts(dfa_d1, 0, {2}, "101"))
print(accepts(dfa_d2, 0, {2}, "101"))
dfa_inter = (intersect(dfa_d1, dfa_d2))
print("intersect DFA")
#print(dfa_inter)
print(accepts_inter(dfa_inter, '00', {'22'}, "10"))#true
print(accepts_inter(dfa_inter, '00', {'22'}, "101"))#false

dfa_e1 = {0:{'0':'1', '1':'2'},
       	1:{'0':'1', '1':'0'},
       	2:{'0':'2', '1':'0'}}

dfa_e2 = {0:{'0':'0', '1':'1'},
		1:{'0':'0', '1':'2'},
		2:{'0':'2', '1':'1'}}


print("---originol DFAs true---5")
print(accepts(dfa_e1, 0, {1}, "1100"))
print(accepts(dfa_e2, 0, {2}, "1100"))
print("originol DFAs false")
print(accepts(dfa_e1, 0, {1}, "11"))
print(accepts(dfa_e2, 0, {2}, "11"))
dfa_inter = (intersect(dfa_e1, dfa_e2))
print("intersect DFA")
#print(dfa_inter)
print(accepts_inter(dfa_inter, '00', {'12'}, "1100"))#true
print(accepts_inter(dfa_inter, '00', {'12'}, "101"))#false
