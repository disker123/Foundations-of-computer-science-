#task11

def trace(dfa, start, accepting, st, ):
	tracelist = [start]
	state = start
	for i in st:
		state = dfa[state][i]
		tracelist.append(state);
	print(tracelist)
	return state in accepting

trace(dfa_even, 0, {0}, "00111000")
trace(dfa_abst, 0, {1}, "0010001")
trace(dfa_traffic_light, 0, {0}, "00001110000" )

