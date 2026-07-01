import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Relatório Estratégico SST', layout='wide')
st.title('📊 Dashboard Estratégico de Vendas e Assinaturas SST')

try:
    df = pd.read_csv('base_tratada_sst.csv')
    df_sub = pd.read_csv('analise_assinatura_sst.csv')

    st.header('1. Resumo Executivo (Últimos 2 Anos)')
    col1, col2, col3 = st.columns(3)
    col1.metric('Ticket Médio (2025-2026)', 'R$ 3.894,39')
    col2.metric('Porte Predominante', 'Microempresa (56%)')
    col3.metric('Produto Líder', 'Contrato Saúde e Segurança')

    st.divider()
    st.header('2. Perfil do Cliente Ideal (ICP)')
    c1, c2 = st.columns(2)
    with c1:
        fig_porte = px.pie(df, names='Porte', title='Distribuição por Porte')
        st.plotly_chart(fig_porte, use_container_width=True)
    with c2:
        st.write('**Insights:** Base focada em Micro (56%) e Pequeno Porte (44%).')

    st.divider()
    st.header('3. Aderência de Produtos e Combos')
    st.write('**O que adicionam ao Contrato Principal:**')
    st.write('1. Renovação de Programas Legais | 2. Gestão do eSocial | 3. Serviços Técnicos')

    st.divider()
    st.header('4. Viabilidade de Assinatura')
    simulacao = df_sub[['Razao Social', 'Total_Pago', 'Qtd_Propostas', 'Mensalidade_Estimada_Base']].head(10)
    simulacao.columns = ['Cliente', 'Total Pago', 'Compras', 'Assinatura Sugerida']
    st.table(simulacao.style.format({'Total Pago': 'R$ {:.2f}', 'Assinatura Sugerida': 'R$ {:.2f}'}))

except Exception as e:
    st.error(f'Erro ao carregar dados: {e}')