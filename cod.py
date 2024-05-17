def add ():
    #essa função adiciona receitas ao código.
    #funcionando!
    file = open("receitas.txt", "a")
    try:
        nome = str(input("Digite o nome da receita: "))
        origem = str(input("Digite o nome do país de origem da receita: "))
        ingredientes = str(input("Digite os ingredientes: ")) #ainda deve ser concertado, pois está tudo em só uma string.
        modo = str(input("Digite o modo de preparo: "))
    except:
        print("Digite apenas com caractéres.")
    else:
        if nome != "x" or origem != "x" or ingredientes != "x" or modo != "x":
            file.write(f"{nome}\n")
            file.write(f"País de origem: {origem}\n")
            file.write(f"Ingredientes: {ingredientes}\n")
            file.write(f"Modo: {modo}\n")
            file.write(f"\n")
            file.close()
            print()

def viz ():
    #essa serve para vizualizar as receitas.
    #funcionando!
    receita = str(input("Qual receita você deseja vizualizar? "))
    file = open('receitas.txt', 'r')
    lista = file.readlines()
    for i in range (len(lista)):
        if (lista[i]) == (receita + "\n"):
            print()
            print(lista[i])
            print(lista[i + 1])
            print(lista[i + 2])
            print(lista[i + 3])
    file.close()

def exc ():
    #essa serve para excluir receitas
    #AINDA NAO TOTALMENTE FUNCIONAL
    receita = str(input("Qual receita você deseja excluir? "))
    file = open('receitas.txt', 'r')
    lista = file.readlines()
    print(file.read())
    file.close()
    print(lista)
    for i in range (len(lista)):
        if (lista[i]) == (receita + "\n"):
            lista[i] = ''
            lista[i+1] = ''
            lista[i+2] = ''
            lista[i+3] = ''
    print(lista)
    file2 = open('receitas.txt', 'w')
    file2.writelines(lista)
    file2.close()

def mod ():
    #essa serve para modificar
    #AINDA NAO FUNCIONAL
    print("Digite [N] para modificar o nome, [O] para o país de origem, [I] para ingredientes e [M] para modo.")
    decisao = str(input("Digite aqui: "))
    if decisao == "N":
        print()
    elif decisao == "O":
        print()
    elif decisao == "I":
        print()
    elif decisao == "M":
        print()

while True:
    #serve apenas para servir como uma interface pro user decidir o que deseja fazer no programa.
    #me livrei do counter xD
    print("Digite [A] para adicionar receita, [V] para vizualizar, [M] para modificar, [E] para excluir e [Q] para quitar.")
    decisao = str(input("Digite aqui: "))
    print()
    if decisao == "A":
        add()
    elif decisao == "V":
        viz()
    elif decisao == "M":
        mod()
    elif decisao == "E":
        exc()
    elif decisao == "Q":
        break
