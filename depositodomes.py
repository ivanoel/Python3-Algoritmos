deposito = 0
mes = 1
while mes <= 12:
    m = int(input('Digite o seu deposito do %d mês? '%mes))
    deposito = deposito + m
    mes = mes + 1
print("O total de ganho com juros é de R$%5.2f "%(deposito))
