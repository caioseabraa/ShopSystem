from lib.archive import *
from lib.interface import *
from time import sleep



user = input("Usuario: ").upper()
arc = f'{user}.txt'
if not userExist(arc):
    createUser(arc)
else:
    print("USUARIO ENCONTRADO COM SUCESSO!")

print('Carregando Sistema....')
sleep(2)
print("Bem vindo!!")
while True:
    menu("Ver lista de produtos","Cadastrar Produtos","Remover produtos","Trocar de Usuario","Sair do Sistema")
    q = int(input("Digite sua opção:"))

    if q == 1:
        header("opção 1")

    elif q == 2:
        header('opção 2')
    elif q == 3:
        header('opção 3')
    elif q == 4:
        header('opção 4')
    elif q == 5:
        print("Saindo do Sistema...")
        sleep(3)
        header("VOLTE SEMPRE!")
        break