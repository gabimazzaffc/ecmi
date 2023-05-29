import streamlit as st
import pandas as pd
st.title('Trabalho de programação')
st.caption('Gabriela Mazza')

df = pd.read_csv('marcas-carros.csv')
st.dataframe(df)

#arquivo = open('marcas-carros.csv')
#for linha in arquivo: 
#   st.write(linha)
