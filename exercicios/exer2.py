#2 - Pergunte ao usuário sua idade e, com base nisso, 
#use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

idade = int(input ='qual a sua idade ?\n')
if idade <= 12:
    print('Classificado como Criança')
elif idade > 12:
    print('Classificado como Adoslescente')
else:
    print('Classificado como adulto')
    