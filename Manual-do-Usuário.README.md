Manual do Usuário

Alunos: Aline Farias Amancio, George Almerio Alves Neto, Tiago Emílio Rodrigues de Abreu, Vinícius Sposito Antonino Nogueira

Grupo 4

Sistema de Gerenciamento de Receitas

Este manual fornece instruções sobre como usar o sistema de gerenciamento de receitas para organizar e gerenciar suas receitas favoritas.


Funcionalidades


Adicionar Receita: Permite adicionar uma nova receita ao sistema.
Visualizar Receitas: Exibe todas as receitas cadastradas.
Atualizar Receita: Permite atualizar informações de uma receita existente.
Excluir Receita: Permite excluir uma receita do sistema.
Filtrar por País: Exibe receitas de acordo com o país de origem.
Marcar/Desmarcar Favorita: Permite marcar ou desmarcar uma receita como favorita.
Visualizar Favoritas: Exibe todas as receitas marcadas como favoritas.
Sugerir Receita Aleatória: Sugere uma receita aleatória do sistema.
Excluir por Ingrediente: Exclui receitas que contenham um ingrediente específico.



Passo a Passo


Iniciar o Sistema:
Execute o arquivo Python que contém o código do sistema. 
Escreva qualquer coisa, exceto “SAIR”, para continuar no menu principal.
O menu principal será exibido com as opções disponíveis.

Adicionar Receita:
Selecione “add” no menu principal
Insira as informações solicitadas: nome da receita, país de origem, ingredientes e modo de preparo.
A receita será adicionada ao sistema e salva no arquivo CSV.

Visualizar Receitas:
Selecione “viz” no menu principal.
Todas as receitas cadastradas serão exibidas.

Modificar Receita:
Selecione “mod” no menu principal.
Insira o nome da receita a ser atualizada.
Atualize as informações desejadas.
As informações atualizadas serão salvas no arquivo CSV.

Excluir Receita:
Selecione “exc” no menu principal.
Insira o nome da receita a ser excluída.
A receita será removida do sistema e do arquivo CSV.

Filtrar por País:
Selecione “filtrar_por_pais” no menu principal.
Insira o país de origem das receitas que deseja visualizar.
As receitas filtradas serão exibidas.

Marcar/Desmarcar Favorita:
Selecione “fav” no menu principal.
Insira o nome da receita a ser marcada ou desmarcada como favorita.
Aparecerá a opção de “Favorito: ”, onde será respondido “sim” para marcar como favorito, e “não” para desmarcar como favorito.
O status de favorito será atualizado no sistema e no arquivo CSV.

Visualizar Favoritas:
Selecione “vis_fav” no menu principal.
Todas as receitas marcadas como favoritas serão exibidas.

Sugerir Receita Aleatória:
Selecione “aleatorio” no menu principal.
Uma receita aleatória será sugerida.

Excluir por Ingrediente:
Selecione “exc_ing” no menu principal.
Insira o ingrediente que deseja buscar.
As receitas que contêm o ingrediente serão exibidas.

Sair do Sistema:
Selecione “SAIR” no menu principal para sair do sistema.



Exceções e Tratamento de Erros

O sistema lida com a ausência do arquivo CSV criando um novo arquivo quando necessário. Caso a receita buscada para atualização, exclusão ou marcação/desmarcação de favoritas não seja encontrada, uma mensagem de erro será exibida. Entradas inválidas no menu principal serão tratadas com uma mensagem de erro e uma nova solicitação de entrada.

![Fluxograma](https://github.com/georgenetoo/Python-Project/assets/167882901/24ffadb1-61b8-4f79-9a89-9494bb59f154)


