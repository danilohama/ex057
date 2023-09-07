"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os "M" ou "F" caso esteja errado peça a digitação
novamente até ter o valor correto"""
sexo = str(input('Qual seu sexo? [M/F] = ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[0;31mDados Invalidos\033[31;0m. Por favor tente novamente, informe seu sexo: '
                     )).strip().upper()[0]
print('Sexo\033[0;32m {}\033[32;0m Registrado com sucesso'.format(sexo))
