
class regex:
	def __init__(self, language):
		'''self.e = e
		self.empty = empty
		self.char = char
		self.union = union
		self.star = star
		self.concat = concat'''
		self.pattern = re.compile(language)
		return
