import streamlit as st
import pandas as pd

df = pd.read_parquet('dados_gruposoma.parquet')
df['Post Created Date'] = pd.to_datetime(df['Post Created Date'])
# df['Post Created'] = pd.to_datetime(df['Post Created'].str[:-4], format='%Y-%m-%d %H:%M:%S').dt.tz_localize('America/Sao_Paulo')

max_interactions = df.groupby('Account')['Total Interactions'].max()
resultado = df[df['Total Interactions'].isin(max_interactions)]
st.write(resultado)


df['Mês'] = df['Post Created Date'].dt.month
df['Ano'] = df['Post Created Date'].dt.year
media_interactions_mes_ano = df.groupby(['Account','Ano'])['Total Interactions'].mean().reset_index().sort_values(by=['Account', 'Ano'])
media_interactions_mes_ano['Interactions Growth'] = media_interactions_mes_ano.groupby('Account')['Total Interactions'].transform(lambda x: x.pct_change())
media_interactions_ano = df.groupby(['Account', 'Ano'])['Total Interactions'].mean().reset_index().sort_values(by=['Account', 'Ano'])
media_interactions_ano['Interactions Growth'] = media_interactions_ano.groupby('Account')['Total Interactions'].pct_change()

chart_data = df[[ 'Ano', 'Interactions Growth']]
st.line_chart(chart_data)
