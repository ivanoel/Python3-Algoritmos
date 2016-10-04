def soma(L):
	total=0
	for x in range(5):
		total+=L[x]
	return total
L = [1,7,2,9,15]
print(soma(L))
print(soma([7,9,12,3,100,8,9,6]))