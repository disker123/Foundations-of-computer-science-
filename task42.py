#task41 regular expression

class regex:
	def __init__(self, language):

		self.pattern = re.compile(language)
		return

#task42 regex print

def re_print(reg, string):
	pattern = reg.pattern
	#result = pattern.search(string)
	result = pattern.match(string)
	if result:
		print(result.group())
		return result.group()
	print("none flag")
	return None

# Call our function, passing in our string

min1 = regex(r"0*10*")#contains a one
x = re_print(min1, "00100 james")
many1 = regex(r"^1")#starts with 1
x = re_print(many1, "1010")
many1 = regex(r".1*$")#ends with 1
x = re_print(many1, "011")
many1 = regex(r"^0.1*$")#ends with 1 starts with 0
x = re_print(many1, "011")
