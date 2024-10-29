"""
Question Class

Author: Moa Burke
Date: 29 Oct 2024
Description:
    This class represents a single question in a quiz application. It stores the question text
    and the corresponding answer. The class provides a simple structure to encapsulate the
    data related to a quiz question.

Attributes:
- text: The text of the question.
- answer: The correct answer to the question.

Usage:
1. Create an instance of Question with the question text and answer.
"""

class Question:

    def __init__(self, q_text, q_answer):
        """
        Initializes a Question instance with the given text and answer.

        :param q_text: The text of the question.
        :param q_answer: The correct answer to the question.
        :param q_answer: The correct answer to the question.
        """
        self.text = q_text # Stores the question text
        self.answer = q_answer # Stores the correct answer
