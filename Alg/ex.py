par = 0
impar = 0
for i in range(1,2022101):
    if(i%2==0):
        par = par + 1
    else:
        impar = impar + 1
print(f'A quantidade de pares é {par} e a quantidade de impares é {impar}')