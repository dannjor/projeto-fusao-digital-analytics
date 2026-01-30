# 5. Resultados e Próximos Passos

## Resultados Alcançados
O projeto resultou na implementação de uma pipeline de dados automatizada e funcional, capaz de integrar dados de vendas provenientes de ambientes distintos (on-premise e cloud), entregando uma base centralizada, padronizada e confiável.

Principais resultados:
- Consolidação dos dados de vendas das duas empresas em uma única fonte
- Eliminação de duplicidades e inconsistências nos indicadores
- Automatização do processo de extração, transformação e carga (ETL)
- Disponibilização dos dados prontos para análises e dashboards
- Redução de retrabalho manual na geração de relatórios

A solução permitiu maior confiabilidade na tomada de decisão e criou as bases para uma estratégia de dados unificada no cenário pós-fusão.

## Contribuições do Projeto
- Implementação de arquitetura híbrida (on-premise + cloud)
- Uso de boas práticas de engenharia de dados (camadas Bronze, Silver e Gold)
- Orquestração e automação com Apache Airflow
- Integração de múltiplas fontes (bancos de dados, API e arquivos)
- Estrutura escalável e preparada para evolução

## Próximos Passos
A solução pode ser evoluída para um ambiente produtivo com as seguintes melhorias:
- Implementação de monitoramento e alertas (Prometheus, Grafana)
- Inclusão de testes automatizados nas DAGs
- Versionamento de dados (Delta Lake, Data Vault)
- Expansão para novas fontes além de vendas
- Integração direta com dashboards no Power BI
- Migração progressiva do ambiente on-premise para cloud
- Reforço das práticas de governança, segurança e compliance (LGPD)

Esses próximos passos permitem elevar a maturidade analítica e transformar a pipeline em um ativo estratégico de dados para a organização.
