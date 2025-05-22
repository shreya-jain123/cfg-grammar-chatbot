from nltk import CFG, ChartParser
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

grammar = CFG.fromstring("""
S -> NP VP | AUX NP VP
NP -> Det N | Pronoun | Adj N | Det Adj N
VP -> V NP
AUX -> 'Do' | 'Does'

Det -> 'a' | 'an' | 'the'
Adj -> 'big' | 'red' | 'tasty'
N -> 'apple' | 'banana' | 'boy' | 'girl'
Pronoun -> 'I' | 'you' | 'he' | 'she' | 'they' | 'we'
V -> 'eat' | 'eats' | 'like' | 'likes'
""")



parser = ChartParser(grammar)

def validate_sentence(sentence):
    tokens = tokenizer.tokenize(sentence)
    try:
        trees = list(parser.parse(tokens))
        return (len(trees) > 0, trees)
    except:
        return (False, [])
