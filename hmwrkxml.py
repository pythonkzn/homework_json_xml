import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter

def SearchFor6digitsWords(list):
    news_str = ''
    for news in list:
        news_str += news #получили строку состоящую из новостей

    news_strs = news_str.split()
    news_strs.sort(key = len, reverse = True) #получили отстортированный список из слов от большего количества символов к меньшему
    output_list = []
    for word in news_strs:
        if len(word) >= 6:
            output_list.append(word)
    return output_list

def main():
    news = []
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    descriptions = root.findall('channel/item/description')
    for text in descriptions:
        news.append(text.text)
    output = Counter(SearchFor6digitsWords(news))#получили список слов больше 6 знаков отсортированных по убыванию знаков
    pprint(output.most_common(10))

main()
