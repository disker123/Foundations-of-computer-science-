#task43 some example REs
'''
r"z{3,}" // a string with 3 or more z in a row
r"hello world" // a string contains hello world
r"pick[234]" // as tring containg pick 2, pick 3, pick 4
r"\d" // a string containing a single digit 
r"ni+ce" // a string that says nice with at least 1 i(preferably more though)
"[^asdfghjkl;']" // any charackter that's not on the middle row of a keyboard (between Lshift and enter)

test = regex(r"[^asdfghjkl;']")#ends with 1 and starts with 0
x = re_print(test, "'")
'''
