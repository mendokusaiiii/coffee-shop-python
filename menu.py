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

def mostrar_menu():
    print("Cardápio:")
    for categoria, subcategorias in menu.items():
        print(f"{categoria.capitalize()}:")
        for subcategoria, produtos in subcategorias.items():
            print(f"  {subcategoria.capitalize()}:")
            for produto, preco in produtos.items():
                print(f"    {produto} - R${preco:.2f}")

def selecionar_itens():
    pedido = []
    while True:
        mostrar_menu()
        categoria = input('Digite a categoria do produto para adicionar ao pedido ou "F" para finalizar: ').lower()
        if categoria == 'f':
            break
        if categoria not in menu:
            print("Categoria inválida. Tente novamente.")
            continue
        subcategoria = input('Digite a sub-categoria do produto: ').lower()
        if subcategoria not in menu[categoria]:
            print("Sub-categoria inválida. Tente novamente.")
            continue
        produto = input('Digite o nome do produto: ').lower()
        if produto not in menu[categoria][subcategoria]:
            print("Produto inválido. Tente novamente.")
            continue
        pedido.append((produto, menu[categoria][subcategoria][produto]))
        print(f"{produto} adicionado ao pedido.")
    return pedido

def calcular_total(pedido, taxa_garcom):
    total = sum(preco for _, preco in pedido)
    total_com_taxa = total * (1 + taxa_garcom)
    return total_com_taxa

def main():
#adicionando comentario para mudancas

    taxa_garcom = 0.10
    while True:
        escolha = int(input(f'Digite (1) para ADICIONAR produtos ao cardápio.\n'
                            f'Digite (2) para REMOVER produtos do cardápio.\n'
                            f'Digite (3) para ALTERAR algum produto já existente.\n'
                            f'Digite (4) para SELECIONAR itens do cardápio para compra.\n'
                            f'Digite (5) para SAIR e salvar.\nO que deseja fazer: '))
        if escolha == 1:
            add()
        elif escolha == 2:
            remove()
        elif escolha == 3:
            change()
        elif escolha == 4:
            pedido = selecionar_itens()
            if pedido:
                total = calcular_total(pedido, taxa_garcom)
                print("\nItens no pedido:")
                for item, preco in pedido:
                    print(f"- {item} - R${preco:.2f}")
                print(f"Total com taxa de serviço ({taxa_garcom * 100}%): R${total:.2f}")
            else:
                print("Nenhum item no pedido.")
        else:
            break
            
with open('Cardapio.txt', 'w') as a: 
  a.write(json.dumps(menu))
            

if __name__ == "__main__":
    main()
