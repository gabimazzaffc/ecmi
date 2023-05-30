import streamlit as st
import pandas as pd
st.title('Trabalho csv+gráfico')
st.caption('Gabriela Mazza')

df = pd.read_csv('happiness.csv', sep=',')
st.dataframe(df)

chart_data = df[['Healthy life expectancy', 'Generosity', 'Social support']]
st.line_chart(chart_data)
