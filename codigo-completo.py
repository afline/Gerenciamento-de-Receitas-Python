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
            ingredientes = str(input("Digite os ingredientes: ")).upper() #ainda deve ser concertado, pois está tudo em só uma string.
            modo = str(input("Digite o modo de preparo: ")).upper()
        except:
            print("Digite apenas com caractéres.")
        else:
            if nome != "x" or origem != "x" or ingredientes != "x" or modo != "x":
                file.write(f"Nome: {nome}\n")
                file.write(f"País de origem: {origem}\n")
                file.write(f"Ingredientes (Digite os ingredientes separados em vírgulas e espaço.): {ingredientes}\n")
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
                lista.pop(i+1)
                lista.pop(i+2)
                lista.pop(i+3)
                file2 = open('receitas.txt', 'w')
                file2.write('')
                file2.writelines(lista)
                file2.close()
                print("Excluido com sucesso!")
                print()
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
                print(lista)
                print("Nome: " + receitaMod + "\n")
                print("Digite [N] para modificar o nome, [P] para o país de origem, [I] para ingredientes e [M] para modo.")
                decisao = str(input("Digite aqui: ")).upper()
                print("Digite a nova informação: ")
                novaInfo = str(input("Digite aqui: ")).upper()

                if decisao == "N":
                    lista[i] = (f"{novaInfo}\n")
                elif decisao == "P":
                    lista[i+1] = (f"País de origem: {novaInfo}\n")
                elif decisao == "I":
                    lista[i+2] = (f"Ingredientes (Digite os ingredientes separados em vírgulas e espaço.): {novaInfo}\n")
                elif decisao == "M":
                    lista[i+3] = (f"Modo de preparo: {novaInfo}\n")

                print(lista)
                file2 = open('receitas.txt', 'w')
                file2.write('')
                file2.writelines(lista)
                file2.close()
                print("Modificado com sucesso!")
                break
              
def aleatorio():
    with open('receitas.txt', 'r') as receitas:
        # Leitura das linhas e armazena em uma lista
        conteudo=receitas.read()
        conteudo_lista=[conteudo]
        elemento_aleatorio = random.choice(conteudo_lista)

        # Exibe o elemento escolhido aleatoriamente
        print(elemento_aleatorio)

def fav():
    # essa serve para marcar/desmarcar favoritas
    receitas = []
    with open("receitas.txt", "r") as file:
        receitas = file.readlines()

    nome = str(input("Digite o nome da receita a ser marcada/desmarcada como favorita: "))
    updated_receitas = []
    skip = False
    for line in receitas:
        if line.strip() == nome:
            skip = True
        if skip and line.startswith("Favorito:"):
            favorito_status = "sim" if "não" in line else "não"
            line = f"Favorito: {favorito_status}\n"
        updated_receitas.append(line)
        if not line.strip():
            skip = False

    with open("receitas.txt", "w") as file:
        for line in updated_receitas:
            file.write(line)
    print("Status de favorito atualizado com sucesso!")

def vis_fav():
    # Essa função serve para visualizar as receitas favoritas.
    try:
        file = open("receitas.txt", "r")
        linhas = file.readlines()
        favorito = False
        for linha in linhas:
            if "Favorito: sim" in linha:
                favorito = True
                print("\n".join(linhas[linhas.index(linha)-4:linhas.index(linha)+1]))
                print()
        if not favorito:
            print("Nenhuma receita favorita encontrada.")
        file.close()
    except FileNotFoundError:
        print("Nenhuma receita cadastrada.")

def exc_ing():
    # essa serve para excluir receitas que contenham certos ingredientes.
    receitas = []
    with open("receitas.txt", "r") as file:
        receitas = file.readlines()

    ingredientes_excluir = str(input("Digite os ingredientes a serem excluídos (separados por vírgula): "))
    ingredientes_excluir = [ing.strip().lower() for ing in ingredientes_excluir.split(", ")]
    
    with open("receitas.txt", "w") as file:
        skip = False
        for line in receitas:
            if line.startswith("Ingredientes:"):
                for ingrediente in ingredientes_excluir:
                    if ingrediente in line.lower():
                        skip = True
            if line.startswith("Receita") or line.strip() == "":
                skip = False
            if not skip:
                file.write(line)
    print(f"Receitas que continham os ingredientes especificados, sendo ele(s) {ingredientes_excluir} foram excluídas.")

file = open("receitas.txt", "w")
file.write('')
file.close()


def filtrar_por_pais():
    pais = str(input("Digite o país de origem das receitas que você deseja visualizar: "))
    with open('receitas.txt', 'r') as file:
        lista = file.readlines()
        encontrou = False
        for i in range(len(lista)):
            if lista[i].strip() == f"País de origem: {pais}":
                encontrou = True
                print(lista[i - 1].strip())  # Nome da receita
                print(lista[i].strip())  # País de origem
                print(lista[i + 1].strip())  # Ingredientes
                print(lista[i + 2].strip())  # Modo de preparo
                print()
        if not encontrou:
            print(f"Não há receitas cadastradas do país {pais}.\n")

while True:
    #serve apenas para servir como uma interface pro user decidir o que deseja fazer no programa.
    print()
    print("Digite [A] para adicionar receita, [V] para vizualizar, [M] para modificar, [E] para excluir e [Q] para quitar.")
    decisao = input("Digite aqui: ").upper()
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
