
produto=int(input("Informe a categoria do produto? "))

if produto == 1:
    preco = 10
else:
    if produto == 2:
        preco = 18
    else:
        if produto == 3:
            preco = 23
        else:
            if produto == 4:
                preco = 26
            else:
                if produto == 5:
                    preco  = 31
                else:
                    print('O produto inválido, digite um valor entre 1 a 5!')
                    preco = 0
print('O preço do produto é: R$6.2f' % (produto,preco))
