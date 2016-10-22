'''
def soma(a,b,c,d,e):
	s = a+b+c+d+e
L=[1,2,3,4,5]
soma(*L)
'''
def barra(n=10,c='*'):
	print(c*n)
L = [[5,'-'],[10,'*'],[5],[6,'-']]
for e in L:
	barra(*e)