"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    pass

import os
import argparse
from nltk.corpus import stopwords
parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help = "path in the following: \usr\\\"")
args = parser.parse_args()
path = args.path
file_Object = open(path, "r")
text = file_Object.read()
stopwords = set(nltk.corpus.stopwords.words('english'))

words = text.split()
words = [word for word in words if len(word) > 1]
words = [word for word in words if not word.isnumeric()]
words = [word.lower() for word in words]
words = [word for word in words if word not in stopwords]
word_freq = []

fdist = nltk.freqdist(words)
for word, frequency in fdist.most_common(100):
    print(u'{};{}'.format(word, frequency))