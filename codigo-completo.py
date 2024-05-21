import random

def add ():
    #Função que adiciona receitas ao txt.
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        if x == "SAIR":
            break
        print()
        file = open("receitas.txt", "a")
        nome = str(input("Digite o nome da receita: ")).upper()
        origem = str(input("Digite o nome do país de origem da receita: ")).upper()
        ingredientes = str(input("Digite os ingredientes (Digite os ingredientes separados em vírgulas e espaço.): ")).upper() #ainda deve ser concertado, pois está tudo em só uma string.
        modo = str(input("Digite o modo de preparo: ")).upper()
        print("Digite apenas com caractéres.")
        file.write(f"Nome: {nome}\n")
        file.write(f"Pais de origem: {origem}\n")
        file.write(f"Ingredientes: {ingredientes}\n")
        file.write(f"Modo de preparo: {modo}\n")
        file.write(f"\n")
        file.close()
        print()
        print("Adicionado com sucesso!")
        break

def viz ():
    #Função que vizualiza receitas do txt.
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        if x == "SAIR":
            break
        print()
        receita = str(input("Qual receita você deseja vizualizar? ")).upper()
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        y = False
        for i in range (len(lista)):
            if (lista[i]) == ("Nome: "+ receita + "\n") or lista[i] == ("Nome: "+ receita + " [FAVORITO]\n"):
                y = True
                print()
                print(lista[i])
                print(lista[i + 1])
                print(lista[i + 2])
                print(lista[i + 3])
        file.close()
        if y == False:
            print("Essa receita não está cadastrada.")
        break

def exc ():
    #Função que exclui receitas do txt.
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
        y = False
        for i in range (len(lista)):
            if (lista[i]) == ("Nome: "+ receita + "\n") or lista[i] == ("Nome: "+ receita + " [FAVORITO]\n"):
                y =  True
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
        if y == False:
            print("Essa receita não está cadastrada.")
        break

def mod ():
    #Função que modifica receitas do txt.
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
        y = False
        for i in range (len(lista)):
            if (lista[i]) == ("Nome: "+ receitaMod + "\n") or lista[i] == ("Nome: "+ receitaMod + " [FAVORITO]\n"):
                y = True
                print()
                print("Digite [N] para modificar o nome, [P] para o país de origem, [I] para ingredientes e [M] para modo.")
                decisao = str(input("Digite aqui: ")).upper()
                print()
                print("Digite a nova informação: ")
                novaInfo = str(input("Digite aqui: ")).upper()

                if decisao == "N":
                    if ("[FAVORITO]") in lista[i]:
                        lista[i] = (f"Nome: {novaInfo} [FAVORITO]\n")
                    else:
                        lista[i] = (f"Nome: {novaInfo}\n")
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
        if y == False:
            print("Essa receita não está cadastrada.")
        break
              
def aleatorio():
    #Função que printa receita aleatoria do txt
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        print()
        if x == "SAIR":
            break
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        listaAlet = []
        y = False
        for elements in lista:
            if elements.startswith("Nome: "):
                listaAlet.append(elements)
        elemento_aleatorio = random.choice(listaAlet)
        for i in range(len(lista)):
            if elemento_aleatorio == lista[i]:
                y = True
                print(lista[i])
                print(lista[i+1])
                print(lista[i+2])
                print(lista[i+3])
        file.close()
        if y == False:
            print("Sem receitas cadastradas.")
        break

def fav():
    #Função favorita ou desfavorita receita
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
        y = False
        for i in range(len(lista)):
            if lista[i].startswith("Nome:") and receita in lista[i]:
                y = True
                if "[FAVORITO]" in lista[i]:
                    lista[i] = lista[i].replace("[FAVORITO]", "").strip() + "\n"
                    print()
                    print("Receita desfavoritada!")
                    print()
                else:
                    lista[i] = lista[i].strip() + " [FAVORITO]\n"
                    print()
                    print("Receita favoritada!")
                    print()
        file = open('receitas.txt', 'w')
        file.write("")
        file.writelines(lista)
        file.close()
        if y == False:
            print("Essa receita não está cadastrada.")
        break

def vis_fav():
    #Função que serve para visualizar as receitas favoritas.
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
    #Função que exclui receitas de um ingrediente específico
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        print()
        if x == "SAIR":
            break
        ingrediente = str(input("Digite o ingrediente que você deseja tirar as receitas que o contenha: ")).upper()
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        file.close()
        y = False
        for i, linha in enumerate(lista):
            if 'Ingredientes:' in linha:
                if ingrediente in linha:
                    y = True
                    lista.pop(i-2)
                    lista.pop(i-2)
                    lista.pop(i-2)
                    lista.pop(i-2)
                    file2 = open('receitas.txt', 'w')
                    file2.write('')
                    file2.writelines(lista)
                    file2.close()
                    print()
        if y == False:
            print("Essa ingrediente não está em nenhuma receita.")
        else:
            print("Excluido com sucesso!")
        print()
        break

def filtrar_por_pais():
    #Função que printa receitas filtradas por país
    while True:
        print("Digite [SAIR] se desejar voltar para a tela inicial e cancelar a ação. Digite qualquer outra coisa para continuar.")
        x = input("Digite aqui: ").upper()
        print()
        if x == "SAIR":
            break
        pais = str(input("Digite o país de origem das receitas que você deseja visualizar: ")).upper()
        file = open('receitas.txt', 'r')
        lista = file.readlines()
        y = False
        print()
        for i in range(len(lista)):
            if lista[i].strip() == f"Pais de origem: {pais.upper()}":
                y = True
                print(lista[i - 1].strip())  # Nome da receita
                print(lista[i].strip())  # País de origem
                print(lista[i + 1].strip())  # Ingredientes
                print(lista[i + 2].strip())  # Modo de preparo
                print()
        if y == False:
            print(f"Não há receitas cadastradas do país {pais}.\n")
        file.close()
        break

while True:
    #Interface pro user decidir o que deseja fazer no programa.
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
