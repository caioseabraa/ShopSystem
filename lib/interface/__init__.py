def header(msg):
    print('-'*40)
    print(f'{msg}'.center(40))
    print('-'*40)


def menu(*lista):
    header("SHOP SYSTEM v1.0")
    
    for i in range(len(lista)):
        print(f'{i+1} - {lista[i]}')