from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import string

snowball = SnowballStemmer(language='english')
stop_words = stopwords.words()

def tokenize(text):
    tokens = word_tokenize(text)
    tokens_without_punctuation = [x for x in tokens if x not in string.punctuation]
    tokens_without_punctuation_and_stop_words = [x for x in tokens_without_punctuation if x not in stop_words]
    stemmed_tokens = [snowball.stem(x) for x in tokens_without_punctuation_and_stop_words]
    return stemmed_tokens