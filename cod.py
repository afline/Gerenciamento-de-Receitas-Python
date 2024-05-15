def add (counter):
    #essa função adiciona receitas ao código.
    file = open("receitas.txt", "a")
    try:
        nome = str(input())
        origem = str(input())
        ingredientes = str(input())
        modo = str(input())
    except:
        print("Digite apenas com caractéres.")
    else:
        if nome != "x" or origem != "x" or ingredientes != "x" or modo != "x":
            file.write(f"Receita [{counter}]\n")
            file.write(f"Nome: {nome}\n")
            file.write(f"País de origem: {origem}\n")
            file.write(f"Ingredientes: {ingredientes}\n")
            file.write(f"Modo: {modo}\n")
            file.write(f"\n")
            file.close()

def viz ():
    #essa serve para vizualizar as receitas.
    x

def exc ():
    #essa serve para excluir receitas
    x

def mod ():
    #essa serve para modificar
    print("Digite [N] para modificar o nome, [O] para o país de origem, [I] para ingredientes e [M] para modo.")
    decisao = str(input("Digite aqui: "))
    if decisao == "N":
        c
    elif decisao == "O":
        c
    elif decisao == "I":
        c
    elif decisao == "M":
        c

file = open("receitas.txt", "w")
file.write('')
file.close()
#COUNTER AINDA DEVE SER CONSERTADO!
counter = 1

while True:
    #serve apenas para servir como uma interface pro user decidir o que deseja fazer no programa.
    print("Digite [A] para adicionar receita, [V] para vizualizar, [M] para modificar, [E] para excluir e [Q] para quitar.")
    decisao = str(input("Digite aqui: "))
    print()
    if decisao == "A":
        add(counter)
        counter+=1
    elif decisao == "V":
        viz()
    elif decisao == "M":
        mod()
    elif decisao == "E":
        exc()
    elif decisao == "Q":
        break
