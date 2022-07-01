import pandas as pd
import numpy as np
import streamlit as st
df = pd.DataFrame(np.random.randn(10, 3),
  columns = ('column %d' % col
    for col in range(3)))
column_left, column_right = st.beta_columns(2)
with column_left:
  st.line_chart(data = df)
with column_right:
  df
