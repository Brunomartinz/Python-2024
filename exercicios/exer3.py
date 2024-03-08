#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else
#para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

user = 'admin'
password = '1234'

login_digitado = input('Digite o usuário\n')
senha_digitada = input('Digite a senha\n')

if login_digitado == 'admin' and senha_digitada == '1234':
    print('Acesso liberado , bem vindo a plataforma')
else:
    print('Usuário ou senha incorretos!')