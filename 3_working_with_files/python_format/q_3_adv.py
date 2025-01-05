import json # import the json module to work with JSON data.
import csv # import the csv module to work with csv data.
#Defint function read_questions_answers() with a single parameter file_path. 
#'file_path' represents the path to the file containing the questions and answers.
# initialize empty lists called questions and answers to store the questions and answers separately.
def read_questions_answers(file_path):
    questions = []
    answers = []
    
    # checks if the file_path ends with .json, indicating that it is a JSON file:
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            data = json.load(file) # load contents of the JSON file into the 'data' variable, which becomes a list of dictionaries.
            # iterates over each item (dictionary) in 'data':   
            for item in data:
                questions.append(item['question']) # appends the value of the 'question' key to the questions list
                answers.append(item['answer']) # the value of the 'answer' key to the answers list.
                
    # If the 'file_path' does not end with .json but ends with .csv, indicating that it is a CSV file:           
    elif file_path.endswith('.csv'):
        with open(file_path, 'r') as file: # Opens the file using open() in read mode and assigns the file object to file.
            reader = csv.reader(file) # Create a 'reader' object using csv.reader() to read the CSV file.
            for row in reader: # Iterates over each row in the 'reader', where each row is a list of values.
                questions.append(row[0]) # Appends the first value (row[0]) to the questions list
                answers.append(row[1]) # Appends the second value (row[1]) to the answers list.
                
    #If the file_path does not end with .json or .csv, the function assumes it is a text file.            
    else:  
        with open(file_path, 'r') as file: # Opens the file in read mode using open() and assigns the file object to 'file'.
            for line in file: # Iterates over each line in the file using a for loop.
                # For each line, remove leading and trailing whitespace using strip().
                # and split the line using split(',') to separate the question and answer, assuming they are comma-separated.
                # The question is assigned to question, and the answer is assigned to answer.
                question, answer = line.strip().split(',') 
                # Appends question to the questions list and answer to the answers list.
                questions.append(question) # The question is assigned to questions
                answers.append(answer) # The answer is assigned to answers
                
    return questions, answers # returns the questions and answers lists as a tuple.

#Define function calculate_score() two parameters: 'questions' and 'answers', representing the lists of questions and corresponding answers.
def calculate_score(questions, answers):
    score = 0 # initialize a variable 'score' to 0 to keep track of the user's score.
    for i in range(len(questions)): # Iterate through each question 
        # prompt the user with the question number (i+1), followed by the actual question from the questions list:
        answer = input(f"Q{i+1}: {questions[i]} ") # take the user's answer as input and assigns it to 'answr'
        # Check if the answer, after removing leading and trailing whitespace using strip() 
        # and converting it to lowercase using lower(), matches the corresponding answer from the answers list:
        if answer.strip().lower() == answers[i].strip().lower():
            score += 1 # # If the user answer matches the correct answer, we increment the score by 1
    return score #Returns the calculated score.


#Store user name and result in separate  json file:

# Define store_user_name_and_result function with two parameters: 'User_name', and 'score'.
def store_user_name_and_result(User_name, score):
    # # create a list of dictionaries called result to store the user's name and score.
    result = [{"User Name": User_name, "Result":score}]

    # open a new JSON file (results.json) in write mode to store the user name and result: 
    with open('results.json', 'w') as r:
        json.dump(result,r) # write the result list to the JSON file.
    

# Read questions and answers from the file:
Q_A_file = 'questions_answers_file.csv'  
questions, answers = read_questions_answers(Q_A_file)
    
#Prompt the user for their name:
User_name = input("Enter your name: ")
    
#Ask the questions and calculate the score:
score = calculate_score(questions, answers)
    
# Print the user's score
print(f"{User_name}, your score is: {score}/20")
    
# Save the user's name and score to a file
result_file = 'results.json'  
store_user_name_and_result(User_name, score)