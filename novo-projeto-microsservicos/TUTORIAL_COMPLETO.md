# 🚀 Tutorial Completo: Microsserviços com Django e Docker

## 📋 Visão Geral do Projeto

Este projeto implementa uma **arquitetura de microsserviços** usando Django REST Framework e Docker Compose. O sistema é composto por 4 microsserviços independentes que se comunicam entre si para formar uma aplicação completa de gerenciamento de solicitações de serviços.

### 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│                        MICROSSERVIÇOS                          │
├─────────────────┬─────────────────┬─────────────────┬─────────────────┤
│  🏪 CATÁLOGO   │  👥 PESSOAS     │  🛠️ SERVIÇOS   │  📋 SOLICITAÇÕES │
│                │                 │                 │                 │
│ - Categorias   │ - Pessoas       │ - Tipos de      │ - Coordena      │
│ - Produtos     │                 │   Serviços      │   tudo          │
│                │                 │                 │                 │
│ Porto: 8001    │ Porto: 8002     │ Porto: 8003     │ Porto: 8004     │
│ DB: catalogo   │ DB: pessoas     │ DB: servicos    │ DB: solicitacoes│
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

---

## 📁 Estrutura do Projeto

```
novo-projeto-microsservicos/
├── 📄 docker-compose.yml          # Orquestração de todos os serviços
├── 📄 TUTORIAL_COMPLETO.md        # Este arquivo
│
├── 🏪 servico_catalogo/           # Microsserviço de Catálogo
│   ├── 📄 Dockerfile
│   ├── 📄 entrypoint.sh
│   ├── 📄 requirements.txt
│   ├── 📄 manage.py
│   ├── catalogo/                  # App Django
│   │   ├── 📄 models.py          # Categoria, Produto
│   │   ├── 📄 views.py           # APIs REST
│   │   ├── 📄 serializers.py     # Conversão JSON
│   │   └── 📄 urls.py            # Rotas da API
│   └── servico_catalogo/          # Configurações Django
│       └── 📄 settings.py
│
├── 👥 servico_pessoas/            # Microsserviço de Pessoas
│   ├── 📄 Dockerfile
│   ├── 📄 entrypoint.sh
│   ├── 📄 requirements.txt
│   ├── 📄 manage.py
│   ├── pessoas/                   # App Django
│   │   ├── 📄 models.py          # Pessoa
│   │   ├── 📄 views.py           # APIs REST
│   │   ├── 📄 serializers.py     # Conversão JSON
│   │   └── 📄 urls.py            # Rotas da API
│   └── servico_pessoas/           # Configurações Django
│       └── 📄 settings.py
│
├── 🛠️ servico_servicos/           # Microsserviço de Serviços
│   ├── 📄 Dockerfile
│   ├── 📄 entrypoint.sh
│   ├── 📄 requirements.txt
│   ├── 📄 manage.py
│   ├── servicos/                  # App Django
│   │   ├── 📄 models.py          # Servico
│   │   ├── 📄 views.py           # APIs REST
│   │   ├── 📄 serializers.py     # Conversão JSON
│   │   └── 📄 urls.py            # Rotas da API
│   └── servico_servicos/          # Configurações Django
│       └── 📄 settings.py
│
└── 📋 servico_solicitacoes/       # Microsserviço Coordenador
    ├── 📄 Dockerfile
    ├── 📄 entrypoint.sh
    ├── 📄 requirements.txt
    ├── 📄 manage.py
    ├── solicitacoes/              # App Django
    │   ├── 📄 models.py          # SolicitarServico
    │   ├── 📄 views.py           # APIs REST + Comunicação
    │   ├── 📄 serializers.py     # Conversão JSON
    │   └── 📄 urls.py            # Rotas da API
    └── servico_solicitacoes/      # Configurações Django
        └── 📄 settings.py
```

---

## 🛠️ Tecnologias Utilizadas

### **Backend**
- **Python 3.11** - Linguagem de programação
- **Django 5.0.6** - Framework web
- **Django REST Framework 3.15.1** - APIs REST
- **psycopg2-binary 2.9.9** - Driver PostgreSQL
- **requests 2.32.3** - Comunicação HTTP entre microsserviços

### **Banco de Dados**
- **PostgreSQL 15** - Banco de dados relacional
- **4 bancos independentes** - Um para cada microsserviço

### **Containerização**
- **Docker** - Containerização dos microsserviços
- **Docker Compose** - Orquestração de múltiplos containers
- **netcat-traditional** - Verificação de conectividade

---

## 🎯 Microsserviços Detalhados

### 🏪 1. Serviço de Catálogo (Porto 8001)

**Responsabilidade:** Gerenciar categorias e produtos do sistema.

#### **Modelos:**
```python
# catalogo/models.py
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
```

#### **APIs Disponíveis:**
- `GET/POST /api/categorias/` - Listar/Criar categorias
- `GET/PUT/DELETE /api/categorias/{id}/` - Detalhes de uma categoria
- `GET/POST /api/produtos/` - Listar/Criar produtos
- `GET/PUT/DELETE /api/produtos/{id}/` - Detalhes de um produto

#### **Exemplo de Uso:**
```bash
# Criar uma categoria
curl -X POST http://localhost:8001/api/categorias/ \
  -H "Content-Type: application/json" \
  -d '{"nome_categoria": "Eletrônicos"}'

# Criar um produto
curl -X POST http://localhost:8001/api/produtos/ \
  -H "Content-Type: application/json" \
  -d '{"nome_produto": "Smartphone", "categoria_id": 1}'
```

---

### 👥 2. Serviço de Pessoas (Porto 8002)

**Responsabilidade:** Gerenciar informações de pessoas/usuários do sistema.

#### **Modelos:**
```python
# pessoas/models.py
class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=100)
```

#### **APIs Disponíveis:**
- `GET/POST /api/pessoas/` - Listar/Criar pessoas
- `GET/PUT/DELETE /api/pessoas/{id}/` - Detalhes de uma pessoa

#### **Exemplo de Uso:**
```bash
# Criar uma pessoa
curl -X POST http://localhost:8002/api/pessoas/ \
  -H "Content-Type: application/json" \
  -d '{"nome_pessoa": "João Silva"}'
```

---

### 🛠️ 3. Serviço de Serviços (Porto 8003)

**Responsabilidade:** Gerenciar tipos de serviços oferecidos.

#### **Modelos:**
```python
# servicos/models.py
class Servico(models.Model):
    nome_servico = models.CharField(max_length=100)
```

#### **APIs Disponíveis:**
- `GET/POST /api/servicos/` - Listar/Criar serviços
- `GET/PUT/DELETE /api/servicos/{id}/` - Detalhes de um serviço

#### **Exemplo de Uso:**
```bash
# Criar um serviço
curl -X POST http://localhost:8003/api/servicos/ \
  -H "Content-Type: application/json" \
  -d '{"nome_servico": "Reparo"}'
```

---

### 📋 4. Serviço de Solicitações (Porto 8004) - **COORDENADOR**

**Responsabilidade:** Coordenar e agregar informações de todos os outros microsserviços.

#### **Modelos:**
```python
# solicitacoes/models.py
class SolicitarServico(models.Model):
    servico_id = models.IntegerField()      # Referência ao Serviço
    pessoa_id = models.IntegerField()       # Referência à Pessoa
    produto_id = models.IntegerField()      # Referência ao Produto
    data_solicitacao = models.DateTimeField(auto_now_add=True)
```

#### **APIs Disponíveis:**
- `GET/POST /api/solicitacoes/` - Listar/Criar solicitações
- `GET/PUT/DELETE /api/solicitacoes/{id}/` - Detalhes de uma solicitação

#### **🔥 Funcionalidade Especial - Comunicação entre Microsserviços:**

Quando você busca uma solicitação específica, o serviço automaticamente:

1. **Busca dados do Serviço** no microsserviço de Serviços
2. **Busca dados da Pessoa** no microsserviço de Pessoas  
3. **Busca dados do Produto** no microsserviço de Catálogo
4. **Agrega tudo** em uma resposta completa

```python
# solicitacoes/views.py (trecho)
def retrieve(self, request, *args, **kwargs):
    solicitacao = self.get_object()
    
    # Busca nos outros microsserviços
    url_servico = f"http://servico-servicos:8000/api/servicos/{solicitacao.servico_id}/"
    servico_data = requests.get(url_servico).json()
    
    url_pessoa = f"http://servico-pessoas:8000/api/pessoas/{solicitacao.pessoa_id}/"
    pessoa_data = requests.get(url_pessoa).json()
    
    url_produto = f"http://servico-catalogo:8000/api/produtos/{solicitacao.produto_id}/"
    produto_data = requests.get(url_produto).json()
    
    # Resposta agregada
    return Response({
        'id': solicitacao.id,
        'data_solicitacao': solicitacao.data_solicitacao,
        'servico_solicitado': servico_data,
        'solicitante': pessoa_data,
        'produto_associado': produto_data
    })
```

---

## 🐳 Docker e Containerização

### **Dockerfile Padrão (Todos os Serviços):**

```dockerfile
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala o netcat para o script entrypoint.sh funcionar
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### **Script entrypoint.sh - Sincronização de Startup:**

```bash
#!/bin/sh

# Verifica se a variável de ambiente DB_HOST foi definida
if [ -z "$DB_HOST" ]; then
  echo "Erro: A variável de ambiente DB_HOST não está definida."
  exit 1
fi

echo "Aguardando o banco de dados em: $DB_HOST"

# Loop até que a porta do PostgreSQL (5432) esteja aberta
while ! nc -z $DB_HOST 5432; do
  echo "Aguardando..."
  sleep 1
done

echo "Banco de dados conectado!"

# Execute o comando principal do contêiner
exec "$@"
```

**Função:** Garante que o Django só inicie **depois** que o PostgreSQL estiver completamente pronto.

---

## 🔧 Docker Compose - Orquestração Completa

### **Características Principais:**

#### **🌐 Rede Interna:**
```yaml
networks:
  microservico-net:
    driver: bridge
```
Todos os containers se comunicam através de uma rede privada.

#### **🔋 Health Checks:**
```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U admin -d db"]
  interval: 5s
  timeout: 5s
  retries: 5
```
Verifica se os bancos PostgreSQL estão funcionando antes de iniciar os serviços Django.

#### **⚙️ Variáveis de Ambiente:**
```yaml
environment: &api-env 
  DB_HOST: db_catalogo
  POSTGRES_DB: db
  POSTGRES_USER: admin
  POSTGRES_PASSWORD: admin
```
Configurações centralizadas e reutilizáveis.

#### **💾 Volumes Persistentes:**
```yaml
volumes:
  db_data_catalogo:
  db_data_pessoas:
  db_data_servicos:
  db_data_solicitacoes:
```
Dados dos bancos são mantidos mesmo quando os containers são recriados.

---

## 🔗 Comunicação entre Microsserviços

### **Endereços Internos do Docker:**
- `servico-catalogo:8000` - Serviço de Catálogo
- `servico-pessoas:8000` - Serviço de Pessoas
- `servico-servicos:8000` - Serviço de Serviços
- `servico-solicitacoes:8000` - Serviço de Solicitações

### **Configuração no Django:**
```python
# settings.py do serviço de solicitações
BASE_URLS = {
    "catalogo": "http://servico-catalogo:8000/api/",
    "pessoas": "http://servico-pessoas:8000/api/",
    "servicos": "http://servico-servicos:8000/api/",
}
```

### **Exemplo de Comunicação:**
```python
# Como o serviço de solicitações busca dados de outros serviços
import requests

url = f"http://servico-catalogo:8000/api/produtos/{produto_id}/"
response = requests.get(url)
produto_data = response.json()
```

---

## 🚀 Como Executar o Projeto

### **1. Pré-requisitos:**
- Docker instalado
- Docker Compose instalado
- Porto 8001-8004 disponíveis

### **2. Executar:**
```bash
# Navegar para o diretório do projeto
cd novo-projeto-microsservicos

# Subir todos os serviços
docker-compose up --build

# Ou em background
docker-compose up --build -d
```

### **3. Verificar se está funcionando:**
```bash
# Verificar status dos containers
docker-compose ps

# Ver logs de um serviço específico
docker-compose logs servico-catalogo

# Ver logs de todos os serviços
docker-compose logs
```

### **4. Acessar as APIs:**
- **Catálogo:** http://localhost:8001/api/
- **Pessoas:** http://localhost:8002/api/
- **Serviços:** http://localhost:8003/api/
- **Solicitações:** http://localhost:8004/api/

---

## 📊 Fluxo de Trabalho Completo

### **Exemplo Prático: Criar uma Solicitação Completa**

#### **1. Criar uma Categoria:**
```bash
curl -X POST http://localhost:8001/api/categorias/ \
  -H "Content-Type: application/json" \
  -d '{"nome_categoria": "Eletrônicos"}'
# Resposta: {"id": 1, "nome_categoria": "Eletrônicos"}
```

#### **2. Criar um Produto:**
```bash
curl -X POST http://localhost:8001/api/produtos/ \
  -H "Content-Type: application/json" \
  -d '{"nome_produto": "Notebook Dell", "categoria_id": 1}'
# Resposta: {"id": 1, "nome_produto": "Notebook Dell", "categoria": {...}}
```

#### **3. Criar uma Pessoa:**
```bash
curl -X POST http://localhost:8002/api/pessoas/ \
  -H "Content-Type: application/json" \
  -d '{"nome_pessoa": "Maria Santos"}'
# Resposta: {"id": 1, "nome_pessoa": "Maria Santos"}
```

#### **4. Criar um Serviço:**
```bash
curl -X POST http://localhost:8003/api/servicos/ \
  -H "Content-Type: application/json" \
  -d '{"nome_servico": "Reparo de Hardware"}'
# Resposta: {"id": 1, "nome_servico": "Reparo de Hardware"}
```

#### **5. Criar uma Solicitação (Agregando tudo):**
```bash
curl -X POST http://localhost:8004/api/solicitacoes/ \
  -H "Content-Type: application/json" \
  -d '{
    "servico_id": 1,
    "pessoa_id": 1,
    "produto_id": 1
  }'
# Resposta: {"id": 1, "servico_id": 1, "pessoa_id": 1, "produto_id": 1, "data_solicitacao": "..."}
```

#### **6. Buscar a Solicitação Completa:**
```bash
curl http://localhost:8004/api/solicitacoes/1/
```

**Resposta Agregada:**
```json
{
  "id": 1,
  "data_solicitacao": "2025-08-06T17:30:00Z",
  "servico_solicitado": {
    "id": 1,
    "nome_servico": "Reparo de Hardware"
  },
  "solicitante": {
    "id": 1,
    "nome_pessoa": "Maria Santos"
  },
  "produto_associado": {
    "id": 1,
    "nome_produto": "Notebook Dell",
    "categoria": {
      "id": 1,
      "nome_categoria": "Eletrônicos"
    }
  }
}
```

---

## 🛡️ Configurações de Segurança e Performance

### **Configurações do Django:**
```python
# settings.py
DEBUG = True                    # ⚠️ Apenas para desenvolvimento
ALLOWED_HOSTS = ['*']           # ⚠️ Apenas para desenvolvimento

# Configurações otimizadas do Docker
ENV PYTHONDONTWRITEBYTECODE 1   # Não cria arquivos .pyc
ENV PYTHONUNBUFFERED 1          # Logs aparecem imediatamente
```

### **Configurações do PostgreSQL:**
```yaml
environment:
  POSTGRES_USER: admin          # ⚠️ Trocar em produção
  POSTGRES_PASSWORD: admin      # ⚠️ Trocar em produção
  POSTGRES_DB: db
```

---

## 🎓 Conceitos Importantes Aprendidos

### **1. Arquitetura de Microsserviços:**
- ✅ **Independência** - Cada serviço tem seu próprio banco
- ✅ **Escalabilidade** - Pode escalar serviços individualmente
- ✅ **Manutenibilidade** - Alterações em um serviço não afetam outros
- ✅ **Tecnologia Diversa** - Cada serviço pode usar tecnologias diferentes

### **2. Comunicação HTTP:**
- ✅ **Comunicação Síncrona** - Usando requests HTTP
- ✅ **Descoberta de Serviços** - Usando nomes dos containers Docker
- ✅ **Tratamento de Erros** - Verificação de disponibilidade dos serviços

### **3. Containerização:**
- ✅ **Isolamento** - Cada microsserviço em seu próprio container
- ✅ **Orquestração** - Docker Compose gerencia tudo
- ✅ **Sincronização** - Scripts entrypoint garantem ordem de inicialização

### **4. API Design:**
- ✅ **REST** - Endpoints padronizados (GET, POST, PUT, DELETE)
- ✅ **Serialização** - Conversão automática entre Python e JSON
- ✅ **Agregação** - Um serviço coordena dados de outros

---

## 🔧 Comandos Úteis

### **Docker Compose:**
```bash
# Subir serviços
docker-compose up --build

# Parar serviços
docker-compose down

# Ver logs
docker-compose logs [nome-do-servico]

# Executar comandos dentro de um container
docker-compose exec servico-catalogo python manage.py shell

# Recriar apenas um serviço
docker-compose up --build servico-catalogo
```

### **Django (dentro do container):**
```bash
# Fazer migrações
docker-compose exec servico-catalogo python manage.py makemigrations
docker-compose exec servico-catalogo python manage.py migrate

# Criar superusuário
docker-compose exec servico-catalogo python manage.py createsuperuser

# Shell interativo
docker-compose exec servico-catalogo python manage.py shell
```

---

## 🚨 Solução de Problemas

### **1. Erro de Conexão com Banco:**
```
django.db.utils.OperationalError: could not connect to server
```
**Solução:** Verificar se o script `entrypoint.sh` está funcionando e se os bancos estão saudáveis.

### **2. Erro de Comunicação entre Serviços:**
```
requests.exceptions.ConnectionError
```
**Solução:** Verificar se todos os serviços estão na mesma rede Docker e se os nomes dos containers estão corretos.

### **3. Portas em Uso:**
```
ERROR: for servico-catalogo  Cannot start service
```
**Solução:** Verificar se as portas 8001-8004 estão disponíveis ou alterar no docker-compose.yml.

---

## 🎯 Próximos Passos e Melhorias

### **Para Produção:**
- [ ] **Autenticação/Autorização** - JWT, OAuth2
- [ ] **Logs Centralizados** - ELK Stack, Fluentd
- [ ] **Monitoramento** - Prometheus, Grafana
- [ ] **Load Balancer** - Nginx, HAProxy
- [ ] **Service Discovery** - Consul, Eureka
- [ ] **Circuit Breaker** - Para tolerância a falhas
- [ ] **API Gateway** - Kong, Zuul

### **Para Desenvolvimento:**
- [ ] **Testes Automatizados** - Testes unitários e de integração
- [ ] **Documentação da API** - Swagger/OpenAPI
- [ ] **CI/CD Pipeline** - GitHub Actions, Jenkins
- [ ] **Versionamento de API** - v1, v2, etc.

---

## 🎉 Conclusão

Este projeto demonstra com sucesso uma **arquitetura de microsserviços completa** usando Django e Docker. Você agora tem:

✅ **4 microsserviços independentes** comunicando-se via HTTP  
✅ **Bancos de dados isolados** para cada serviço  
✅ **Containerização completa** com Docker e Docker Compose  
✅ **APIs RESTful** padronizadas  
✅ **Comunicação entre serviços** com agregação de dados  
✅ **Sincronização de startup** com health checks  

Este é um excelente **ponto de partida** para projetos mais complexos e pode ser facilmente expandido conforme suas necessidades específicas!

---

**🔧 Criado com:** Django REST Framework + Docker + PostgreSQL  
**📅 Data:** Agosto 2025  
**👨‍💻 Status:** Projeto Completo e Funcional
