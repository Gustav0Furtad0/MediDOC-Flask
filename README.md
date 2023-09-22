# **MediDOC - Sistema de Gerenciamento de Prontuários Médicos**

O **MediDOC** é um sistema de gerenciamento de prontuários médicos desenvolvido com Flask, SQLAlchemy e outras tecnologias web. Ele permite que médicos e profissionais de saúde armazenem e gerenciem prontuários médicos de seus pacientes de forma eficiente.

## **Funcionalidades Principais**

- Registro e autenticação de médicos.
- Adição, edição e exclusão de pacientes.
- Criação, edição e visualização de prontuários médicos.
- Controle de acesso com autenticação Flask-Session.
- Sistema de busca para localizar rapidamente prontuário

## **Pré-requisitos**

- Python 3.x
- Flask
- Flask SQLAlchemy
- Outras dependências listadas em **`requirements.txt`**

## **Instalação e Uso**

1. Clone o repositório do **MediDOC**:

```bash
git clone https://github.com/seu-usuario/medidoc.git
cd medidoc
```

1. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
# Ou
venv\Scripts\activate  # Para Windows

pip install -r requirements.txt
```

1. Configure as variáveis de ambiente no arquivo **`.env`** (ou renomeie **`.env.example`**):

```bash
# Configurações de banco de dados
DATABASE_URL=sqlite:///database.db  # Você pode usar outro banco de dados, se preferir

# Configurações adicionais
DEBUG=True  # Ative o modo de depuração em desenvolvimento
```

1. Crie o banco de dados e execute as migrações:

```bash
flask db init
flask db migrate
flask db upgrade
```

1. Inicie o aplicativo:

```bash
flask run
```

1. Acesse o aplicativo em seu navegador em **[http://localhost:5000](http://localhost:5000/)**.

## **Autor**

[Gustavo de Jesus Furtado](https://www.linkedin.com/in/gustavo-furtado02/)

## **Licença**

Este projeto está licenciado sob a **[Licença MIT](https://chat.openai.com/c/LICENSE.md)**.

## **Reconhecimentos**

- Agradeço à comunidade Flask e ao ecossistema Python por fornecer as ferramentas para criar este aplicativo.

## **Contato**

Para perguntas ou sugestões, entre em contato com [gufurtado02@gmail.com](mailto:gufurtado02@gmail.com).