'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
nome = input('Informe seu nome utilizando no minimo 3 caracteres ')
while (len(nome) < 3):
    nome = input('Por gentileza informe seu nome utilizando no minimo 3 caracteres ')
idade = int(input('Informe sua idade'))
while idade < 0 or idade > 150:
    idade = int(input('Informe sua idade entre 0 e 150'))
salario = float(input('Informe seu salario'))
while salario <= 0:
    salario = float(input('Informe seu salario'))
sexo = input('Informe (f) para feminino e (m) para masculino')
while sexo != 'f' and sexo != 'm':
    sexo = input('Informe (f) para feminino e (m) para masculino')
ec = input('Informe (s) para Solteiro, (c) para Casado, (v) para Viuvo e (d) para divorciado')
while ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
    ec = input('Informe (s) para Solteiro, (c) para Casado, (v) para Viuvo e (d) para divorciado')