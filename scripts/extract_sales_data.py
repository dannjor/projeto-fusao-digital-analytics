# flake8: noqa
def executar_extracao():
    import pandas as pd
    import requests
    from db import get_postgres_engine

    def carregar_dados_api(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            dados_json = response.json()
            df = pd.DataFrame(dados_json['value'])

            df['dataHoraCotacao'] = pd.to_datetime(df['dataHoraCotacao'], errors='coerce')
            df['DataCotacao'] = df['dataHoraCotacao'].dt.date
            df_ultima_ocorrencia = df.sort_values('dataHoraCotacao') \
                                    .groupby('DataCotacao') \
                                    .tail(1).reset_index(drop=True)

            df_ultima_ocorrencia.columns = ['CotacaoCompra', 'CotacaoVenda', 'DataHoraCotacao', 'DataCotacao']
            return df_ultima_ocorrencia

        except Exception as e:
            print(f"❌ Erro ao acessar a API: {e}")
            return pd.DataFrame()

    def extrair_dados():
        try:
            print("🔄 Iniciando extração de dados...")

            engine_pg = get_postgres_engine()
            print("✅ Conexões com bancos de dados estabelecidas.")

            # Leitura dos dados
            df_b = pd.read_sql('SELECT * FROM "TB_VENDAS_EMPRESA_B_GOLD"', engine_pg)
            print(f"🔍 Leitura de TB_VENDAS_EMPRESA_B_GOLD: {len(df_b)} linhas")
            df_a = pd.read_csv('/dados_vendas_empresa_a.csv', sep=';', encoding='utf-8')
            print(f"🔍 Leitura de TB_VENDAS_EMPRESA_A_GOLD: {len(df_a)} linhas")

            # (restante igual, com prints se possível...)

        except Exception as e:
            print("❌ Erro durante a execução de extrair_dados():")
            print(e)

        # Renomeia colunas para padronizar
        colunas = ['NomeProduto', 'CategoriaProduto', 'DataVenda', 'EstadoFilial', 'ValorTotalVenda']
        df_b.columns = colunas
        df_a.columns = colunas

        # Concatena e limpa
        df_final = pd.concat([df_b, df_a], ignore_index=True)
        df_final['ValorTotalVenda'] = df_final['ValorTotalVenda'].astype('string').apply(lambda x: format(float(x), '.2f'))
        df_final.drop_duplicates(inplace=True)

        # Salva tabela unificada no SQL Server
        df_final.to_sql("TB_VENDAS_EMPRESA_A_EMPRESA_B", engine_pg, if_exists="replace", index=False)
        print("✅ Tabela TB_VENDAS_EMPRESA_A_EMPRESA_B carregada com sucesso!")

        # Carrega dados da API do dólar
        url = ("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
            "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
            "?@dataInicial='01-01-2020'&@dataFinalCotacao='07-24-2025'"
            "&$top=1400&$format=json")

        df_api = carregar_dados_api(url)

        if not df_api.empty:
            df_api.to_sql("TB_VENDAS_AUXILAR", engine_pg, if_exists="replace", index=False)
            print("✅ Cotação do dólar carregada na tabela TB_VENDAS_AUXILAR.")
        else:
            print("⚠️ Nenhum dado foi salvo da API.")

        print("🏁 Extração finalizada com sucesso.")

    # 🚀 CHAMADA REAL DA TASK
    extrair_dados()
