# coffee-shop



## Requisitos Funcionais:

#### 1- Adicionar Itens ao Cardápio:

O sistema deve permitir a adição de novos itens ao cardápio.
Cada item deve pertencer a uma categoria pré-definida (Bebida, Entradas, Pratos Principais, Sobremesas).
Para cada item, o usuário deve inserir o produto e seu respectivo preço.
O novo cardápio deve ser armazenado automaticamente no arquivo de dados.

#### 2- Excluir Itens do Cardápio:

O sistema deve permitir a exclusão de itens existentes no cardápio.
O usuário deve especificar a categoria, o item e o produto a ser removido.
Após a exclusão, o cardápio atualizado deve ser salvo no arquivo de dados.

#### 3- Alterar Itens do Cardápio:

Os usuários devem ter a capacidade de alterar o preço de um produto existente no cardápio.
Eles devem especificar a categoria, o item e o produto que desejam modificar, bem como o novo preço.
Após a alteração, o cardápio atualizado deve ser salvo no arquivo de dados.

#### 4- Buscar Itens no Cardápio:

O sistema deve permitir aos usuários buscar itens no cardápio com base em um termo de pesquisa.
A busca deve ser insensível a maiúsculas/minúsculas.
Os resultados da pesquisa devem ser exibidos ao usuário.

#### 5- Listar Todos os Itens do Cardápio:

Os usuários devem poder listar todos os itens do cardápio, agrupados por categoria.
Cada item deve exibir o nome do produto e seu preço.

#### 6- Calcular Total a Pagar:

O sistema deve permitir aos usuários selecionar itens do cardápio para compra.
Depois de selecionar os itens desejados, o sistema deve calcular o total a pagar.
O total deve incluir os preços dos produtos escolhidos e a porcentagem do garçom.
O usuário deve ter a opção de finalizar a compra ou adicionar mais itens.


## Requisitos Não Funcionais:

#### 1- Armazenamento Persistente:

O cardápio e as configurações do restaurante (nome e porcentagem do garçom) devem ser armazenados em arquivos de texto.
O sistema deve ser capaz de carregar esses dados armazenados ao iniciar e salvar as atualizações automaticamente.

#### 2- Usabilidade Intuitiva:

O programa deve ser fácil de usar, com instruções claras e prompts para orientar o usuário durante a interação.

#### 3- Eficiência:

As operações de adição, remoção e atualização do cardápio devem ser executadas de forma eficiente, mesmo com grandes conjuntos de dados.

#### 4- Robustez:

O sistema deve lidar adequadamente com entradas inválidas ou inesperadas do usuário, garantindo que não ocorram falhas inesperadas.

#### 5- Portabilidade:

O programa deve ser capaz de ser executado em diferentes sistemas operacionais e ambientes Python compatíveis.

#### 6- Segurança:

Assegure-se de que apenas usuários autorizados possam acessar e modificar o cardápio e as configurações do restaurante.
