import streamlit as st
import nltk
from nltk import CFG

# Define English grammar
english_grammar = CFG.fromstring("""
S -> NP VP
NP -> Pronoun | Det Noun
VP -> V NP
Det -> 'a' | 'an' | 'the'
Noun -> 'apple' | 'banana' | 'cat' | 'dog' | 'football'
Pronoun -> 'I' | 'you' | 'they'
V -> 'eat' | 'like' | 'play'
""")

# Define Hindi grammar
hindi_grammar = CFG.fromstring("""
S -> NP VP
NP -> Pronoun | Noun
VP -> V NP
Pronoun -> 'वह' | 'वे'
Noun -> 'सेब' | 'केला'
V -> 'खाता_है' | 'पसंद_करता_है'
""")

# Streamlit app
st.title("CFG Grammar Validator Chatbot")
language = st.selectbox("Choose Language", ["English", "Hindi"])

# Load the appropriate grammar
grammar = english_grammar if language == "English" else hindi_grammar
st.write(f"Grammar loaded for: **{language}**")

# User input
sentence = st.text_input("Enter a sentence:")

# Preprocess Hindi verb phrases
if sentence and language == "Hindi":
    sentence = sentence.replace("खाता है", "खाता_है")
    sentence = sentence.replace("पसंद करता है", "पसंद_करता_है")

# Tokenize and parse
if sentence:
    tokens = sentence.strip().split()
    parser = nltk.ChartParser(grammar)
    try:
        parses = list(parser.parse(tokens))
        if parses:
            st.success("✅ The sentence is grammatically correct!")
            for tree in parses:
                st.text(tree)
        else:
            st.error("❌ Invalid Grammar")
    except Exception as e:
        st.error(f"Error: {e}")
