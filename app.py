import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title='Dashboard Comercial SST', layout='wide')

st.title('📊 Dashboard de Vendas e Assinaturas SST')

# Carregar dados
try:
    df = pd.read_csv('base_tratada_sst.csv')

    # Sidebar Filtros
    st.sidebar.header('Filtros')
    porte_options = df['Porte'].unique().tolist()
    porte = st.sidebar.multiselect('Selecione o Porte:', porte_options, default=porte_options)

    # Filtragem
    df_filtered = df[df['Porte'].isin(porte)]

    # KPIs Principais
    col1, col2, col3 = st.columns(3)
    receita_total = df_filtered['Valor total'].sum()
    ticket_medio = df_filtered['Valor total'].mean()
    
    col1.metric('Receita Total', f'R$ {receita_total:,.2f}')
    col2.metric('Qtd Propostas', len(df_filtered))
    col3.metric('Ticket Médio', f'R$ {ticket_medio:,.2f}')

    # Gráficos
    col_left, col_right = st.columns(2)
    
    with col_left:
        fig1 = px.pie(df_filtered, names='Porte', title='Distribuição por Porte')
        st.plotly_chart(fig1, use_container_width=True)

    with col_right:
        fig2 = px.bar(df_filtered.groupby('Status')['Valor total'].sum().reset_index(), 
                      x='Status', y='Valor total', title='Receita por Status')
        st.plotly_chart(fig2, use_container_width=True)

except FileNotFoundError:
    st.error('ERRO: Arquivo base_tratada_sst.csv não encontrado. Suba o arquivo CSV para o GitHub!')