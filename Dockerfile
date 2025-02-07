# Usa a imagem oficial do Python como base
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários para o container
COPY requirements.txt ./
COPY . ./

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Copia todo o restante do código (caso tenha mais arquivos)
COPY . .

# Comando para rodar o script
CMD ["python", "run.py"]
