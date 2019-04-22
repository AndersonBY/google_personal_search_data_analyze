# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2019-04-22 12:22:50
# @Last Modified by:   Anderson
# @Last Modified time: 2019-04-22 17:09:09
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import jieba

with open('MyActivity.html', 'r', encoding='utf-8') as f:
	content = f.read()

soup = BeautifulSoup(content, 'lxml')
items = soup.select('.content-cell')
search_list = []
for item in items:
	if str(item.text).startswith('Searched for'):
		search_list.append(item.select('a')[0].text)

with open('search_list.txt', 'w', encoding='utf-8') as f:
	f.write('\n'.join(search_list))

words_list = []
for index, text in enumerate(search_list):
	print(f'{index+1}/{len(search_list)}')
	words_list += jieba.lcut(text)
words = ' '.join(words_list)
wordcloud = WordCloud(
					font_path='msyhbd.ttc',
					background_color="white",   
					margin=5, width=1920, height=1080,
					random_state=42) 
wordcloud = wordcloud.generate(words)
wordcloud.to_file('google_personal_search_data_analyze.jpg')