'__autor__' == '__Ivanoel__'
print(' ## Calculadora ## \n')
A = int(input("Informe um  número? "))
B = int(input("Informe o segundo número? "))
print("Qual operação você deseja realiza?\nsoma, subtrair, multiplica, divisão e 0 para sair: ")
opcao = str(input(""))

if (opcao == 'soma'):
    soma = A + B
    print(' A soma é: ',soma)
elif(opcao == 'subtrair'):
    sub = A - B
    print(' A subtração é: ',sub)
elif (opcao == 'multiplica'):
    multi = A * B
    print(' A multiplicação é: ',multi)
elif(opcao == 'divisão'):
    divisão = A / B
    print(' A divisão é: ',divisão)
elif opcao == 0:
    break
else:
    print('Opção inválida!!!')
