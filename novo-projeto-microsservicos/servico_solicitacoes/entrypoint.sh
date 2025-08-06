#!/bin/sh

# Verifica se a variável de ambiente DB_HOST foi definida
if [ -z "$DB_HOST" ]; then
  echo "Erro: A variável de ambiente DB_HOST não está definida."
  exit 1
fi

echo "Aguardando o banco de dados em: $DB_HOST"

# Loop até que a porta do PostgreSQL (5432) esteja aberta
# O nc (netcat) tenta estabelecer uma conexão
while ! nc -z $DB_HOST 5432; do
  echo "Aguardando..."
  sleep 1
done

echo "Banco de dados conectado!"

# Execute o comando principal do contêiner (passado pelo docker-compose)
exec "$@"
