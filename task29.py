
class t_tree:
	def __init__(self, xdict):
		self.dict = xdict

#task29 
dic_1 = {1:{'0':['1'], '1':['1', '2']},
         2:{'0':['3'], 'e':['3']},
         3:{'1':['4']},
         4:{'0':['4'], '1':['4']}}
tree_1 = t_tree(dic_1)

dic_2 = {1:{'0':['1'], '1':['1', '2']},
         2:{'0':['3'], '1':['3']},
         3:{'0':['4'], '1':['4']},
         4:{}}
tree_2 = t_tree(dic_2)

dic_3 = {1:{'0':['1', '2'], '1':['1', '3']},
         2:{'0':['4']},
         3:{'1':['4']},
         4:{'0':['4'], '1':['4']}}
tree_3 = t_tree(dic_3)

dic_4 = {1:{'0':['1', '2'], '1':['1']},
         2:{'0':['2'], '1':['2']}}
tree_4 = t_tree(dic_4)

dic_5 = {1:{'0':['1', '2']},
         2:{'0':['1'], '1':['3']},
         3:{'1':['2', '3']}}
tree_5 = t_tree(dic_5)