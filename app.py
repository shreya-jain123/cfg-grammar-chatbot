import streamlit as st
from validator import validate_sentence

st.title("CFG Grammar Validator Chatbot 💬")

sentence = st.text_input("Enter a sentence:")

if st.button("Validate"):
    valid, trees = validate_sentence(sentence)
    if valid:
        st.success("✅ Valid Sentence!")
        for tree in trees:
            st.text(tree)
    else:
        st.error("❌ Invalid Grammar")
