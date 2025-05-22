# grammar_rules.py
import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Pronoun | Det Noun
VP -> V NP
Det -> 'a' | 'an' | 'the'
Noun -> 'apple' | 'banana' | 'cat' | 'dog' | 'football'
Pronoun -> 'I' | 'you' | 'they'
V -> 'eat' | 'like' | 'play'
""")
