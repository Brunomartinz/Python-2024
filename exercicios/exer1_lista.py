"""
Crie uma lista para cada informação a seguir
lista de numeros de 1 a 10
Lista com quatro nomes
Lista com ano que você nasceu """

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['Bruno','Bianca','Murilo']
lista_ano_nascimento = [1997,2024]

#Percorrer a lista de numeros e imprimir na tela:
for numero in lista_de_numeros:
    print(numero)

#Calcular a soma dos numeros impares de 1 a 10
soma_impares = 0
for i in range(1,11,2): # range (1,11) inclui numero de 1 a 10 com um passo de 2 terceiro argumento , isso garante que numeros impares sejam considerados
    soma_impares += i
print(soma_impares)

for i in range(10,0,-1):
    print(i)
