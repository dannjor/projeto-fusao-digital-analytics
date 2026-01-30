# 4. Desenvolvimento da Solução

![Projeto Arquivos](images/projeto_arquivos.jpg)

O desenvolvimento do projeto foi organizado em etapas incrementais, seguindo uma abordagem iterativa, permitindo validações contínuas e ajustes ao longo da construção da pipeline de dados.

## Etapa 1 — Preparação dos Ambientes e Bases
- Configuração dos bancos de dados SQL Server (on-premise) e PostgreSQL (AWS RDS)
- Criação de bases de dados de vendas fictícias para simular o cenário real
- Carga inicial dos dados brutos no formato de Datalake
- Estruturação das camadas Bronze, Silver e Gold

**Resultado:**  
Bases organizadas e prontas para evolução da pipeline.

---

## Etapa 2 — Construção da Pipeline ETL
- Desenvolvimento dos processos de extração dos dados de vendas das duas empresas
- Integração com API externa para enriquecimento dos dados (cotação do dólar)
- Transformação, padronização e consolidação dos dados
- Geração da tabela final de vendas e exportação para arquivos CSV
- Upload dos dados consolidados para o Amazon S3

**Resultado:**  
Pipeline funcional integrando múltiplas fontes e entregando dados prontos para consumo analítico.

---

## Etapa 3 — Orquestração e Automação
- Configuração do ambiente Docker Compose para execução do Apache Airflow
- Conversão dos scripts de notebooks (.ipynb) para módulos Python (.py)
- Criação e configuração da DAG com as etapas de extração, transformação e carga
- Testes de execução, monitoramento e validação do fluxo completo

**Resultado:**  
Pipeline totalmente automatizada, com controle de dependências e monitoramento via Airflow.

---

## Desafios Enfrentados
- Integração entre bancos de dados heterogêneos (on-premise e cloud)
- Configuração de conectores e drivers (ODBC, APIs)
- Limitações de recursos e prazos
- Ajustes de ambiente e compatibilidade entre ferramentas

## Aprendizados
- Importância de uma arquitetura bem definida desde o início
- Valor da automação para garantir confiabilidade e escalabilidade
- Necessidade de adaptação rápida diante de mudanças de escopo
- Evolução prática em engenharia de dados e orquestração de pipelines
