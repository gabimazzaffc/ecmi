import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_parquet('dados_gruposoma.parquet')
df['Post Created Date'] = pd.to_datetime(df['Post Created Date'])
# df['Post Created'] = pd.to_datetime(df['Post Created'].str[:-4], format='%Y-%m-%d %H:%M:%S').dt.tz_localize('America/Sao_Paulo')


def plot_interacoes_followers(df, username, ano):
    if type(ano) != str:
        ano = str(ano)
    usuario = df[df['User Name'] == username].query('`Post Created Date` >= "' + ano + '-01-01" and `Post Created Date` <= "' + ano + '-12-31"')
    usuario_interactions = usuario.groupby('Post Created Date')['Total Interactions'].sum().reset_index()
    usuario_followers = usuario.groupby('Post Created Date')['Followers at Posting'].mean().reset_index()
    fig, axes = plt.subplots(2,1, sharex=True, figsize=(18,18))
    fig.suptitle('Interações e Seguidores - ' + username + ' - ' + ano)
    sns.lineplot(ax=axes[0], data=usuario_interactions, x='Post Created Date', y='Total Interactions').set(title='Total de interações por dia - ' + username)
    sns.lineplot(ax=axes[1], data=usuario_followers, x='Post Created Date', y='Followers at Posting').set(title='Followers por dia - ' + username)
    st.pyplot(fig)
    
plot_interacoes_followers(df, 'bynv', '2021')





#chart_data = df[[ 'Ano', 'Interactions Growth']]
#st.line_chart(chart_data)
