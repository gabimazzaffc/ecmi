import streamlit as st
import pandas as pd
st.title('Trabalho csv2')
st.caption('Gabriela Mazza')

df = pd.read_csv('happiness.csv', sep=',')
st.dataframe(df)
df

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.happinnes(20, 3),
    columns=['Healthy life expectancy', 'Generosity', 'Social suport'])

st.line_chart(happinnes)

