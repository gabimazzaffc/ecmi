import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

st.caption('Gabriela Mazza - A2')
st.header('Arquivo Contas do Instagram do Grupo Soma')
df = pd.read_parquet('dados_gruposoma.parquet')
df['Post Created Date'] = pd.to_datetime(df['Post Created Date'])
df['Total Interactions'] = df['Total Interactions'].apply(lambda x: int(x.replace(',', '')))
# df['Post Created'] = pd.to_datetime(df['Post Created'], format='mixed')

with st.sidebar:
    st.title('Marca + Ano')
    marca_sidebar = st.selectbox('Escolha uma marca para analisar:', ['bynv', 'adorofarm', 'foxtonbrasil', 'hering_oficial', 'animalebrasil', 'mariafilo'])
    ano_sidebar = st.number_input('Escolha um ano', min_value=2019, max_value=2022, value=2021)

st.dataframe(df)

st.header('O post com mais interação de cada marca')
max_interactions = df.groupby('Account')['Total Interactions'].max()
resultado = df[df['Total Interactions'].isin(max_interactions)]
st.write(resultado)

st.header('Posts com maior número de interações de uma marca')
st.write(df[df['User Name'] == marca_sidebar].sort_values(by='Total Interactions', ascending=False))


def grafico_interativo_interacoes(df, username, ano):
    if type(ano) != str: 
        ano = str(ano) 
    usuario = df[df['User Name'] == username].query('`Post Created Date` >= "' + ano + '-01-01" and `Post Created Date` <= "' + ano + '-12-31"')
    usuario_followers = usuario.groupby('Post Created Date')['Followers at Posting'].mean().reset_index()
    usuario_interactions = usuario.groupby('Post Created Date')['Total Interactions'].sum().reset_index() 
    interacao = alt.Chart(usuario_interactions).mark_line().encode(x='Post Created Date', y='Total Interactions', tooltip=['Post Created Date', 'Total Interactions'])
    follower = alt.Chart(usuario_followers).mark_line().encode(x='Post Created Date', y='Followers at Posting', tooltip=['Post Created Date', 'Followers at Posting'])
    return interacao & follower

st.header('Análise de interações e seguidores')
#st.markdown('análise de interações e seguidores')
st.header('Gráficos')
st.altair_chart(grafico_interativo_interacoes(df, marca_sidebar, ano_sidebar), use_container_width=True)


st.header('Crescimento percentual de interações por conta')
df['Ano'] = df['Post Created Date'].dt.year
df['Ano'] = df['Ano'].astype(int)
df['Mes'] = df['Post Created Date'].dt.month
df['Semana'] = df['Post Created Date'].dt.isocalendar().week

media_interactions_ano = df.groupby(['Account', 'Ano'])['Total Interactions'].mean().reset_index().sort_values(by=['Account', 'Ano'])
media_interactions_ano['Interactions Growth'] = media_interactions_ano.groupby('Account')['Total Interactions'].pct_change()

st.altair_chart(alt.Chart(media_interactions_ano).mark_line().encode(x='Ano', y='Interactions Growth', color='Account', tooltip=['Account', 'Ano', 'Interactions Growth']).interactive(), use_container_width=True)

st.header('Média de interações por ano')
st.altair_chart(alt.Chart(media_interactions_ano).mark_line().encode(x='Ano', y='Total Interactions', color='Account', tooltip=['Account', 'Ano', 'Interactions Growth']).interactive(), use_container_width=True)

