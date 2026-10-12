estoque = []

while True:
    print('=' * 10, end=' ')
    print('Controle de Estoque', end=' ')
    print('=' * 10)
    print('[1] Cadastrar produto\n'
          '[2] Listar produto\n'
          '[3] Buscar produto\n'
          '[4] Entrada de estoque\n'
          '[5] Saída de estoque\n'
          '[0] Sair\n')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 0:
        break

    if opcao == 1:

        print('=' * 10, end=' ')
        print('Cadastro de Produtos', end=' ')
        print('=' * 10)
        item = {'nome': input('Nome do produto: ').upper().strip(), 'quantidade': int(input('Quantidade: ')),
                'preco': float(input('Preço: R$ '))}

        estoque.append(item)

    if opcao == 2:
        if not estoque:
            print('Nenhum produto cadastrado!\n')

        else:
            print('=' * 10, end=' ')
            print('Produtos Cadastrados', end=' ')
            print('=' * 10)

            for p in estoque:
                print(f"Produto: {p['nome']}")
                print(f"Quantidade: {p['quantidade']}")
                print(f"Preço: R${p['preco']:.2f}")

    if opcao == 3:
        busca = input('Digite o nome do produto que deseja buscar: ').upper().strip()
        encontrado = False

        for b in estoque:
            if busca == b['nome']:
                encontrado = True
                print('Produto encontrado!')
                print(f"Produto: {b['nome']}")
                print(f"Quantidade: {b['quantidade']}")
                print(f"Preço: R${b['preco']:.2f}")

        if encontrado == False:
            print('Não há produto cadastrado com este nome.\n')

    if opcao == 4:
        busca = input('Digite o nome do produto que deseja buscar: ').upper().strip()
        quant = int(input('Qual a quantidade deseja dar de entrada ? '))
        encontrado = False

        for b in estoque:
            if busca == b['nome']:
                encontrado = True
                print('-' * 30)
                print('Produto encontrado!')
                print(f"O saldo atual de {b['nome']} é de {b['quantidade']} unidades.")
                b['quantidade'] += quant
                print(f"O saldo atualizado é de {b['quantidade']} unidades.")

    if opcao == 5:
        busca = input('Digite o nome do produto que deseja buscar: ').upper().strip()
        quant = int(input('Qual a quantidade deseja dar de saída ? '))
        encontrado = False

        for b in estoque:
            if busca == b['nome']:
                encontrado = True
                print('-' * 30)
                print('Produto encontrado!')

                if b['quantidade'] - quant < 0:
                    print('Saldo indisponível !')
                    print(f"O saldo atual de {b['nome']} é de {b['quantidade']} unidades.")

                else:
                    b['quantidade'] -= quant
                    print(f"O saldo atualizado é de {b['quantidade']} unidades.")

                break

        if not encontrado:
            print('Não há produto cadastrado com este nome.\n')


