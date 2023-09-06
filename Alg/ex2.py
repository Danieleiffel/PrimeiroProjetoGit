pessoas = 0
idades = 0
resposta = 'sim'
while(resposta == 'sim'):
    nome = input('Digite seu nome\n')
    idade = int(input('Digite sua idade\n'))
    idades = idade + idades
    pessoas = pessoas +1
    resposta = input('Deseja continuar?\n')
calculo = idades/pessoas
print(f'A média da idade é igual à {calculo}')