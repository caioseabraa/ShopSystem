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
    

def listproducts(arc):
    try:
        a = open(arc, "rt")
    except:
        print("Erro ao abrir a lista!")
    with a:
        header("LISTA DE PRODUTOS")
        for linha in a:
            if linha.strip() == '':
                continue
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            dado[2] = dado[2].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]:>8}{dado[2]:<12}')


def register(arc,p = "Não informado", q = 0 , price = 0):
    try:
       a = open(arc, "at")
    except:
        print("Houve um erro ao abrir a lista")
    else:
        try:
            a.write(f'{p};{q};{price}\n')
        except:
            print("Erro na escrita dos produtos")
        else:
            print("Produto registrado com sucesso!")
    
