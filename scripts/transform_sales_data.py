# flake8: noqa
def executar_transformacao():
    import pandas as pd
    from db import get_postgres_engine

    # --- Etapa 1: Função para extrair dados do Postgres
    def extract_sales_data(engine_postgres):
        query = """
            SELECT 
            E."NomeProduto",
            E."CategoriaProduto",
            CAST(E."DataVenda" AS DATE) AS "DataVenda",
            E."EstadoFilial",
            E."ValorTotalVenda",
            COALESCE (A."CotacaoVenda", (SELECT MAX("CotacaoVenda") FROM "TB_VENDAS_AUXILAR")) AS "CotacaoDolar"
            FROM "TB_VENDAS_EMPRESA_A_EMPRESA_B" AS E
            LEFT JOIN "TB_VENDAS_AUXILAR" AS A ON CAST(A."DataCotacao" AS VARCHAR(10)) = E."DataVenda"
        """
        return pd.read_sql(query, engine_postgres)

    # --- Etapa 2: Função para carregar dados
    def load_data(df, engine, table_name="TB_VENDAS_FINAL"):
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"✅ Dados carregados com sucesso na tabela {table_name}!")
        
    def executar_transf():  
        engine_postgres = get_postgres_engine()
        print("📤 Carregando dados no Postgres...")
        df = extract_sales_data(engine_postgres)
        load_data(df, engine_postgres)
        print("✅ Pipeline concluído com sucesso!")

    executar_transf()