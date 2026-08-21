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
print(f"Bem vindo {arc.removesuffix(".txt")}")
while True:
    menu("Ver lista de produtos","Cadastrar Produtos","Remover produtos","Trocar de Usuario","Sair do Sistema")
    q = int(input("Digite sua opção:"))

    if q < 1 or q > 5:
        print("Alternativa invalida!, Tente novamente")
        sleep(1)
    else:

        match q:

            case 1:
                sleep(1)
                header("Listagem de Produtos")
                listproducts(arc)

            case 2:
                sleep(1)
                while True:
                    try:
                        header('Cadastro de Produtos')
                        product = str(input("Nome do produto: "))
                        qtde = int(input("Quantidade: "))
                        price = float(input("Preço: ").replace(",","."))
                    except :
                        print("Houve um erro na entrada dos dados!, Tente novamente")
                    else:
                        register(arc,product,qtde,price)
                        cho = input("Voce deseja cadastrar mais produtos?(S/N): ").capitalize().upper()

                        if cho == "S":
                            continue
                        elif cho == "N":
                            break
                        else:
                            print("Entrada invalida!, Tente novamente")
                            sleep(1)
                            cho = input("Voce deseja cadastrar mais produtos?(S/N): ").capitalize().upper()


            case 3:
                sleep(1)
                header('Remover Produto')
                while True:
                    #listProducts(a)
                    #criar condição para quando a lista tiver vazia
                    try:
                    
                        choice = int(input("Remover qual produto da lista? "))
                    except:
                        print("Houve erro na entrada dos dados, tente novamente!")
                        continue
                    else:
                        #if choice > len(listProducts) or choice < 0:
                            #print("Entrada invalida, Tente Novamente!")
                            #continue
                        Q = input("Tem certeza?(S/N) ").capitalize().upper()
                        if Q == "S":
                            #removeProducts(choice)
                            print("Removido com Sucesso!")
                        elif Q == "N":
                            continue
                        else:
                            print("Entrada Invalida!,tente novamente")
                            Q = input("Tem certeza?(S/N) ").capitalize().upper()
                            break

            case 4:
                sleep(1)
                header('Troca de Usuario')
                newuser = input("Usuario: ").upper()
                newarc = f'{newuser}.txt'
                while True:
                    if not userExist(newarc):
                        possUser = input("Usuario não encontrado!, deseja criar um novo usario?(S/N)").upper().capitalize()
                        if possUser == "N":
                            break
                        elif possUser == "S":
                            createUser(newarc)
                            arc = newarc
                            print("USUARIO ENCONTRADO COM SUCESSO!")
                            break
                        else:
                            print("Entrada invalida!, Tente novamente")
                            continue


                    else:
                        arc = newarc
                        print("USUARIO ENCONTRADO COM SUCESSO!")
                        break

            case 5:
                print("Saindo do Sistema...")
                sleep(3)
                header("VOLTE SEMPRE!")
                break
        