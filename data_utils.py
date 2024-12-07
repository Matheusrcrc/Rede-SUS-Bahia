
import pandas as pd
import numpy as np
import os

def load_and_process_data(filename='dados_rede_urgencias_bahia.csv'):
    '''Load and process the main dataset'''
    try:
        # Verificar se o arquivo existe
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Arquivo {filename} não encontrado no diretório {os.getcwd()}")
        
        # Carregar dados
        df = pd.read_csv(filename)
        
        # Ensure numeric columns
        numeric_cols = ['cobertura_samu', 'cobertura_atencao_basica', 
                       'taxa_leitos_uti', 'taxa_mortalidade_iam']
        
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df
    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        # Criar DataFrame vazio com colunas esperadas
        return pd.DataFrame(columns=[
            'regiao', 'ano', 'cobertura_samu', 'cobertura_atencao_basica',
            'n_usb', 'n_usa', 'n_upa', 'n_pa', 'taxa_leitos_uti',
            'taxa_mortalidade_iam', 'lat', 'lon'
        ])

def calculate_metrics(df, year=None, region=None):
    '''Calculate summary metrics for selected data'''
    try:
        if year:
            df = df[df['ano'] == year]
        if region:
            df = df[df['regiao'].isin(region) if isinstance(region, list) else df['regiao'] == region]
        
        metrics = {
            'total_usb': df['n_usb'].sum() if 'n_usb' in df.columns else 0,
            'total_usa': df['n_usa'].sum() if 'n_usa' in df.columns else 0,
            'total_upa': df['n_upa'].sum() if 'n_upa' in df.columns else 0,
            'total_pa': df['n_pa'].sum() if 'n_pa' in df.columns else 0,
            'media_cobertura_samu': df['cobertura_samu'].mean() if 'cobertura_samu' in df.columns else 0,
            'media_cobertura_ab': df['cobertura_atencao_basica'].mean() if 'cobertura_atencao_basica' in df.columns else 0
        }
        
        return metrics
    except Exception as e:
        print(f"Erro ao calcular métricas: {str(e)}")
        return {
            'total_usb': 0, 'total_usa': 0, 'total_upa': 0, 'total_pa': 0,
            'media_cobertura_samu': 0, 'media_cobertura_ab': 0
        }
