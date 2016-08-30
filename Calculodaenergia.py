#!/usr/bin/python3
'__autor__'=='__Ivanoel__'

print('## Calculo para energia elétrica ##\n')

consumo = float(input("Informe a quantidade de KWH consumido?\n "))
print("Que tipo de Instalação  Elétrica é?\nR para Residencial; I para Industrial; C para Comercios?")
opcao = str(input("Qual foi sua opção? \n"))

if( opcao == 'R' and consumo < 500):
    paga = 0.40
  #  print('Você pagará de energia residencial? ',(paga * consumo))
else:
    paga = 0.65
  #  print('Você pagará de energia rsidencial? ',(paga * consumo ))

    if( opcao == 'I' and consumo < 1000):
        paga = 0.55
    #    print('Você pagará de energia Industrial? ',(paga * consumo))
    else:
        paga = 0.65
     #   print('Você pagará de energia Idustrial? ',(paga * consumo))


        if( opcao == 'C' and consumo < 5000):
            
            paga = 0.55
            
     #       print('Você pagará de energia Comercial? ',(paga * consumo))
        else:
            paga = 0.60
      #      print('Você pagará de energia Comercial? ',(paga * consumo))
            
print('Você pagará no consumo de energia R$%6.2f' %(paga*consumo))
