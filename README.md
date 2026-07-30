# Especificação do Sistema – Controle de Despesas

## 1. Objetivo

O sistema de Controle de Despesas tem como objetivo permitir o gerenciamento de gastos pessoais de forma simples e organizada. A aplicação possibilitará o cadastro, consulta, atualização e exclusão de despesas, permitindo ao usuário acompanhar seus gastos por categoria e período.

---

# 2. Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework:** Django
* **Banco de Dados:** SQLite
* **Frontend:** HTML, CSS e Bootstrap
* **ORM:** Django ORM

---

# 3. Funcionalidades

## Cadastro de Despesas

Permite registrar uma nova despesa contendo:

* Descrição
* Valor
* Categoria
* Data da despesa

---

## Listagem de Despesas

O sistema deverá exibir todas as despesas cadastradas, permitindo:

* Ordenação por data;
* Pesquisa por descrição;
* Filtro por categoria;
* Filtro por período.

---

## Edição de Despesas

O usuário poderá alterar qualquer informação de uma despesa previamente cadastrada.

---

## Exclusão de Despesas

Permite remover uma despesa mediante confirmação do usuário.

---

## Relatórios

O sistema deverá apresentar:

* Total gasto no período;
* Total gasto por categoria;
* Quantidade de despesas cadastradas;
* Média de gastos.

---

# 4. Modelo de Dados

## Tabela: Categoria

| Campo | Tipo        | Restrições         |
| ----- | ----------- | ------------------ |
| id    | Integer     | PK                 |
| nome  | Varchar(50) | Obrigatório, único |

---

## Tabela: Despesa

| Campo         | Tipo                  | Restrições  |
| ------------- | --------------------- | ----------- |
| id            | Integer               | PK          |
| descricao     | Varchar(150)          | Obrigatório |
| valor         | Decimal(10,2)         | Obrigatório |
| data          | Date                  | Obrigatório |
| categoria     | ForeignKey(Categoria) | Obrigatório |
| criado_em     | DateTime              | Automático  |
| atualizado_em | DateTime              | Automático  |

---

# 5. Regras de Negócio

### RN01

Toda despesa deve possuir uma descrição.

---

### RN02

O valor da despesa deve ser maior que zero.

---

### RN03

A data da despesa não poderá ser nula.

---

### RN04

Toda despesa deve estar vinculada a uma categoria.

---

### RN05

Não poderão existir categorias com o mesmo nome.

---

### RN06

Não será permitida a exclusão de uma categoria que possua despesas cadastradas.

---

### RN07

Ao cadastrar uma despesa, o sistema deverá validar todos os campos obrigatórios antes de salvar.

---

### RN08

O valor será armazenado utilizando duas casas decimais.

---

### RN09

As despesas deverão ser exibidas, por padrão, da mais recente para a mais antiga.

---

### RN10

O sistema deverá calcular automaticamente:

* Soma total das despesas;
* Média de gastos;
* Total por categoria.

---

### RN11

O sistema permitirá pesquisa por:

* Descrição;
* Categoria;
* Intervalo de datas.

---

### RN12

Toda alteração realizada em uma despesa deverá atualizar automaticamente o campo **atualizado_em**.

---

# 6. Estrutura do Projeto Django

```
controle_despesas/
│
├── manage.py
├── controle_despesas/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── despesas/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── despesas/
│   ├── static/
│   └── migrations/
```

---

# 7. Telas do Sistema

1. Página inicial
2. Listagem de despesas
3. Cadastro de despesa
4. Edição de despesa
5. Exclusão de despesa
6. Cadastro de categorias
7. Relatório de gastos

---

# 8. Fluxo do Sistema

1. O usuário acessa a aplicação.
2. Cadastra as categorias de despesas.
3. Registra uma nova despesa.
4. O sistema valida os dados e salva no banco SQLite.
5. As despesas são exibidas em uma lista ordenada por data.
6. O usuário pode pesquisar, editar ou excluir registros.
7. O sistema gera automaticamente os totais e relatórios de despesas.
