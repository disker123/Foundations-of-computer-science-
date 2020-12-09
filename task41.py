
#task41 regular expression

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
