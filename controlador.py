import modelo


class Controlador:
    @staticmethod
    def cadastrar_produto(lista: list):
        while True:
            try:
                novo_produto = modelo.Produto(nome=input("Insira o nome do produto: "),
                                              preco=float(input("insira o preco do produto: ")),
                                              quantidade=int(input("Insira a quantidade do produto: ")))

                if not (novo_produto.nome and novo_produto.preco and novo_produto.quantidade):
                    raise ValueError("Por favor, preencha todos os campos.")
                lista.append(novo_produto)
                print("Produto cadastrado com sucesso\n")
                break

            except ValueError as error:
                print(error)

    @staticmethod
    def consultar_produto(lista: list):
        while True:
            try:
                produto_a_consultar = input("Insira o nome do produto: ").strip()

                if not produto_a_consultar:
                    raise ValueError("Por favor, insira o nome do produto")

                for item in lista:
                    if produto_a_consultar.lower() == item.nome.lower():
                        print(f"\nNome: {item.nome.capitalize()}\nPreço: R${round(item.preco, 2)}\nQuantidade: {item.quantidade}\n")
                        return

                raise ValueError("Produto não encontrado.")

            except ValueError as error:
                print(error)
                break

    @staticmethod
    def atualizar_estoque(lista: list):
        while True:
            try:
                produto_a_atualizar = input("Insira o nome do produto: ").strip()

                if not produto_a_atualizar:
                    raise ValueError("Por favor, insira o nome do produto")

                produto_encontrado = None
                for item in lista:
                    if produto_a_atualizar.lower() == item.nome.lower():
                        produto_encontrado = item
                        break

                if produto_encontrado is None:
                    raise ValueError("Produto não encontrado.")

                while True:
                    print('''    
                        [1] Adicionar ao estoque
                        [2] Remover do estoque
                        [3] Sair''')
                    opcao = int(input("Insira o número da opção para executá-la: "))

                    if opcao == 1:
                        quantidade_a_acrescentar = int(input("Insira a quantidade a acrescentar: "))
                        if quantidade_a_acrescentar < 0:
                            raise ValueError("A quantidade a acrescentar deve ser positiva.")
                        produto_encontrado.quantidade += quantidade_a_acrescentar
                        print(f"Quantidade atualizada. Nova quantidade: {produto_encontrado.quantidade}\n")
                    elif opcao == 2:
                        quantidade_a_remover = int(input("Insira a quantidade a remover: "))
                        if quantidade_a_remover < 0:
                            raise ValueError("A quantidade a remover deve ser positiva.")
                        if quantidade_a_remover > produto_encontrado.quantidade:
                            raise ValueError("Não há estoque suficiente para remover essa quantidade.")
                        produto_encontrado.quantidade -= quantidade_a_remover
                        print(f"Quantidade atualizada. Nova quantidade: {produto_encontrado.quantidade}\n")
                    elif opcao == 3:
                        print("Saindo da atualização de estoque.")
                        return
                    else:
                        print("Opção inválida. Tente novamente.")

            except ValueError as error:
                print(error)







