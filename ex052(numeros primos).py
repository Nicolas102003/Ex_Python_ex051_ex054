num = int(input('digite um número:'))
tot = 0
for c in range(1,num + 1):
    if num % c ==0:
        print('\033[34m',end=' ')
        tot += 1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
if tot == 2:
    print('\n O número {} foi divisível apenas duas vezes\n Sendo assim ele é primo'.format(num))
else:
    print('\n O número {} foi divisível mais de duas vezes\n Sendo assim ele não primo é primo'.format(num))
