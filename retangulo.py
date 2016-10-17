#!/usr/bin/python3
#'__autor__' == '__Ivanoel__'
#Funçaõ retângulo com parâmetro obrigatorios e opcionais.

def retangulo(largura, altura, carac= '*'):
	linha = carac * largura

	for i in range(altura):
		print(linha)

#retangulo(3,4)

#retangulo(largura = 3 , altura = 10)
retangulo(carac ='-' , altura = 10, largura = 3)
