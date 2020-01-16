print('='*5 ,'P A', '='*5)
pn = int(input('Digite o primeiro numero da PA:'))
r = int(input('Digite a razão da PA:'))
dec = pn +(10 - 1)* r
for c in range(pn,dec + r ,r):
    print(c, end=' ')

