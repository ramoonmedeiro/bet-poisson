from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# scraping step

class ScrapeBrasileirao():

	def __init__(self, url: str):
		self.url = url

	def sup_class(self, rodada : int, tipo: str):
		r = requests.get(self.url)
		soup = BeautifulSoup(r.text, 'html.parser')
		r = soup.find_all('div', {'class':f'rodadas_grupo_A_numero_rodada_{rodada} {tipo}Rodada'})

		for tag in r:
			return tag.find_all('li', {'class': 'table__games__item'})

scrape = ScrapeBrasileirao(url='https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/')


if __name__ == '__main__':
	url = 'https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/'
	scrape = ScrapeBrasileirao(url)

	# Extrai o valor do atributo 'title' usando a propriedade ['title']
	#for i in range(1, 39, 1):
#		if i == 1:
			#tipo = 'mostrar'
		#else:
	#		tipo = 'esconder'

		#for tag in scrape.sup_class(rodada=i, tipo=tipo):
		#	title = tag.find('a')
		#	title = title['title']
		#	print(title)