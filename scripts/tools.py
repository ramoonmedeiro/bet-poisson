import numpy as np
import pandas as pd
from scipy.stats import poisson


def lambda_(df, team1, team2):
    
    #forca1 = df.loc[team1]['forca']
    #forca2 = df.loc[team2]['forca']
    forca1 = df.loc[team1]['forca'] 
    forca2 = df.loc[team2]['forca']
    
    if forca1 >= 0.8:
        forca1 = forca1
    else:
        forca1 += 0.15*forca1
    #forca1 += 0.20
    m = 2.25
    lambda1 = m*forca1/(forca2 + forca1)
    lambda2 = m - lambda1

    return [lambda1, lambda2]


def resultado_vde(gols1, gols2):

    if gols1 > gols2:
       	resultado = 'V'
    elif gols1 < gols2:
       	resultado = 'D'
    else:
       	resultado = 'E'

    return resultado


def pontos_time(gols1, gols2):
    
    resultado = resultado_vde(gols1, gols2)
    if resultado == 'V':
       	pontos1, pontos2 = 3, 0
    elif resultado == 'D':
       	pontos1, pontos2 = 0, 3
    else:
       	pontos1, pontos2 = 0, 0

    return [pontos1, pontos2, resultado]

def dist_poisson(media):

    probs = [poisson.pmf(i, media) for i in range(0, 6, 1)] # calcula a probabilidade de sair i gols quando a média = media
    probs.append(1-sum(probs)) # probabilidade de sair mais que 5 gols
    return pd.Series(probs, index = ['0', '1', '2', '3', '4', '5', '6+'])


def probabilidades_partidas(df, team1, team2):

    lambda1, lambda2 = lambda_(df, team1, team2)
    dist1, dist2 = dist_poisson(lambda1), dist_poisson(lambda2)
    matriz_resultados = np.outer(dist1, dist2) # outer produto dos valores de dist1 e dist2

    # empates
    empates = np.trace(matriz_resultados)

    # soma dos triangulos inferiores
    vitoria_team1 = np.tril(matriz_resultados).sum() - empates

    # soma dos triangulos superiores
    vitoria_team2 = np.triu(matriz_resultados).sum() - empates

    vde = np.around([vitoria_team1, empates, vitoria_team2], 3)
    probabilidades = [f'{100*i:.2f}%' for i in vde]

    return probabilidades, 100*matriz_resultados