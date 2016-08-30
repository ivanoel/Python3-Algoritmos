##                                                ##
##                Salario do Funcionário          ##
##                                                ##
##                                                ##






salario = float(input('Qual é o seu salario? '))
base = salario
aumento = 0
if base > 1250:
    aumento = aumento + ((base + 1250)* 10)
    base = 1250
if base > 2000:
    aumento = aumento+((base + 2000)* 15)
print('Seu salario R$%6.2f aumentou para R$%6.2f  ' % (salario,aumento))
