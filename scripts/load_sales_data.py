# flake8: noqa
def executar_carga():
    import os
    import pandas as pd
    from db import get_postgres_engine
    import boto3

    def extrair_dados(engine_postgres):
        try:
            print("🔄 Iniciando extração de dados...")
            df = pd.read_sql('SELECT * FROM "TB_VENDAS_FINAL"', engine_postgres)
            df['CotacaoDolar'] = df['CotacaoDolar'].round(2).astype(float)
            return df
        except Exception as e:
                print("❌ Erro durante a execução de extrair_dados():")
                print(e)

    def salvar_csv(df, caminho_arquivo):
        try:
            print("🔄 Iniciando o salve do dataframe em csv...")
            os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
            df.to_csv(caminho_arquivo, index=False, sep=';')
        except Exception as e:
                print("❌ Erro durante a execução de salvar_csv():")
                print(e)

    def enviar_para_s3(caminho_arquivo, bucket_name, caminho_destino_s3, aws_access_key_id, aws_secret_access_key, region_name='us-east-1'):
        try:
            print("🔄 Iniciando o envio do arquivo para o bucket...")
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=region_name
            )
            with open(caminho_arquivo, 'rb') as f:
                s3_client.upload_fileobj(f, bucket_name, caminho_destino_s3)
        except Exception as e:
                print("❌ Erro durante a execução de enviar_para_s3():")
                print(e)
                
    def executar_load():
        engine_postgres = get_postgres_engine()
        caminho_local = '/dados_vendas_final.csv'
        bucket_s3 = 'my-bucket-jc-01'
        caminho_s3 = 'data_processed/dados_vendas_final.csv'

        df = extrair_dados(engine_postgres)
        salvar_csv(df, caminho_local)

        enviar_para_s3(
            caminho_local,
            bucket_s3,
            caminho_s3,
            aws_access_key_id='',
            aws_secret_access_key='',
            region_name='us-east-1'
        )
        
        print("✅ Arquivo exportado com sucesso para o diretório local e para o S3.")

    executar_load()

