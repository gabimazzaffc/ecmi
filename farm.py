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
df_adorofarm_mais2019 = df[df['User Name'] == 'adorofarm'].query('`Post Created Date` >= "2019-01-01" and `Post Created Date` <= "2023-05-01"')
df_adorofarm_mais2019_interactions = df_adorofarm_mais2019.groupby('Post Created Date')['Total Interactions'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_adorofarm_mais2019_interactions, x='Post Created Date', y='Total Interactions').set(title='Total de interações - adorofarm')



















#df_farmrio = df[df['User Name']=="farmrio"]

#st.write(df[df['User Name'] == 'farmrio'].sort_values(by='Total Interactions', ascending=False))
