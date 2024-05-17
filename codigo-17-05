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

def vis ():
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

#def exc diferente do de vinicius
def exc():
    # essa serve para excluir receitas
    # possivelmente solucao para funcionar
    receita = str(input("Qual receita você deseja excluir? "))
    file = open('receitas.txt', 'r')
    lista = file.readlines()
    file.close()
    
    nova_lista = []
    skip = False
    for i in range(len(lista)):
        if lista[i].strip() == receita:
            skip = True
        if not skip:
            nova_lista.append(lista[i])
        if skip and lista[i].strip() == "":
            skip = False
    
    file2 = open('receitas.txt', 'w')
    file2.writelines(nova_lista)
    file2.close()
    print("Receita excluída com sucesso!")

#def mod diferente do de vinicius
def mod():
    # essa serve para modificar
    # possivelmente solucao para funcionar
    receitas = []
    with open("receitas.txt", "r") as file:
        receitas = file.readlines()

    nome = str(input("Nome da receita a ser modificada: "))
    updated_receitas = []
    skip = False
    for line in receitas:
        if line.strip() == nome:
            skip = True
            print("Digite [N] para modificar o nome, [O] para o país de origem, [I] para ingredientes e [M] para modo.")
            decisao = str(input("Digite aqui: "))
            if decisao == "N":
                line = f"{str(input('Novo nome: '))}\n"
            elif decisao == "O":
                next_line = f"País de origem: {str(input('Novo país de origem: '))}\n"
                updated_receitas.append(line)
                line = next_line
            elif decisao == "I":
                next_line = f"Ingredientes: {str(input('Novos ingredientes: '))}\n"
                updated_receitas.append(line)
                line = next_line
            elif decisao == "M":
                next_line = f"Modo de preparo: {str(input('Novo modo de preparo: '))}\n"
                updated_receitas.append(line)
                line = next_line
        updated_receitas.append(line)
        if not line.strip():
            skip = False

    with open("receitas.txt", "w") as file:
        for line in updated_receitas:
            file.write(line)
    print("Receita modificada com sucesso!")

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
    ingredientes_excluir = [ing.strip().lower() for ing in ingredientes_excluir.split(",")]
    
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
    print(f"Receitas que continham os ingredientes especificados, sendo eles {ingredientes_excluir} foram excluídas.")

file = open("receitas.txt", "w")
file.write('')
file.close()

while True:
    # interface pro user decidir o que deseja fazer no programa.
    print("Digite [A] para adicionar receita, [V] para visualizar, [M] para modificar, [E] para excluir, [F] para marcar/desmarcar favorita, [L] para visualizar favoritas, [X] para excluir por ingrediente e [Q] para quitar.")
    decisao = str(input("Digite aqui: "))
    print()
    if decisao == "A":
        add()
    elif decisao == "V":
        vis()
    elif decisao == "M":
        mod()
    elif decisao == "E":
        exc()
    elif decisao == "F":
        fav()
    elif decisao == "L":
        vis_fav()
    elif decisao == "X":
        exc_ing()
    elif decisao == "Q":
        break
    else:
        print("Opção inválida. Tente novamente.")
