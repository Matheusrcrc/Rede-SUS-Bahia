
import pandas as pd
import numpy as np
import os

def load_and_process_data():
    '''Load and process the main dataset'''
    try:
        # Carregar dados
        df = pd.read_csv('dados_rede_urgencias_bahia.csv')
        
        # Ensure numeric columns
        numeric_cols = ['cobertura_samu', 'cobertura_atencao_basica', 
                       'taxa_leitos_uti', 'taxa_mortalidade_iam',
                       'n_usb', 'n_usa', 'n_upa', 'n_pa']
        
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df
    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        return pd.DataFrame()

def calculate_metrics(df, year=None, region=None):
    '''Calculate summary metrics for selected data'''
    try:
        if year:
            df = df[df['ano'] == year]
        if region:
            df = df[df['regiao'].isin(region) if isinstance(region, list) else df['regiao'] == region]
        
        metrics = {
            'total_usb': int(df['n_usb'].sum()),
            'total_usa': int(df['n_usa'].sum()),
            'total_upa': int(df['n_upa'].sum()),
            'total_pa': int(df['n_pa'].sum()),
            'media_cobertura_samu': round(df['cobertura_samu'].mean(), 2),
            'media_cobertura_ab': round(df['cobertura_atencao_basica'].mean(), 2)
        }
        
        return metrics
    except Exception as e:
        print(f"Erro ao calcular métricas: {str(e)}")
        return {
            'total_usb': 0, 'total_usa': 0, 'total_upa': 0, 'total_pa': 0,
            'media_cobertura_samu': 0, 'media_cobertura_ab': 0
        }
