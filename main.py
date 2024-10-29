"""
Quiz Application - main.py

Author: Moa Burke
Date: 29 Oct 2024
Description:
    This script serves as the entry point for the Quiz Application. It performs the following functions:
    1. Initializes the QuizSetup to configure the quiz parameters.
    2. Fetches question data from an external API based on user-defined criteria (category and number of questions).
    3. Constructs a list of Question objects using the fetched data.
    4. Initializes the QuizBrain to manage quiz logic and scoring.
    5. Sets up the QuizInterface for user interaction.

"""

from question_model import Question
from data import fetch_question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
from setup import QuizSetup

# Initialize the quiz setup
quiz_setup = QuizSetup()

# Retrieve the category code and number of questions from the quiz setup
category_code = quiz_setup.category_code
number_of_questions = quiz_setup.number_of_questions

# Fetch question data from the Open Trivia Database API using the specified parameters
question_data = fetch_question_data(number_of_questions, category_code)

# Extract the category name from the first question data retrieved
category_name = question_data[0]["category"]

# Create a list to hold the Question objects for the quiz
question_bank = []

# Loop through each question in the fetched data to create Question objects
for question in question_data:
    question_text = question["question"] # Get the text of the question
    question_answer = question["correct_answer"] # Get the correct answer
    new_question = Question(question_text, question_answer) # Create a Question object
    question_bank.append(new_question) # Add the Question object to the question bank

# Initialize the QuizBrain with the created question bank to manage quiz logic and scoring
quiz = QuizBrain(question_bank)

# Set the total number of questions in the quiz
quiz.set_total_number_of_questions(number_of_questions)

# Set the category name for the quiz based on fetched data
quiz.set_category(category_name)

# Initialize the QuizInterface to handle user interaction and display the quiz UI
quiz_ui = QuizInterface(quiz)
