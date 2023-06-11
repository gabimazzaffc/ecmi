import streamlit as st
import pandas as pd

df = pd.read_parquet('dados_farm.parquet')
df[df['User Name']== 'adorofarm'].sort_values(by=['Total Interactions'], ascending=False)
