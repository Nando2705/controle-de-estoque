# Controle de Estoque

Projeto desenvolvido em Python com integração ao MySQL para gerenciar produtos e quantidades em estoque.

## Funcionalidades

- **Cadastrar produtos:** registra nome, quantidade e preço.
- **Listar produtos:** exibe os produtos cadastrados.
- **Buscar produtos:** localiza um produto pelo nome.
- **Entrada de estoque:** adiciona unidades ao saldo existente.
- **Saída de estoque:** retira unidades, verificando se há saldo suficiente.
- **Validação:** impede quantidades negativas no cadastro e quantidades menores ou iguais a zero nas operações de entrada e saída.

## Tecnologias utilizadas

- Python
- MySQL
- mysql-connector-python
- SQL: `SELECT`, `INSERT` e `UPDATE`

## Estrutura do banco de dados

Banco: `estoque`

Tabela: `produtos`

| Campo | Descrição |
|---|---|
| `id` | Identificador do produto |
| `nome` | Nome do produto |
| `quantidade` | Quantidade em estoque |
| `preco` | Preço unitário |

## Como executar

1. Instale o Python e o MySQL.
2. Instale a biblioteca de conexão:

   ```bash
   pip install mysql-connector-python
   ```

3. Crie o banco de dados `estoque` e a tabela `produtos`, caso ainda não existam.
4. Configure a variável de ambiente `MYSQL_PASSWORD` com a senha do usuário do MySQL.
5. Confira os parâmetros de conexão no arquivo `main.py`.
6. Execute o programa pelo PyCharm.

## Segurança

As credenciais devem ficar fora do código-fonte. Não publique senhas no repositório.

## Objetivo

Praticar lógica de programação, Python, comandos SQL, validação de dados e integração com banco de dados relacional.

Projeto em desenvolvimento, com funcionalidades implementadas e testadas gradualmente.
