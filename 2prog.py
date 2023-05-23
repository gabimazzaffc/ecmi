import streamlit as st
import panda as pd
import numpy as np

st.title('Teste ECMI 2')

st.write("Tabela")

dataframe = pd.DataFrame({
  'Name': ['Josir', 'Gabi', 'Lua', 'Manu'], 
  'Salário': [10, 20, 30, 40]
})
dataframe.style.highlight_max(axis=0)

st.write(dataframe)

