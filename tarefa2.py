import streamlit as st
import pandas as pd
import numpy as np
st.title('Trabalho csv2')
st.caption('Gabriela Mazza')

df = pd.read_csv('happiness.csv', sep=',')
st.dataframe(df)

chart_data = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['Healthy life expectancy', 'Generosity', 'Social support'])

st.line_chart(chart_data)

