#!usr/bin/python3
# Exercio de função com multiplos
'__autor__' == '__Ivanoel__'
def multiplos(x,y):
	m = x%y
	if m == 0:
		return True
	else:
		return False
x = int(input("Informe um numero: "))
y = int(input("Informe outro numero: "))
print("mútiplos(%d,%d) =="%(x,y),multiplos(x,y))
