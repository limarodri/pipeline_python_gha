# DevOps Automation - Task Manager
Um aplicativo moderno de gerenciamento de tarefas desenvolvido com **FastAPI** e **Frontend responsivo**, ideal para demonstrações de **CI/CD** e **práticas DevOps** em laboratórios de automação.
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-yellow)
## Funcionalidades
### Backend API (FastAPI)
- **CRUD completo** para tarefas
- **Dashboard de estatísticas**
- **Filtros avançados** (status, prioridade, busca)
- **Paginação** automática
- **Health checks** para monitoramento
- **Documentação automática** (Swagger/OpenAPI)
### Frontend Moderno
- **Interface responsiva** com gradientes modernos
- **Interações dinâmicas** com animações CSS
- **Mobile-friendly** design
- **Cards animados** com hover effects
- **Dashboard visual** com estatísticas em tempo real
- **Atualização automática** de dados
### DevOps Ready
- **Docker** containerização completa
- **GitHub Actions** CI/CD pipeline
- **Testes automatizados** (unitários + integração)
- **Load testing** com Locust
- **Security scanning** integrado
- **Multi-architecture builds**
## Quick Start
### Desenvolvimento Local
```bash
# Clonar o repositório
git clone <repository-url>
cd task-manager
# Instalar dependências
pip install -r requirements.txt
# Executar a aplicação
python main.py
# ou
uvicorn main:app --reload
# Acessar aplicação
open http://localhost:8000
```
### Docker
```bash
# Build da imagem
docker build -t task-manager .
# Executar container
docker run -p 8000:8000 task-manager
# Ou usar docker-compose
docker-compose up
```
### Executar Testes
```bash
# Testes simples
python -m pytest -v
# Testes com cobertura no terminal
python -m pytest --cov=. --cov-report=term-missing -v
# Testes com cobertura + relatório HTML
python -m pytest --cov=. --cov-report=html --cov-report=term-missing -v
# Abrir relatório: open htmlcov/index.html
# Testes completos (HTML + XML)
python -m pytest --cov=. --cov-report=html --cov-report=xml --cov-report=term-missing -v
# Testes de performance
locust -f .github/workflows/locustfile.py --host http://localhost:8000
```
**Análise de Cobertura:**
- Relatório HTML: `htmlcov/index.html`
- Relatório XML: `coverage.xml`
- Meta de cobertura: 90%+
## API Endpoints
### Core Endpoints
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Interface web principal |
| `GET` | `/api/health` | Health check do sistema |
| `GET` | `/api/docs` | Documentação Swagger |
### Tasks Management
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/tasks` | Listar todas as tarefas |
| `POST` | `/api/tasks` | Criar nova tarefa |
| `GET` | `/api/tasks/{id}` | Obter tarefa específica |
| `PUT` | `/api/tasks/{id}` | Atualizar tarefa |
| `DELETE` | `/api/tasks/{id}` | Deletar tarefa |
| `GET` | `/api/stats` | Estatísticas das tarefas |
### Query Parameters
```bash
# Filtros
GET /api/tasks?completed=true&priority=high&skip=0&limit=10
# Busca
GET /api/tasks?search=importante
```
## Arquitetura
```
├── main.py              #  FastAPI application
├── requirements.txt     #  Python dependencies
├── Dockerfile          #  Container configuration
├── docker-compose.yml  #  Multi-service setup
├── pytest.ini         #  Test configuration
├── static/             #  Frontend assets
│   ├── index.html      #  Main page
│   ├── style.css       #  Modern styling
│   └── script.js       #  Interactive features
├── tests/              #  Test suite
│   └── test_main.py    #  Comprehensive tests
└── .github/
└── workflows/
├── ci-cd.yml   #  CI/CD pipeline
└── locustfile.py #  Performance tests
```
##  CI/CD Pipeline
### Workflow Stages
1. ** Lint & Code Quality**
- Black (formatação)
- isort (imports)
- Flake8 (linting)
2. ** Testing Matrix**
- Python 3.9, 3.10, 3.11
- Testes unitários + cobertura
- Upload para Codecov
3. ** Security Scanning**
- Safety (vulnerabilidades)
- Bandit (security linting)
4. **Build & Push**
- Multi-arch Docker builds
- Push para Docker Hub
- Cache otimizado
5. ** Integration Tests**
- Testes end-to-end
- Validação de API
- Frontend accessibility
6. ** Performance Tests**
- Load testing com Locust
- Métricas de performance
7. ** Deployment**
- Staging (branch develop)
- Production (branch main)
### Configuração de Secrets
```bash
# GitHub Secrets necessários
DOCKERHUB_USERNAME=seu_usuario
DOCKERHUB_TOKEN=seu_token
```
##  Monitoramento
### Health Checks
```bash
# Status da aplicação
curl http://localhost:8000/api/health
# Estatísticas
curl http://localhost:8000/api/stats
```
### Métricas Disponíveis
- **Total de tarefas**
- **Tarefas concluídas/pendentes**
- **Distribuição por prioridade**
- **Response times**
- **Error rates**
##  Frontend Features
### UI Components
- **Dashboard Cards** com estatísticas animadas
- **Modal Forms** para criação/edição
- **Filtros Dinâmicos** em tempo real
- **Animações CSS** suaves
- **Design Responsivo**
### User Experience
- **Loading states** visuais
- **Notificações** toast
- **Auto-save** indicators
- **Hover effects** interativos
- **Drag & drop** (futuro)
##  Testes
### Test Coverage
- **Unit Tests**: API endpoints
- **Integration Tests**: E2E workflows
- **Performance Tests**: Load testing
- **Security Tests**: Vulnerability scanning
### Test Categories
```python
# Exemplos de testes incluídos
- test_create_task()
- test_update_task()
- test_filter_tasks()
- test_task_stats()
- test_health_check()
- test_security_headers()
```
##  Roadmap
### Próximas Features
- [ ] **Autenticação JWT**
- [ ] **Multi-usuário**
- [ ] **Due dates** e lembretes
- [ ] **Tags** e categorias
- [ ] **Analytics** avançados
- [ ] **Real-time updates** (WebSocket)
- [ ] **PWA** support
- [ ] **Internacionalização**
### **Infrastructure**
- [ ] **Kubernetes** deployment
- [ ] **Prometheus** monitoring
- [ ] **Grafana** dashboards
- [ ] **PostgreSQL** production DB
- [ ] **CDN** integration
##  Contribuindo
1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/amazing-feature`)
3. Commit suas mudanças (`git commit -m 'Add amazing feature'`)
4. Push para a branch (`git push origin feature/amazing-feature`)
5. Abra um Pull Request
##  Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
##  Agradecimentos
- **FastAPI** pela excelente framework
- **GitHub Actions** pela plataforma CI/CD
- **Docker** pela containerização
- **Locust** pelos testes de performance
--- **DevOps Automation - Feito para demonstrações de CI/CD e GitHub Actions**