import pandas as pd

df = pd.read_parquet('dados_gruposoma.parquet')
df

df['Post Created Date'] = pd.to_datetime(df['Post Created Date'])
df['Post Created'] = pd.to_datetime(df['Post Created'].str[:-4], format='%Y-%m-%d %H:%M:%S').dt.tz_localize('America/Sao_Paulo')

df['Mês'] = df['Post Created Date'].dt.month
df['Ano'] = df['Post Created Date'].dt.year
media_interactions_mes_ano = df.groupby(['Account', 'Mês','Ano'])['Total Interactions'].mean().reset_index().sort_values(by=['Account', 'Ano', 'Mês'])
media_interactions_mes_ano['Interactions Growth'] = media_interactions_mes_ano.groupby('Account')['Total Interactions'].transform(lambda x: x.pct_change())
media_interactions_ano = df.groupby(['Account', 'Ano'])['Total Interactions'].mean().reset_index().sort_values(by=['Account', 'Ano'])
media_interactions_ano['Interactions Growth'] = media_interactions_ano.groupby('Account')['Total Interactions'].pct_change()

import streamlit as st
import pandas as pd
import numpy as np

st.line_chart(media_interactions_ano)