'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.'''
t = 1
x = []
media = 0
i = 0
while t != -0:
    t = float(input('Informe a temperatura ou digite "0" para sair'))
    if t != 0:
        x.append(t)
        media += t
        i +=1

print(f'A media das temperaturas é {sum(x)/ i},\nA maior temperatura é: {max(x)}\n A menor temperatura é: {min(x)} ')





