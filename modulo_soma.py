from modulo_entrada import valida_inteiro
L=[]
for x in range(10):
	L.append(valida_inteiro("Digite um número:",0,20))
print("Soma: %d"%(sum(L)))