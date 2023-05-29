import streamlit as st

st.title('Trabalho de programação')

arquivo = open('marcas-carros.csv')
for linha in arquivo: 
   st.write(linha)
