# 📸 Creative Validator API  🛠️

Bem-vindo ao repositório da **Creative Validator API**! Este projeto foi desenvolvido para sanar um problema específico em um processo interno, mas o código está aberto para que possa ajudar outras pessoas que enfrentem desafios semelhantes. 🚀

## 🌟 O que esta API faz?

Esta API realiza as seguintes tarefas:

1. **📥 Baixa imagens do Amazon S3**: A API se conecta ao Amazon S3 e faz o download das imagens armazenadas em um bucket específico.
2. **🌐 Faz requests para uma API específica**: Após o download, a API envia as imagens para uma API externa que realiza análises específicas.
3. **🔍 Cruza os dados**: A API cruza os dados retornados pela API externa com as informações locais para verificar a precisão das imagens.
4. **✅ Verifica a correção das imagens**: Por fim, a API verifica se as imagens estão corretas com base nos critérios definidos.

## 🛠️ Tecnologias Utilizadas

- **Python**: A linguagem principal utilizada para desenvolver a API.
- **Boto3**: Biblioteca para interagir com os serviços da AWS, como o S3.
- **Requests**: Biblioteca para fazer requisições HTTP para a API externa.
- **Docker**: Para containerização da aplicação, facilitando a implantação e o desenvolvimento.

## 🚀 Como usar?

### Pré-requisitos

- **Python 3.8+**: Certifique-se de ter o Python instalado.
- **Conta AWS**: Para acessar o Amazon S3.
- **Docker**: Caso queira rodar a API em um container.

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/sua-api.git
   cd sua-api
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente:

   Crie um arquivo `.env` na raiz do projeto:

4. Execute a API:

   ```bash
   python run.py
   ```

## 📄 Licença

Open-source