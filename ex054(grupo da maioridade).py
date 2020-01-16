from datetime import date
print('='*5,'M A I O R I D A D E','='*5 )
maior = 0
menor = 0
aa = date.today().year
for c in range(1,8):
    an = int(input('Em que ano você nasceu:'))
    res = aa - an
    if res >= 21:
       maior += 1
    else:
        menor += 1
print(' Ao todo tivemos {} pessoas maiores de idade\n E tivemos {} pessoas menores de idade'.format(maior,menor))
