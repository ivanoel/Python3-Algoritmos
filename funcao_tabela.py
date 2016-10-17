def soma (a,b):
	return a + b

def subtracao (a,b):
	return a - b

def multi (a,b):
	return a * b

def divisao (a,b):
	return a / b	

def imprime(a,b, foper):
	print(foper(a,b)) # passamos os parâmetros a e b para função foper que ainda não reconheceu.


imprime(5,4, soma) # chamamos a função imprime, passando a função soma como parâmetro.
imprime(5,4, subtracao)#chamamos a função imprime, mas dessa vez passando a função subtração como foper.
imprime(5,4, multi)
imprime(50,5, divisao)	
#print(soma(4,3))
#print(subtracao(4,3))
#print(multi(4,3))
#print(divisao(40,4))
