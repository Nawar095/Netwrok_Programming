import json #  import the json module to work with JSON data.

# Read the JSON file containing questions and answers.
with open('questions_answers_file.json') as f:
    Q_A_pairs = json.load(f) # load the JSON data from the file into the Q_A_pairs.
# initialize empty lists called questions and answers to store the questions and answers separately.
questions = []
answers = []
# Ask the user for their name.
User_name = input("Enter your name: ")
# Iterate through each question-answer pair in Q_A_pairs and append the question and answer to their respective lists.
for q in Q_A_pairs:
    questions.append(q['question']) # append question to qustions list
    answers.append(q['answer']) # append answer to answer list
# initialize a variable score to keep track of the user score:
score = 0
# iterate through each question and ask the user for their answer.
for i in range(0, len(questions)):
    answer = input(f"{questions[i]} ")
    # Compare the user's answer with the correct answer 
    if answer.lower().split()== answers[i].lower().split():
        # If the user answer matches the correct answer, we increment the score by 1 
        score+=1

# create a list of dictionaries called result to store the user's name and score.
result = [{"User Name": User_name, "Result":score}]
print(result) #  prints user results 

# open a new JSON file (results.json) in write mode to store the user name and result: 
with open('results.json', 'w') as r:
    json.dump(result,r) # write the result list to the JSON file.