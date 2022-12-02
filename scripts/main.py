import numpy as np
import pandas as pd
from scipy.stats import poisson
import tools

# Lendo arquivo excel
df = pd.read_excel('./info_futebol.xlsx', sheet_name='info_geral', index_col='Time')


# Criando coluna de força de times
a, b = df['Pontuação'].min(), df['Pontuação'].max()
fa, fb = 0.3, 1 # novos limites
b1 = (fb - fa)/(b-a)
b0 = fb - b*b1
df['forca'] = round(b0 + b1*df['Pontuação'], 3)


prob, matrix = tools.probabilidades_partidas('São Paulo', 'Ferroviário')
print(prob)
print(matrix)