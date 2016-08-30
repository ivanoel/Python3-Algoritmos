materia =int(input('Digite a quantidade de nota que você quer das Avaliações? '))
i = 0
soma = 0
while i < materia:
    ap1 = int(input('Digite suas notas das avaliações[%d]: ' % (i+1)))
    soma = soma + ap1 
    i += 1;
media = soma / materia
print("A média é? %.1f "% media)
