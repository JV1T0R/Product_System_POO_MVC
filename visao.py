import controlador
import modelo

while True:
    print('''    
    [1] Cadastrar produto
    [2] Consultar produto
    [3] Atualizar estoque
    [4] Sair''')
    opcao = int(input("insira o número da opção para executa-la: "))

    if opcao == 1:
        novo_cadastro = controlador.Controlador()
        novo_cadastro.cadastrar_produto(modelo.produtos)

    elif opcao == 2:
        controlador.Controlador.consultar_produto(modelo.produtos)

    elif opcao == 3:
        controlador.Controlador.atualizar_estoque(modelo.produtos)

    elif opcao == 4:
        print("sistema Encerrado.")
        break

    else:
        print("Opção Invalida")
