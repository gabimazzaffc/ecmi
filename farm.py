import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt

st.header('Arquivo Contas do Instagram Farm')
df = pd.read_parquet('dados_farm.parquet')
df['Post Created Date'] = pd.to_datetime(df['Post Created Date'])
df['Total Interactions'] = df['Total Interactions'].apply(lambda x: int(x.replace(',', '')))
st.dataframe(df)

df_adorofarm = df[df['User Name']=="adorofarm"]
df_adorofarm['Total Interactions'].max()
st.write(df[df['User Name'] == 'adorofarm'].sort_values(by='Total Interactions', ascending=False))

def grafico_interativo_interacoes(df, username, ano):
    if type(ano) != str: 
        ano = str(ano) 
    usuario = df[df['User Name'] == 'adorofarm'].query('`Post Created Date` >= "' + ano + '-01-01" and `Post Created Date` <= "' + ano + '-12-31"')
    usuario_interactions = usuario.groupby('Post Created Date')['Total Interactions'].sum().reset_index() 
    
st.header('Gráficos')
st.altair_chart(grafico_interativo_interacoes(df, adorofarm, '2019'), use_container_width=True)

    

















#df_farmrio = df[df['User Name']=="farmrio"]

#st.write(df[df['User Name'] == 'farmrio'].sort_values(by='Total Interactions', ascending=False))
