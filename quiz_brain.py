"""
QuizBrain Class

Author: Moa Burke
Date: 29 Oct 2024
Description:
    This class is responsible for managing the quiz logic in a quiz application. It handles
    the initialization of questions, tracks the current question number and user's score,
    and provides methods to retrieve the next question, check the user's answer, and set
    the quiz category and total number of questions.

Main Features:
- Initializes with a list of questions.
- Tracks the current question number and user's score.
- Provides functionality to check if more questions are available.
- Retrieves the next question with proper formatting.
- Compares user answers against correct answers and updates the score accordingly.

Usage:
1. Create an instance of QuizBrain with a list of Question objects.
2. Use methods to manage the quiz flow and check answers.
"""

import html

class QuizBrain:

    def __init__(self, q_list):
        """
        Initializes the QuizBrain instance with a list of questions.

        :param q_list: A list of Question objects containing quiz questions and answers.
        """
        self.question_number = 0 # Tracks the current question number the user is on
        self.score = 0 # Keeps track of the user's score
        self.question_list = q_list # Stores the list of questions
        self.current_question = None # Holds the current question object
        self.total_questions = 0 # Total number of questions in the quiz
        self.category = "" # Default category placeholder

    def set_category(self, category):
        """
        Sets the category of the quiz using the provided category string.

        :param category: The category name as a string, which will be unescaped
        """
        self.category = html.unescape(category) # Unescapes HTML entities in the category name

    def set_total_number_of_questions(self, total_questions):
        """
        Sets the total number of questions in the quiz.

        :param total_questions: The total number of questions to be tracked.
        """
        self.total_questions = total_questions # Stores the total question count

    def still_has_questions(self):
        """
        Checks if there are more questions available to answer.

        :return: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list) # Returns True if there are questions left

    def next_question(self):
        """
         Retrieves the next question from the question list and increments the question number.

        :return: A formatted string containing the current question number and question text.
        """
        self.current_question = self.question_list[self.question_number] # Get the current question object
        self.question_number += 1 # Move to the next question
        q_text = html.unescape(self.current_question.text) # Unescape HTML entities in the question text
        return f"Q.{self.question_number}: {q_text}" # Return the formatted question

    def check_answer(self, user_answer):
        """
        Checks the user's answer against the correct answer for the current question.

        :param user_answer: The answer provided by the user.
        :return: True if the user's answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer # Get the correct answer from the current question

        # Compare the user's answer to the correct answer, ignoring case.
        if user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increment the score if the answer is correct
            return True
        else:
            return False
