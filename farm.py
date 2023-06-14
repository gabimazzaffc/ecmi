import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt

st.header('Arquivo Contas do Instagram Farm')
df = pd.read_parquet('dados_farm.parquet')
df['Post Created Date'] = pd.to_datetime(df['Post Created Date'])
df['Total Interactions'] = df['Total Interactions'].apply(lambda x: int(x.replace(',', '')))
st.dataframe(df)

st.header('Adoro farm')
df_adorofarm = df[df['User Name']=="adorofarm"]
df_adorofarm['Total Interactions'].max()
st.write(df[df['User Name'] == 'adorofarm'].sort_values(by='Total Interactions', ascending=False))

st.header('Farm rio')
df_farmrio = df[df['User Name']=="farmrio"]
df_farmrio['Total Interactions'].max() 
st.write(df[df['User Name'] == 'farmrio'].sort_values(by='Total Interactions', ascending=False))
