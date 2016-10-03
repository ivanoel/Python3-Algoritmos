while 1:
	def epar(x):
		return(x%2==0)
	def par_ou_impar(x):
		if epar(x):
			return "Par"
		else:
			return "Impar"
	p = int(input("Digite um numero ou 00 para sair: "))
	if p == 00:
		break
	print(par_ou_impar(p))
	#print(par_ou_impar(5))
