import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt

st.header('Arquivo Contas do Instagram do Grupo Soma')
df = pd.read_parquet('dados_farm.parquet')
df['Post Created Date'] = pd.to_datetime(df['Post Created Date'])
df['Total Interactions'] = df['Total Interactions'].apply(lambda x: int(x.replace(',', '')))
st.dataframe(df)

df_adorofarm = df[df['User Name']=="adorofarm"]
df_farmrio = df[df['User Name']=="farmrio"]

st.write(df[df['User Name'] == 'farmrio'].sort_values(by='Total Interactions', ascending=False))
