from validator import validate_sentence
from suggestion import suggest_fix

print("CFG Chatbot 🤖 - Type 'exit' to quit\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break

    valid, trees = validate_sentence(user_input)
    
    if valid:
        print("Bot ✅: That's a grammatically correct sentence!")
        for tree in trees:
            tree.pretty_print()  # Shows parse tree in console
            # tree.draw()        # Uncomment this for popup GUI (Tkinter)
        print()
    else:
        print("Bot ❌: That's not grammatically correct.\n")
        print("Hint 💡:", suggest_fix(user_input), "\n")
