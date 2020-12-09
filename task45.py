import re
import rstr

class regex:
	def __init__(self, language):
		self.raw = language
		self.pattern = re.compile(language)
		return

#task45 generate a accepting string of a regex

def generator(reg):
	return rstr.xeger(reg.pattern)
test1 = regex(r"z{3,}")
test2 = regex(r"hello world")
test3 = regex(r"pick [234]")
test4 = regex(r"\d")
test5 = regex(r"ni+ce")
test6 = regex(r"[^asdfghjkl;']")

print(generator(test1))
print(generator(test2))
print(generator(test3))
print(generator(test4))
print(generator(test5))
print(generator(test6))
