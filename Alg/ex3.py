COR = 0
PAL = 0
SANT = 0
SP = 0 
OUTRO = 0
total = 0
resposta = 'sim'
while(resposta == 'sim'):
    time = input('Qual time vc torce: Corinthians, Palmeiras, Santos, São Paulo ou outro?\n')
    if(time == 'Corinthians'):
        COR = COR + 1
    elif(time == 'Palmeiras'):
        PAL = PAL + 1
    elif(time == 'Santos'):
        SANT = SANT + 1
    elif(time == 'São Paulo'):
        SP = SP + 1
    else:
        OUTRO = OUTRO + 1
    total = total + 1
    resposta = input('Deseja continuar?\n')
mediaCOR = COR/(total*100)
mediaPAL = PAL/(total*100)
mediaSANT = SANT/(total*100)
mediaSP = SP/(total*100)
mediaOUTRO = OUTRO/(total*100)
print(f'A % de cada time é: Corinthians = {mediaCOR}, Palmeiras = {mediaPAL}, Santos = {mediaSANT}, São Paulo = {mediaSP} e outros times = {mediaOUTRO}\n')