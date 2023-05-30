import streamlit as st
import pandas as pd
st.title('Trabalho csv2')
st.caption('Gabriela Mazza')

df = pd.read_csv('happiness.csv', sep=',')
st.dataframe(df)

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.happinnes(155, 3),
    columns=['Healthy life expectancy', 'Generosity', 'Social support'])

st.line_chart(happinnes)

