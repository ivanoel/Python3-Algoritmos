# Cálculo de média com acumulador #
# Ivanoel Rodrigo #
# Exercico do livro de python3 Cap. 5 #


x = 1
soma = 0
while x <= 3:
    n = int(input("%d Digite o numero: "%x))
    soma = soma + n
    x = x + 1
print("Média: %5.2f"  % (soma*0.3))
