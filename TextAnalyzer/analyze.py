import spacy
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from collections import Counter


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
    
    #blob = TextBlob(' '.join(lem), **args)
    
    adj = [token.lemma_ for token in doc if (not token.is_stop and not token.is_punct and token.pos_ == "ADJ")]

    doc = [token.text for token in doc]
    blob = TextBlob(' '.join(doc), **args)
    return {"sentiment": blob.sentiment[0], "subjectivity": blob.sentiment[1], "most used adj": Counter(adj).most_common(10)}
