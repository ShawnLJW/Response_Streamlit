from autocorrect import Speller
from nltk import download
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
import re

download('stopwords')
download('punkt')
download('averaged_perceptron_tagger')
download('wordnet')

newWords = ['youre','u','ur','really','sector','industry','be','being','related','else','xd','probably','work','something','sure','yet','interested','either']
no_spell_check = ['raffle','raffles','eunoia','lasalle','chong','asrjc']
cStopwords = stopwords.words('english')
cStopwords += newWords
stemmer = SnowballStemmer("english")
lem = WordNetLemmatizer()
spell = Speller()
punc = re.compile(r"[^a-zA-Z0-9 ]+")

def removePunc(i):
    i = re.sub(r"[.,?!:;]", ' ', i)
    i = punc.sub(' ', i)
    return i

def findKeywords(i):
    try:
        i = removePunc(i)
        i = word_tokenize(i)
        i = pos_tag(i)
        kw = []
        for word,tag in i:
            if word == 'IT':
                kw.append('technology')
            word = word.lower()
            if word[:3] == 'las':
                word = 'lasalle'
            if word not in no_spell_check and len(word)>4:
                word = spell(word)
            if word == 'tech':
                kw.append('technology')
            elif word == 'media':
                kw.append('media')
            elif word not in cStopwords:
                kw.append(lem.lemmatize(word, pos=tag[0].lower() if tag[0].lower() in 'arnv' else 'n'))
        return kw
    except TypeError:
        return []

def find_root_words(i):
    try:
        i = removePunc(i)
        i = word_tokenize(i)
        kw = []
        for word in i:
            if word == 'IT':
                kw.append('technolog')
            word = word.lower()
            if word[:3] == 'las':
                word = 'lasalle'
            if word not in no_spell_check and len(word)>4:
                word = spell(word)
            if word == 'tech':
                kw.append('technolog')
            elif word not in cStopwords:
                kw.append(stemmer.stem(word))
        return kw
    except TypeError:
        return []