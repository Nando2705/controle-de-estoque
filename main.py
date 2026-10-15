import os
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.getenv('MYSQL_PASSWORD'),
    database='estoque'
)

cursor = conexao.cursor()

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

        nome = input('Nome do produto: ').upper().strip()
        quantidade = int(input('Quantidade: '))

        if quantidade < 0:
            print('Quantidade inválida!')
        else:
            preco = float(input('Preço: R$ '))
            cursor.execute(
                'INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s)',
                (nome, quantidade, preco)
            )
            conexao.commit()
            print('Produto cadastrado com sucesso!')


    if opcao == 2:
        cursor.execute('SELECT * FROM produtos')
        resultado = cursor.fetchall()

        if not resultado:
            print('Nenhum produto cadastrado!\n')
        else:
            print('=' * 10, end=' ')
            print('Produtos Cadastrados', end=' ')
            print('=' * 10)

            for p in resultado:
                print(f'Produto: {p[1]}')
                print(f'Quantidade: {p[2]}')
                print(f'Preço: R${p[3]:.2f}')
                print('-' * 20)

    if opcao == 3:
        busca = input('Digite o nome do produto que deseja buscar: ').upper().strip()

        cursor.execute(
            'SELECT * FROM produtos WHERE nome = %s',
            (busca,)
        )
        resultado = cursor.fetchall()

        if not resultado:
            print('Não há produto cadastrado com este nome.\n')
        else:
            for b in resultado:
                print('Produto encontrado!')
                print(f'Produto: {b[1]}')
                print(f'Quantidade: {b[2]}')
                print(f'Preço: R${b[3]:.2f}')

    if opcao == 4:
        busca = input('Digite o nome do produto: ').upper().strip()
        quant = int(input('Qual quantidade deseja dar de entrada? '))

        if quant <= 0:
            print('Quantidade inválida!')
        else:
            cursor.execute(
                'SELECT * FROM produtos WHERE nome = %s',
                (busca,)
            )
            resultado = cursor.fetchall()

            if not resultado:
                print('Não há produto cadastrado com este nome.')
            else:
                cursor.execute(
                    'UPDATE produtos SET quantidade = quantidade + %s WHERE nome = %s',
                    (quant, busca)
                )
                conexao.commit()
                print('Entrada de estoque realizada com sucesso!')

                cursor.execute(
                    'SELECT * FROM produtos WHERE nome = %s',
                    (busca,)
                )
                resultado = cursor.fetchall()

                for p in resultado:
                    print(f"Produto: {p[1]}")
                    print(f"Saldo atualizado: {p[2]} unidades.")

    if opcao == 5:
        busca = input('Digite o nome do produto: ').upper().strip()
        quant = int(input('Qual quantidade deseja dar de saída? '))

        if quant <= 0:
            print('Quantidade inválida!')
        else:
            cursor.execute(
                'SELECT * FROM produtos WHERE nome = %s',
                (busca,)
            )
            resultado = cursor.fetchall()

            if not resultado:
                print('Não há produto cadastrado com este nome.')
            else:
                for p in resultado:
                    print(f"Produto: {p[1]}")
                    print(f"Saldo atual: {p[2]} unidades.")

                    if quant > p[2]:
                        print('Saldo insuficiente!')
                    else:
                        cursor.execute(
                            'UPDATE produtos SET quantidade = quantidade - %s WHERE nome = %s',
                            (quant, busca)
                        )
                        conexao.commit()

                        print('Saída de estoque realizada com sucesso!')
                        print(f'Saldo atualizado: {p[2] - quant} unidades.')


print('Programa encerrado!')
