'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
'''
n = input('Informe seu nome ')
s = input('informe sua senha ')
while n == s:
    s = input('Senha não pode ser igual ao nome ')