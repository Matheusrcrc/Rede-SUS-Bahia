
import pandas as pd
import numpy as np

def load_and_process_data(filename='dados_rede_urgencias_bahia.csv'):
    '''Load and process the main dataset'''
    df = pd.read_csv(filename)
    
    # Ensure numeric columns
    numeric_cols = ['cobertura_samu', 'cobertura_atencao_basica', 
                   'taxa_leitos_uti', 'taxa_mortalidade_iam']
    
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

def calculate_metrics(df, year=None, region=None):
    '''Calculate summary metrics for selected data'''
    if year:
        df = df[df['ano'] == year]
    if region:
        df = df[df['regiao'].isin(region) if isinstance(region, list) else df['regiao'] == region]
    
    metrics = {
        'total_usb': df['n_usb'].sum(),
        'total_usa': df['n_usa'].sum(),
        'total_upa': df['n_upa'].sum(),
        'total_pa': df['n_pa'].sum(),
        'media_cobertura_samu': df['cobertura_samu'].mean(),
        'media_cobertura_ab': df['cobertura_atencao_basica'].mean()
    }
    
    return metrics
