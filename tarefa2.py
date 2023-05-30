import streamlit as st
import pandas as pd
st.title('Trabalho csv2')
st.caption('Gabriela Mazza')

df = pd.read_csv('happiness.csv', sep=',')
st.dataframe(df)

import streamlit as st
import pandas as pd
import numpy as np

st.line_chart(data= happiness, x=Healthy life expectancy, y=Generosity, use_container_width=True)
