from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# scraping step
url = 'https://ge.globo.com/sp/campinas-e-regiao/futebol/campeonato-paulista/noticia/2022/11/16/paulistao-2023-fpf-divulga-tabela-veja-a-ordem-dos-jogos.ghtml'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
itens = soup.find_all('ul', class_='content-unordered-list')
partidas = []
for i in range(0, 12, 1):	
	for jogo in itens[i].find_all('li'):
		partidas.append(jogo.get_text().split(' x '))

# Dataframe Step

time1 = [time[0] for time in partidas]
time2 = [time[1] for time in partidas]
d = {'Time1': time1, 'Time2': time2}
df_jogos = pd.DataFrame(data=d)

df_jogos.to_excel('./../datasets/info_futebol.xlsx', sheet_name='jogos_totais')