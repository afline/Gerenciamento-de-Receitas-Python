def add ():
    #essa função adiciona receitas ao código.
    #funcionando!
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = str(input("Aqui: "))
        if x == "SAIR":
            break
        print()
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
                file.write(f"Nome: {nome}\n")
                file.write(f"País de origem: {origem}\n")
                file.write(f"Ingredientes: {ingredientes}\n")
                file.write(f"Modo: {modo}\n")
                file.write(f"\n")
                file.close()
                print()
        break

def viz ():
    #essa serve para vizualizar as receitas.
    #funcionando!
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = str(input("Aqui: "))
        if x == "SAIR":
            break
        print()
        receita = str(input("Qual receita você deseja vizualizar? "))
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        for i in range (len(lista)):
            if (lista[i]) == ("Nome: "+ receita + "\n"):
                print()
                print(lista[i])
                print(lista[i + 1])
                print(lista[i + 2])
                print(lista[i + 3])
        file.close()
        break

def exc ():
    #essa serve para excluir receitas
    #funcionando!
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = str(input("Aqui: "))
        if x == "SAIR":
            break
        print()
        receita = str(input("Qual receita você deseja excluir? "))
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        file.close()
        for i in range (len(lista)):
            if (lista[i]) == ("Nome: "+ receita + "\n"):
                lista[i] = ''
                lista[i+1] = ''
                lista[i+2] = ''
                lista[i+3] = ''
                file2 = open('receitas.txt', 'w')
                file2.write('')
                file2.writelines(lista)
                file2.close()
                print("Excluido com sucesso!")
                print()
                break

def mod ():
    #essa serve para modificar
    #AINDA NAO FUNCIONAL
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = str(input("Aqui: "))
        print()
        if x == "SAIR":
            break
        receitaMod = str(input("Qual receita você deseja modificar? "))
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        file.close()
        for i in range (len(lista)):
            if (lista[i]) == (receitaMod + "\n"):
                print(lista)
                print(receitaMod)
                print("Digite [N] para modificar o nome, [P] para o país de origem, [I] para ingredientes e [M] para modo.")
                decisao = str(input("Digite aqui: "))
                print("Digite a nova informação: ")
                novaInfo = str(input("Digite aqui: "))

                if decisao == "N":
                    lista[i] = (f"{novaInfo}\n")
                elif decisao == "P":
                    lista[i+1] = (f"País de origem: {novaInfo}\n")
                elif decisao == "I":
                    lista[i+2] = (f"Ingredientes: {novaInfo}\n")
                elif decisao == "M":
                    lista[i+3] = (f"Modo: {novaInfo}\n")

                print(lista)
                file2 = open('receitas.txt', 'w')
                file2.write('')
                file2.writelines(lista)
                file2.close()
                print("Modificado com sucesso!")
                break

while True:
    #serve apenas para servir como uma interface pro user decidir o que deseja fazer no programa.
    print()
    print("Digite [A] para adicionar receita, [V] para vizualizar, [M] para modificar, [E] para excluir e [Q] para quitar.")
    decisao = input("Digite aqui: ").upper() #independente de digitar a ou A, o programa roda. também planejo fazer isso com as receitas para evitar problemas.
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
    else:
        print("Digite apenas alguma das letras acima!")
