def suggest_fix(sentence):
    if len(sentence.split()) == 1:
        return "Try a full sentence like: 'I eat an apple'."
    if "eat apple" in sentence:
        return "Maybe add a determiner: 'I eat an apple'."
    return "Check word order or missing articles."

