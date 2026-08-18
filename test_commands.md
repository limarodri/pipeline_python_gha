# Comandos para Testes de Cobertura

## Pré-requisitos
Certifique-se de que seu virtual environment está ativo e as dependências estão instaladas:

```bash
# Ativar virtual environment (se não estiver ativo)
source .venv/bin/activate  # ou source venv/bin/activate

# Instalar dependências de teste
pip install pytest pytest-cov coverage httpx
```

## Comandos de Teste

### 1. Testes Simples
```bash
python -m pytest -v
```

### 2. Testes com Cobertura (Terminal)
```bash
python -m pytest --cov=. --cov-report=term-missing -v
```

### 3. Testes com Cobertura + Relatório HTML
```bash
python -m pytest --cov=. --cov-report=html --cov-report=term-missing -v
```
- Relatório gerado em: `htmlcov/index.html`

### 4. Testes com Cobertura + Relatório XML
```bash
python -m pytest --cov=. --cov-report=xml --cov-report=term-missing -v
```
- Relatório gerado em: `coverage.xml`

### 5. Testes Completos (Todos os Relatórios)
```bash
python -m pytest --cov=. --cov-report=html --cov-report=xml --cov-report=term-missing -v
```

### 6. Testes com Filtros Específicos
```bash
# Apenas testes de API
python -m pytest tests/test_main.py::TestTaskCRUD -v

# Apenas testes de health check
python -m pytest tests/test_main.py::TestHealthEndpoint -v
```

## Relatórios de Cobertura

### Terminal
- Mostra percentual de cobertura por arquivo
- Lista linhas não cobertas

### HTML (recomendado para análise detalhada)
```bash
# Gerar relatório HTML
python -m pytest --cov=. --cov-report=html -v

# Abrir relatório no navegador (macOS)
open htmlcov/index.html

# Ver apenas o relatório de cobertura
python -m coverage html
open htmlcov/index.html
```

### XML (para CI/CD)
```bash
python -m pytest --cov=. --cov-report=xml -v
```

## Comandos de Coverage Diretos

```bash
# Executar testes e gerar dados de cobertura
python -m coverage run -m pytest

# Mostrar relatório no terminal
python -m coverage report

# Gerar relatório HTML
python -m coverage html

# Gerar relatório XML
python -m coverage xml

# Apagar dados de cobertura anterior
python -m coverage erase
```

## Estrutura dos Testes

Nossos testes cobrem:
-**Health Check** endpoint
-**CRUD de Tarefas** (Create, Read, Update, Delete)
-**Filtros e Paginação**
-**Estatísticas**
-**Validação de Dados**
-**Casos de Erro**

## Análise de Cobertura

### Meta de Cobertura
- **Mínimo**: 80%
- **Ideal**: 90%+

### Arquivos Importantes
- `main.py` - API principal
- `tests/test_main.py` - Suite de testes

### Métricas Importantes
- **Statements**: Linhas de código executadas
- **Missing**: Linhas não cobertas pelos testes
- **Branches**: Caminhos condicionais testados