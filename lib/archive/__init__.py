from lib.interface import *


def userExist(archive):
    try:
        a = open(archive,"rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def createUser(archive):
    header("CRIAÇÃO DE USUARIO")
    archive = f'{archive}'.removesuffix('.txt')
    qUser = input(f"Quer se registrar como {archive}?(S/N):  ").upper().capitalize()
    
    if qUser == 'S':
        newUser = archive
        res = verifyUser(newUser)
    elif qUser == 'N':
         newUser = input("novo nome de usuario: ").upper()
         newUser += '.txt'
         res = verifyUser(newUser)

    while True:
        if res is False:
            newUser = input("novo nome de usuario: ").upper()
            newUser += '.txt'
            res = verifyUser(newUser)
        else:
            a = open(newUser,"wt+")
            a.close()
            print(f"Arquivo {newUser} criado com sucesso!")
            break





def verifyUser(archive):
    try:
        a = open(archive,"rt")
        a.close()
    except FileNotFoundError:
        return True
    else:
        print("Ja existe um usuario com esse nome!, tente novamente.")
        return False
    