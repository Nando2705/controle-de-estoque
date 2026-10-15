# 📦 Controle de Estoque em Python e MySQL

Projeto de estudos desenvolvido em Python com integração ao MySQL para gerenciar produtos de um estoque.

O objetivo é aplicar, na prática, os conceitos de programação e banco de dados, evoluindo o sistema passo a passo.

## 🚀 Funcionalidades implementadas

- **Listagem de produtos:** consulta os produtos cadastrados no banco de dados.
- **Cadastro de produtos:** permite informar nome, quantidade e preço.
- **Validação de quantidade:** impede o cadastro quando a quantidade informada é negativa.
- **Menu interativo:** permite navegar pelas opções e encerrar o programa.
- **Persistência de dados:** armazena os produtos no MySQL.

## 🛠️ Tecnologias utilizadas

- Python 3
- MySQL
- `mysql-connector-python`
- PyCharm
- Git e GitHub

## 📚 Conceitos estudados

### Python

- Variáveis e tipos de dados: `str`, `int` e `float`
- Entrada de dados com `input()`
- Conversão de tipos
- Estruturas condicionais: `if`, `elif` e `else`
- Laço de repetição `while`
- Laço `for` para percorrer resultados
- Uso de `break` para encerrar o menu
- Indentação e organização do código

### SQL e MySQL

- Conexão com o banco de dados
- Consulta de registros com `SELECT`
- Recuperação de resultados com `fetchall()`
- Inserção de registros com `INSERT INTO`
- Uso de parâmetros nas consultas
- Confirmação das alterações com `commit()`
- Fechamento do cursor e da conexão

## ⚙️ Configuração do projeto

1. Instale o Python 3.
2. Instale o MySQL e crie o banco de dados `estoque`.
3. Crie a tabela `produtos` com as colunas `id`, `nome`, `quantidade` e `preco`.
4. Instale o conector do MySQL:

   ```bash
   pip install mysql-connector-python
   ```

5. Configure os dados de conexão no arquivo Python, usando as credenciais locais do MySQL.
6. Execute `main.py`.

**Segurança:** não publique senhas ou outras credenciais no repositório. Use variáveis de ambiente ou outra forma segura de configuração.

## 📈 Próximas melhorias

- Validar entradas que não sejam números.
- Implementar busca de produtos.
- Implementar entrada e saída de estoque.
- Melhorar a organização do código.
- Aprimorar o tratamento de erros.

## 👨‍💻 Objetivo

Construir um projeto prático para consolidar os conhecimentos em Python, SQL e MySQL, desenvolvendo gradualmente uma aplicação de controle de estoque.
