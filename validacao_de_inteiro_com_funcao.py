#!/usr/bin/python3
#'__autor__' == '__Ivanoel__'

'''
Validação de um inteiro usando uma função.

'''

def faixa_int(pergunta, minimo, maximo):
	while True:
		v = int(input(pergunta))
		if v < 0 or v > 10:
			print("Valor Inválido. Digite um valor entre %d e %d"%(minimo,maximo))
		else:
			return v
