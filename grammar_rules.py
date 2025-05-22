import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP

# English Rules
NP -> EN_Pronoun | EN_Det EN_Noun
VP -> EN_V EN_NP
EN_NP -> EN_Pronoun | EN_Noun

EN_Det -> 'a' | 'an' | 'the'
EN_Noun -> 'apple' | 'banana' | 'cat' | 'dog' | 'football'
EN_Pronoun -> 'I' | 'you' | 'they'
EN_V -> 'eat' | 'like' | 'play'

# Hindi Rules
NP -> HI_Pronoun | HI_Noun
VP -> HI_V HI_NP
HI_NP -> HI_Noun | HI_Pronoun

HI_Pronoun -> 'वह' | 'वे'
HI_Noun -> 'सेब' | 'केला'
HI_V -> 'खाता है' | 'पसंद करता है'
""")
