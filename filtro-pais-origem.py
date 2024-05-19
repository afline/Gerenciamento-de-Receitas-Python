# Função para filtrar receitas por país de origem
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
