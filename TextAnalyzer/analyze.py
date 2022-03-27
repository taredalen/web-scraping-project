import spacy
from nltk import pos_tag
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from nltk.probability import FreqDist


def punc_filter(doc):
    return [token for token in doc if not token.is_punct]


def stopword_filter(doc):
    return [token for token in doc if not token.is_stop]

def lemma(doc):
    return [token.lemma_ for token in doc]

#python -m spacy download en_core_web_md
#python -m spacy download fr_core_news_md
def text_analyze(text, language='en'):
    if language == 'en':
        nlp = spacy.load("en_core_web_md")
        args = {}
    if language == 'fr':
        nlp = spacy.load('fr_core_news_md')
        args = {"pos_tagger": PatternTagger(), "analyzer": PatternAnalyzer()}

    doc = nlp(text)
    doc = punc_filter(doc)
    doc = stopword_filter(doc)
    lem = lemma(doc)

    freq = FreqDist(lem)
    blob = TextBlob(' '.join(lem), **args)

    return {"sentiment": blob.sentiment[0], "subjectivity": blob.sentiment[1], "most used word": freq.most_common(10)}
