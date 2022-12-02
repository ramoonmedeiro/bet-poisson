import numpy as np
import pandas as pd
from scipy.stats import poisson
import tools
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo arquivo excel
df = pd.read_excel('../datasets/info_futebol.xlsx', sheet_name='info_geral', index_col='Time')

# Criando coluna de força de times
a, b = df['Pontuação'].min(), df['Pontuação'].max()
fa, fb = 0.3, 1 # novos limites
b1 = (fb - fa)/(b-a)
b0 = fb - b*b1
df['forca'] = round(b0 + b1*df['Pontuação'], 3)


prob, matrix = tools.probabilidades_partidas(df, 'São Paulo', 'Ferroviária')

# Streamlit Step

st.markdown(""" ##  :soccer: BET-POISSON """)
st.write('Simulando jogos com base na distribuição de Poisson.')

if st.button('Aperte aqui'):
	st.write('Valeu')

name = st.text_input('Nome')
st.write(name)

time1 = st.selectbox('Time 1', ['São Paulo', 'Palmeiras', 'Santos'])
time2 = st.selectbox('Time 2', ['São Paulo', 'Palmeiras', 'Santos'])
#add = st.text_area('Endereço')
#st.dataframe(matrix)
#st.table(matrix)

#fig, ax = plt.subplots(figsize=(10, 5))
#sns.heatmap(matrix, vmax = 19 , annot=True, linewidth = .5, fmt=".1f")
#st.pyplot(fig)