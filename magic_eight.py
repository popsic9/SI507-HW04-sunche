

while(True):
    ques = input("What is your question or enter exit? ")
    if ques == "exit":
        quit()
    elif ques[-1] != "?":
        print("I’m sorry, I can only answer questions")
