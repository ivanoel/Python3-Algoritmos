##                                       ##
##         O maior e Menor Número        ##
##                                       ##
##                                       ##

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número tbm: '))
if a < b and a < c:
    print('Esse número é o menor==> ',a)
if a > b and a > c:
    print('Esse é Maior==>',a)
if b > a and b > c:
    print('Esse é o Maior==> ', b)
if b < a and b < c:
    print('Esse é o Menor==>',b)
if c > b and c > a:
    print('Esse é o Maior==>', c)
if c < b and c < a:
    print('Esse é o Menor==>',c )
