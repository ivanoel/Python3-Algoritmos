#!/usr/bin/python3
#'__autor__'=='__Ivanoel__'
'''
Valição sem usar uma função

'''

while True:
	v = int(input("digite um valor entre 0 a 5:"))
	if v < 0 or v > 5:
		print("Valor Inválido")
	else:
		break		
