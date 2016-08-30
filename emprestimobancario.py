casa = float(input('Digite o valor da casa à comprar? '))
salario = float(input('Informe seu salario? '))
ano = float(input('Em quantos anos a paga a casa? '))
mensal = casa / salario
if ano < 30:
    print('Seu emprestimo não foi aprovado!, está em torno de R$%6.2f'%mensal,'reais por mês')
else:
    print('Você foi aprovado para o emprestimo, você pagará mensalmente R$%6.2f'%mensal)
    
    
