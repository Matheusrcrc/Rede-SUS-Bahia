# Rede de Urgências - Bahia Dashboard

## Sobre
Dashboard interativo para análise da Rede de Urgências no Estado da Bahia, desenvolvido com Streamlit. 
O sistema permite visualizar e analisar dados sobre cobertura SAMU, atenção básica e distribuição de unidades de saúde.

## Funcionalidades
- Filtros interativos por ano e região
- Mapa de distribuição das unidades de saúde
- Gráficos de cobertura SAMU e Atenção Básica
- Métricas gerais do sistema de saúde
- Tabela detalhada com todos os indicadores

## Dados
O dashboard utiliza dados de 2013 a 2023, incluindo:
- Cobertura SAMU
- Cobertura Atenção Básica
- Número de unidades (USB, USA, UPA, PA)
- Taxa de leitos UTI
- Taxa de mortalidade por IAM

## Instalação
1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução
```bash
streamlit run app.py
```

## Estrutura do Projeto
- `app.py`: Aplicação principal
- `dados_rede_urgencias_bahia.csv`: Base de dados
- `requirements.txt`: Dependências do projeto

## Requisitos
- Python 3.8+
- Streamlit
- Pandas
- Folium
- Plotly

## Licença
MIT License

## Contato
Para dúvidas ou sugestões, entre em contato através das issues do projeto.
