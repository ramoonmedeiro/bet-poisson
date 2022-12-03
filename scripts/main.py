import numpy as np
import pandas as pd
from scipy.stats import poisson
import tools
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo arquivo excel
df = pd.read_excel('./../datasets/info_futebol.xlsx', sheet_name='info_geral', index_col='Time')

# Criando coluna de força de times
a, b = df['Pontuacao'].min(), df['Pontuacao'].max()
fa, fb = 0.15, 1 # novos limites
b1 = (fb - fa)/(b-a)
b0 = fb - b*b1
df['forca'] = round(b0 + b1*df['Pontuacao'], 3)

# Streamlit Step

rad = st.sidebar.radio('Navegue pelos itens', ['Home', 'Sobre', 'BET Jogos', 'BET Campeonato'])

if rad == 'Home':
	st.markdown(""" ##  :soccer: BET-POISSON """)
	st.markdown(""" ### Simulando jogos com base na distribuição de Poisson.""")
	st.write('Este projeto ainda está em construção e em contante mudança. Navegue pelos itens oferecidos na barra ao lado.')

if rad == 'Sobre':
	st.write('Em construção')

if rad == 'BET Jogos':
	times1 = list(df.index)
	times2 = times1.copy()
	casa, visitante = st.columns(2)
	time1 = casa.selectbox('Time Casa', times1)
	times2.remove(time1)
	time2 = visitante.selectbox('Time Visitante', times2)
	prob, matrix = tools.probabilidades_partidas(df, time1, time2)
	st.markdown('----------')

	col1, col2, col3, col4, col5 = st.columns(5)
	col1.image(df.loc[time1, 'imagem'])  
	col2.metric(time1, prob[0])
	col3.metric('Empate', prob[1])
	col4.metric(time2, prob[2]) 
	col5.image(df.loc[time2, 'imagem'])

	if st.button('Mostrar mapa de calor dos placares'):
		fig, ax = plt.subplots(figsize=(10, 5))
		sns.heatmap(matrix, vmax = 19 , annot=True, linewidth = .5, fmt=".1f")
		plt.xlabel(f'{time2}', fontsize=13)
		plt.ylabel(f'{time1}', fontsize=13)
		st.pyplot(fig)

if rad == 'BET Campeonato':
	st.write('Em construção')