carro = int(input('Digite sua velocidade? '))
multa = 5
mu = multa * carro
if carro >= 80:
    print('Você foi multado por dirigir acima do limite em', mu,'reais')
if carro < 80:
    print('Pode ir adiante meu rapaz! ')
