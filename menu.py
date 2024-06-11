import json

with open('Cardapio.txt', 'r') as a:
    menu = json.load(a)
    
def add():
    categoria = input('Digite a categoria do produto: ')
    while categoria.lower() not in menu:
        categoria = input('Digite a categoria do produto novamente: ')
    subcategoria = input('Digite a sub-categoria do produto: ')
    while subcategoria.lower() not in menu[categoria]:
        subcategoria = input('Digite a sub-categoria do produto novamente: ')
    while True:
        produto = input('Digite o nome do produto ou "sair" para parar de adicionar itens: ')
        if produto.lower() == 'sair':
            break
        preco = float(input('Digite o preço do produto: '))
        menu[categoria][subcategoria][produto] = preco

def remove():
    categoria = input('Digite a categoria do produto que deseja remover: ')
    while categoria.lower() not in menu:
        categoria = input('Digite a categoria do produto que deseja remover novamente: ')
    subcategoria = input('Digite a sub-categoria do produto que deseja remover: ')
    while subcategoria.lower() not in menu[categoria]:
        subcategoria = input('Digite a sub-categoria do produto que deseja remover novamente: ')
    while True:
        produto = input('Digite o nome do produto que deseja remover ou "sair" para parar: ')
        if produto.lower() == 'sair':
            break
        if produto not in menu[categoria][subcategoria]:
            produto = input('Este produto não existe no cardapio, verifique se esta em outra categoria, volte para adiciona-lo (digite "sair") ou tente novamente: ')
            if produto.lower() == 'sair':
                break
        else: 
            del menu[categoria][subcategoria][produto]
            print(f'Produto {produto} removido com sucesso!')

def change():
    categoria = input('Digite a categoria do produto que deseja alterar: ')
    while categoria.lower() not in menu:
        categoria = input('Digite a categoria do produto que deseja alterar novamente: ')
    subcategoria = input('Digite a sub-categoria do produto que deseja alterar: ')
    while subcategoria.lower() not in menu[categoria]:
        subcategoria = input('Digite a sub-categoria do produto que deseja alterar novamente: ')
    produto = input('Digite o nome do produto que deseja alterar: ')
    while produto not in menu[categoria][subcategoria]:
        produto = input('Este produto não existe no cardapio, verifique se esta em outra categoria, volte para adiciona-lo (digite "sair") ou tente novamente: ')
        if produto.lower() == 'sair':
            break
    while True:
        novoproduto = input('Digite o nome do novo produto (digite "sair" para parar de alterar itens): ')
        if novoproduto.lower() == 'sair':
            break
        novopreco = float(input('Digite o novo preco do produto: '))
        menu[categoria][subcategoria].pop(produto)
        menu[categoria][subcategoria][novoproduto] = novopreco

while 1 == 1:
    escolha = int(input(f'Digite (1) para ADICIONAR produtos ao cardapio.\nDigite (2) para REMOVER produtos do cardapio.\nDigite (3) para ALTERAR algum produto ja existente.\nDigite (4) para SAIR e salvar.\nO que deseja fazer: '))
    if escolha == 1:
        add()
    elif escolha == 2:
        remove()
    elif escolha == 3:
        change()
    else:
        break
    
with open('Cardapio.txt', 'w') as a: 
    a.write(json.dumps(menu))