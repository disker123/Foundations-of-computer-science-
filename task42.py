
class regex:
	def __init__(self, char=None, epsilon=None, empty=None, union=None, star=None, circ=None):
		if char != None:
			self.char = char
			self.state = 0
		elif(epsilon != None):
			self.epsilon = epsilon
			self.state = 1
		elif(empty != None):
			self.empty = empty
			self.state = 2
		elif(union != None):
			self.union = union
			self.state = 3
		elif(star != None):
			self.star = star
			self.state = 4
		elif(circ != None):
			self.circ = circ
			self.state = 5

#task 42
	def printer(self):
		if self.state == 0:
			return self.char#return an established chacrackter nfa 
		if self.state == 1:
			#print("epsilon")
			return "epsilon"#epsilon is an established nfa 
		if self.state == 2:
			#print("empty")
			return "empty"#and empty nfa is an established nfa 
		if self.state == 3:
			return f"({self.char[0].printer()}) | ({self.char[1].printer()})"# take the union of all the nfas so far in the tree
		if self.state == 4:
			return f"({self.star.printer()})*"#useing the kleen star function all the nfas in the tree 
		if self.state == 5:
			return f"({self.circ[0].printer()})({self.circ[1].printer()})"
