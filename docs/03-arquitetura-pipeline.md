# 3. Arquitetura da Solução e Pipeline de Dados

## Visão Geral da Arquitetura
A solução foi projetada para integrar dados de vendas provenientes de ambientes heterogêneos (on-premise e cloud), garantindo escalabilidade, automação e confiabilidade no processo analítico.

A arquitetura adota uma abordagem modular, permitindo fácil manutenção, evolução e reuso dos componentes.

![Arquitetura da Pipeline](../images/arquitetura_pipeline.png)

## Fontes de Dados
- Banco de dados SQL Server (on-premise) – Empresa A
- Banco de dados PostgreSQL (AWS RDS) – Empresa B
- API externa para enriquecimento de dados (cotação do dólar)
- Arquivos CSV para armazenamento intermediário e integração com ferramentas de BI

## Camadas de Dados
A pipeline foi estruturada seguindo o conceito de camadas, garantindo organização e governança dos dados:

- **Bronze:**  
Dados brutos, extraídos diretamente das fontes, sem transformações.

- **Silver:**  
Dados tratados, padronizados, com remoção de duplicidades e ajustes de formato.

- **Gold:**  
Dados consolidados, agregados e prontos para consumo analítico e geração de KPIs.

## Orquestração e Automação
A orquestração do fluxo de dados foi realizada utilizando **Apache Airflow**, responsável por:
- Agendar execuções
- Controlar dependências entre tarefas
- Monitorar falhas e status das execuções

As DAGs seguem o fluxo:

## Infraestrutura e Deploy
- Ambiente conteinerizado com **Docker Compose**
- Apache Airflow 2.9.1 com **CeleryExecutor**
- Comunicação entre containers e bancos externos via ODBC e conectores nativos
- Arquitetura preparada para escalabilidade horizontal

## Consumo Analítico
Os dados consolidados na camada Gold são disponibilizados para:
- Dashboards no Power BI
- Relatórios gerenciais
- Análises exploratórias e tomadas de decisão estratégicas

Essa arquitetura garante uma fonte única da verdade, reduzindo inconsistências e aumentando a confiabilidade das informações.

