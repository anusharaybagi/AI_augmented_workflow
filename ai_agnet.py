def quiz_agent(answer):
    answer = answer.lower().strip()

    if answer == "paris":
        return "Correct! Paris is the capital of France."
    elif answer == "delhi":
        return "Correct! New Delhi is the capital of India."
    elif answer == "python":
        return "Correct! Python is a programming language."
    else:
        return "That's not the expected answer. Try again."


print("================================")
print("       AI QUIZ AGENT")
print("================================")

print("Question 1: What is the capital of France?")
answer = input("Your answer: ")
print("Agent:", quiz_agent(answer))

print("\nQuestion 2: What is the capital of India?")
answer = input("Your answer: ")
print("Agent:", quiz_agent(answer))

print("\nQuestion 3: Which language is commonly used in AI?")
answer = input("Your answer: ")
print("Agent:", quiz_agent(answer))
