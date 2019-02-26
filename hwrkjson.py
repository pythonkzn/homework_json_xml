import json
from pprint import pprint
from collections import Counter

def SearchFor6digitsWords(dict_json):
    news_str = ''
    for news in dict_json['rss']['channel']['items']:
        news_str += news['description'] #получили строку состоящую из новостей

    news_strs = news_str.split()
    news_strs.sort(key = len, reverse = True) #получили отстортированный список из слов от большего количества символов к меньшему
    output_list = []
    for word in news_strs:
        if len(word) >= 6:
            output_list.append(word)
    return output_list

def main():
    with open('newsafr.json', encoding ='utf-8') as json_file:
        news = json.load(json_file)
    output = Counter(SearchFor6digitsWords(news))#получили список слов больше 6 знаков отсортированных по убыванию знаков
    pprint(output.most_common(10))

main()
