divisores = 0
numero = int(input('Digite o numero\n'))
for i in range(1,numero+1):
    if(numero%i==0):
        divisores = divisores + 1
if(divisores == 2):
    print(f'Seu numero   é primo\n')
else:
    print(f'Seu numero nao é primo\n')