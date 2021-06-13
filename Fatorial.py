'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''
f = int(input('Informe um numero para ser calculado o seu fatorial '))
fa = 1
count = f
for i in range(f, 0, -1):
    fa = fa * i
    print(count, end=" * ")
    count -= 1
print("1 = ", fa)

