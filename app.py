
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_folium import folium_static
import os

# Import custom modules
from data_utils import load_and_process_data, calculate_metrics
from map_utils import create_base_map, add_health_unit_markers, add_heatmap

# Page config
st.set_page_config(
    page_title='Rede de Urgências - Bahia',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS
st.markdown('''
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    ''', unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        return load_and_process_data()
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        st.error(f"Diretório atual: {os.getcwd()}")
        st.error(f"Arquivos disponíveis: {os.listdir()}")
        return pd.DataFrame()  # Return empty DataFrame

df = load_data()

if df.empty:
    st.error("Não foi possível carregar os dados. Por favor, verifique se o arquivo existe e está acessível.")
    st.stop()

# Sidebar filters
st.sidebar.header('Filtros')
selected_year = st.sidebar.selectbox('Ano', sorted(df['ano'].unique()))
selected_region = st.sidebar.multiselect('Região', df['regiao'].unique())

# Filter data
if selected_region:
    df_filtered = df[(df['ano'] == selected_year) & (df['regiao'].isin(selected_region))]
else:
    df_filtered = df[df['ano'] == selected_year]

# Title
st.title('Rede de Urgências - Bahia')
st.markdown('---')

# Metrics
metrics = calculate_metrics(df_filtered)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('USB', metrics['total_usb'])
with col2:
    st.metric('USA', metrics['total_usa'])
with col3:
    st.metric('UPA', metrics['total_upa'])
with col4:
    st.metric('PA', metrics['total_pa'])

# Coverage graphs
if not df_filtered.empty:
    st.subheader('Indicadores de Cobertura')
    col1, col2 = st.columns(2)

    with col1:
        fig_samu = px.bar(
            df_filtered,
            x='regiao',
            y='cobertura_samu',
            title='Cobertura SAMU por Região',
            labels={'cobertura_samu': 'Cobertura SAMU (%)', 'regiao': 'Região'}
        )
        st.plotly_chart(fig_samu, use_container_width=True)

    with col2:
        fig_ab = px.bar(
            df_filtered,
            x='regiao',
            y='cobertura_atencao_basica',
            title='Cobertura da Atenção Básica por Região',
            labels={'cobertura_atencao_basica': 'Cobertura AB (%)', 'regiao': 'Região'}
        )
        st.plotly_chart(fig_ab, use_container_width=True)

    # Map
    st.subheader('Distribuição das Unidades de Saúde')
    map_type = st.radio('Tipo de Visualização', ['Marcadores', 'Mapa de Calor'])

    m = create_base_map()
    if map_type == 'Marcadores':
        m = add_health_unit_markers(m, df_filtered)
    else:
        m = add_heatmap(m, df_filtered)

    folium_static(m, width=1200)

    # Detailed data
    st.subheader('Dados Detalhados')
    if st.checkbox('Mostrar dados completos'):
        st.dataframe(df_filtered)
else:
    st.warning("Nenhum dado disponível para os filtros selecionados.")

# Footer
st.markdown('---')
st.markdown('Desenvolvido com Streamlit - Dados da Rede de Urgências da Bahia')
