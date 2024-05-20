import random
def add ():
    #essa função adiciona receitas ao código.
    #funcionando!
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        if x == "SAIR":
            break
        print()
        file = open("receitas.txt", "a")
        try:
            nome = str(input("Digite o nome da receita: ")).upper()
            origem = str(input("Digite o nome do país de origem da receita: ")).upper()
            ingredientes = str(input("Digite os ingredientes (Digite os ingredientes separados em vírgulas e espaço.): ")).upper() #ainda deve ser concertado, pois está tudo em só uma string.
            modo = str(input("Digite o modo de preparo: ")).upper()
        except:
            print("Digite apenas com caractéres.")
        else:
            if nome != "x" or origem != "x" or ingredientes != "x" or modo != "x":
                file.write(f"Nome: {nome}\n")
                file.write(f"Pais de origem: {origem}\n")
                file.write(f"Ingredientes: {ingredientes}\n")
                file.write(f"Modo de preparo: {modo}\n")
                file.write(f"\n")
                file.close()
                print()
                print("Adicionado com sucesso!")
                print()
            else:
                print("Não disponível!")
        break

def viz ():
    #essa serve para vizualizar as receitas.
    #funcionando!
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        if x == "SAIR":
            break
        print()
        receita = str(input("Qual receita você deseja vizualizar? ")).upper()
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
    #o lista.pop de vez em quando da index out of range
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        if x == "SAIR":
            break
        print()
        receita = str(input("Qual receita você deseja excluir? ")).upper()
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        file.close()
        for i in range (len(lista)):
            if (lista[i]) == ("Nome: "+ receita + "\n"):
                lista.pop(i)
                lista.pop(i)
                lista.pop(i)
                lista.pop(i)
                file2 = open('receitas.txt', 'w')
                file2.write('')
                file2.writelines(lista)
                file2.close()
                print("Excluido com sucesso!")
                print()
                break
        break

def mod ():
    #essa serve para modificar
    #funcionando na maior parte, mas fica repetindo no loop por algum motivo
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        print()
        if x == "SAIR":
            break
        receitaMod = str(input("Qual receita você deseja modificar? ")).upper()
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        file.close()
        for i in range (len(lista)):
            if (lista[i]) == ("Nome: " + receitaMod + "\n"):
                print()
                print("Digite [N] para modificar o nome, [P] para o país de origem, [I] para ingredientes e [M] para modo.")
                decisao = str(input("Digite aqui: ")).upper()
                print()
                print("Digite a nova informação: ")
                novaInfo = str(input("Digite aqui: ")).upper()

                if decisao == "N":
                    lista[i] = (f"{novaInfo}\n")
                elif decisao == "P":
                    lista[i+1] = (f"Pais de origem: {novaInfo}\n")
                elif decisao == "I":
                    lista[i+2] = (f"Ingredientes: {novaInfo}\n")
                elif decisao == "M":
                    lista[i+3] = (f"Modo de preparo: {novaInfo}\n")
                file2 = open('receitas.txt', 'w')
                file2.write('')
                file2.writelines(lista)
                file2.close()
                print()
                print("Modificado com sucesso!")
                break
        break
              
def aleatorio():
    #defeitos
        # Leitura das linhas e armazena em uma lista
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        listaAlet = []
        for elements in lista:
            if elements.startswith("Nome: "):
                listaAlet.append(elements)
        elemento_aleatorio = random.choice(listaAlet)
        for i in range(len(lista)):
            if elemento_aleatorio == lista[i]:
                print(lista[i])
                print(lista[i+1])
                print(lista[i+2])
                print(lista[i+3])
        file.close()

def fav():
    #ainda nao funcional, favorita mas nâo desfavorita
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        print()
        if x == "SAIR":
            break
        receita = str(input("Qual receita você deseja favoritar/desfavoritar? ")).upper()
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        file.close()
        for i in range(len(lista)):
            if lista[i] == "Nome: " + receita + "\n":
                if '[FAVORITO]' in lista[i]:
                    lista[i] = "Nome: " + receita + "\n"
                    print("Receita desfavoritada!")
                else:
                    lista[i] = "Nome: " + receita + " [FAVORITO]" + "\n"
                    print("Receita favoritada!")
        file = open('receitas.txt', 'w')
        file.write("")
        file.writelines(lista)
        file.close()
        break

def vis_fav():
    # Essa função serve para visualizar as receitas favoritas.
    # funciona!
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        print()
        if x == "SAIR":
            break
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        y = False
        for i in range(len(lista)):
            if lista[i].endswith("[FAVORITO]\n"):
                y = True
                print(lista[i])
                print(lista[i+1])
                print(lista[i+2])
                print(lista[i+3])
                print()
        if y == False:
            print("Nenhuma receita foi favoritada.")
        break


def exc_ing():
    #nao funcionando
    receitas = []
    with open("receitas.txt", "r") as file:
        receitas = file.readlines()

    ingredientes_excluir = str(input("Digite os ingredientes a serem excluídos (separados por vírgula): "))
    ingredientes_excluir = [ing.strip().upper() for ing in ingredientes_excluir.split(", ")]

    with open("receitas.txt", "w") as file:
        skip = False
        receita_menos_ingredientes = []
        for line in receitas:
            if line.startswith("Nome:"):
                if skip:
                    skip = False
                    receita_menos_ingredientes = []
                receita_menos_ingredientes.append(line)
            elif line.startswith("Ingredientes:"):
                for ingrediente in ingredientes_excluir:
                    if ingrediente in line.upper():
                        skip = True
                receita_menos_ingredientes.append(line)
            else:
                receita_menos_ingredientes.append(line)

            if line.strip() == "" and not skip:
                file.receita_writelines(receita_menos_ingredientes)
                receita_menos_ingredientes = []

    print(f"Receitas que continham os ingredientes especificados foram excluídas.")



def filtrar_por_pais():
    #funcionado!!
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        print()
        if x == "SAIR":
            break
        pais = str(input("Digite o país de origem das receitas que você deseja visualizar: ")).upper()
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        counter = False
        print()
        for i in range(len(lista)):
            counter = True
            if lista[i].strip() == f"Pais de origem: {pais.upper()}":
                encontrou = True
                print(lista[i - 1].strip())  # Nome da receita
                print(lista[i].strip())  # País de origem
                print(lista[i + 1].strip())  # Ingredientes
                print(lista[i + 2].strip())  # Modo de preparo
                print()
        if counter == False:
            print(f"Não há receitas cadastradas do país {pais}.\n")
        break

while True:
    #serve apenas para servir como uma interface pro user decidir o que deseja fazer no programa.
    print()
    print("Digite [ADD] para adicionar receita.")
    print("Digite [VIZ] para vizualizar receita")
    print("Digite [MOD] para modificar receita")
    print("Digite [EXC] para excluir receita")
    print("Digite [FAV] para marcar ou desmarcar receita como favorita.")
    print("Digite [VFV] para vizualizar favoritos")
    print("Digite [FPP] para filtrar receitas por país.")
    print("Digite [EXI] para excluir receitas por ingrediente.")
    print("Digite [ALE] para mostrar receita aleatória.")
    print("Digite [QUI] para quitar o programa.")
    print()
    decisao = input("Digite aqui: ").upper()
    print()
    if decisao == "ADD":
        add()
    elif decisao == "VIZ":
        viz()
    elif decisao == "MOD":
        mod()
    elif decisao == "EXC":
        exc()
    elif decisao == "QUI":
        break
    elif decisao == 'VFV':
        vis_fav()
    elif decisao == 'FPP':
        filtrar_por_pais()
    elif decisao == 'EXI':
        exc_ing()
    elif decisao == 'ALE':
        aleatorio()
    elif decisao == 'FAV':
        fav()
    else:
        print("Digite uma decisão válida!")
