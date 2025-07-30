score = 0

print("Welcome to todays game!")
print("Let's get started with some questions.")

#Questions 1.
print("\n What is the meaning of life biologically?")
print("1. Preserving life by mantaining genetic information")
print("2. Just to survive")
print("3. Failure to reproduce and pass on genetic information")
answer1 = input("Please enter the number of your answer: ")
if answer1 == "1":
    print("Correct! Tackle the next.")
    score += 1
else:
    print("Not really. Nicetry try though! Move to next.")
    
#Questions 2.
print("\n What is HTML?")
print("1. Hyper Markup Language") 
print("2. Hyper Text Markup Language")
print("3. Hyperlink Markup Language")
answer2 = input("Please enter the number of your answer: ")
if answer2 == "2":
    print("Correct! Tackle the next.")
    score += 1
else:
    print("Not really. Nicetry try though! Move to next.")
    
#Questions 3.
print("\n What is the capital of France?")
print("1. Paris")
print("2. London")
print("3. Berlin")
answer3 = input("Please enter the number of your answer: ")
if answer3 == "1":
    print("Correct! This is the last quiz.")
    score += 1
else:
    print("Not really. Nicetry try though!.")
    
#Final Score
print(f"Your final score is {score} out of 3.")
if score ==3:
    print("Congratulations! You are a genius!")
else:
    print("Try better next time buddy")
    

