import pandas as pd

df = pd.read_parquet('dados_gruposoma.parquet')



df['Post Created Date'] = pd.to_datetime(df['Post Created Date'])
# df['Post Created'] = pd.to_datetime(df['Post Created'].str[:-4], format='%Y-%m-%d %H:%M:%S').dt.tz_localize('America/Sao_Paulo')
df
df['Mês'] = df['Post Created Date'].dt.month
df['Ano'] = df['Post Created Date'].dt.year
media_interactions_ano = pd.DataFrame({
   'Account': media_interactions_ano['Account'],
   'Interactions Growth': media_interactions_ano['Interactions Growth']
})

st.line_chart(data=media_interactions_ano, x='Account', y='Interactions Growth', use_container_width=True)

import streamlit as st
import pandas as pd
import numpy as np

media_interactions_ano = pd.DataFrame(
   media_interactions_ano('Ano', 'Interactions Growth'),
    columns=['Account'])


st.line_chart(data=media_interactions_ano, x='Ano', y='Total Interactions', use_container_width=True)
