"""
Quiz Interface Module

Author: Moa Burke
Date: 29 Oct 2024
Description:
    This module creates a graphical user interface (GUI) for the QuizMe application using Tkinter.
    It allows users to answer quiz questions, track their score, and display question categories.

Key Components:
- QuizInterface class: Manages the GUI elements, updates based on user interactions, and displays quiz questions.
- Event handling: Responds to user input (true/false answers) and updates the GUI accordingly.

Usage:
Instantiate the QuizInterface class with a QuizBrain object to start the quiz interface.
"""

from tkinter import *
from quiz_brain import QuizBrain

# UI Color Scheme and Fonts
MAIN_COLOR = "#375362" # Primary background color
SECONDARY_COLOR = "#fafafa"  # Secondary background or text color
ACCENT_COLOR = "#ff9051" # Accent color for buttons and highlights
CORRECT_ANSWER_COLOR = "#d0dbc5"  # Light green for correct answers
INCORRECT_ANSWER_COLOR = "#dbafb8"  # Light red for incorrect answers
FONT_NAME = "Bahnschrift SemiLight Condensed" # Font for application text

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizMe by Moa Burke") # Title of the window
        self.window.config(width=400, height=600, padx=20, pady=20, bg=MAIN_COLOR)

        # Label to display the question number
        self.question_number_label = Label(bg=MAIN_COLOR, fg=SECONDARY_COLOR, font=(FONT_NAME, 14), pady=15)
        self.question_number_label.grid(row=0, column=0)

        # Label to display the user's score
        self.score_label = Label(text="Score: 0", bg=MAIN_COLOR, fg=SECONDARY_COLOR, font=(FONT_NAME, 14), pady=15)
        self.score_label.grid(row=0, column=1)

        # Label to display the current category of questions
        self.category_label = Label(text=self.quiz.category, bg=MAIN_COLOR, fg=ACCENT_COLOR, font=(FONT_NAME, 18))
        self.category_label.grid(row=1, column=0, columnspan=2)

        # Create canvas to display the card
        self.canvas = Canvas(width=300, height = 250, highlightthickness=0, bg=SECONDARY_COLOR)

        # Create text element on the canvas for the question text
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            font=("Arial", 14, "italic"),
            fill=MAIN_COLOR)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=15)

        # Button for user to answer "True"
        self.button_true = Button(
            text="TRUE",
            command= self.true_pressed,
            bg=ACCENT_COLOR,
            fg=SECONDARY_COLOR,
            width=30,
            height=2,
            font=(FONT_NAME, 15, "bold"),
            borderwidth=2,
            highlightthickness=0,
            bd=0,
            cursor="hand2"   # Changes cursor to hand when hovering
        )
        self.button_true.grid(row=3, column=0, columnspan=2, pady=10)

        # Button for user to answer "False"
        self.button_false = Button(
            text="FALSE",
            command=self.false_pressed,
            bg=ACCENT_COLOR,
            fg=SECONDARY_COLOR,
            width=30,
            height=2,
            font=(FONT_NAME, 15, "bold"),
            borderwidth=2,
            highlightthickness=0,
            bd=0,
            cursor="hand2"  # Sets the cursor to a hand when hovering over the button
        )
        self.button_false.grid(row=4, column=0, columnspan=2, pady=(0, 20))

        # Load the first question at startup
        self.get_next_question()

        # Start the Tkinter event loop to listen for user interactions
        self.window.mainloop()


    def get_next_question(self):
        """
        Retrieves the next question from the quiz and updates the GUI elements accordingly.

        This method changes the background color of the canvas, updates the score display,
        and configures the question number label. It retrieves the next question and displays it
        on the canvas. If there are no more questions, it shows the final score and disables the answer buttons.
        """
        self.canvas.config(bg=SECONDARY_COLOR)  # Reset canvas background color
        self.score_label.config(text=f"Score: {self.quiz.score}") # Update score label

        # Check if there are more questions available
        if self.quiz.still_has_questions():
            # Update the question number label to show current question and total questions\
            self.question_number_label.config(
                text=f"Question {self.quiz.question_number + 1}/{self.quiz.total_questions}")

            # Get the next question text from the quiz brain
            q_text = self.quiz.next_question()

            # Update the canvas to show the new question
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # No more questions: Display the final score and disable answer buttons
            self.canvas.itemconfig(self.question_text, text=f"Total Score: {self.quiz.score}/{self.quiz.question_number}", font=(FONT_NAME, 25, "bold"))
            self.button_true.config(state="disabled")  # Disable the True button
            self.button_false.config(state="disabled") # Disable the True button


    def true_pressed(self):
        """
        Handles the event when the user presses the "True" button.

        This method checks if the answer "True" is correct by calling the check_answer method
        from the quiz brain and provides feedback to the user.
        """
        # Check if the selected answer is correct
        is_right = self.quiz.check_answer("true")
        # Provide feedback based on correctness of the answer
        self.give_feedback(is_right)

    def false_pressed(self):
        """
        Handles the event when the user presses the "False" button.

        This method checks if the answer "False" is correct by calling the check_answer method
        from the quiz brain and provides feedback to the user.
        """
        # Check if the selected answer is correct
        is_right = self.quiz.check_answer("false")
        # Provide feedback based on correctness of the answer
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """
        Provides visual feedback to the user based on whether their answer was correct or incorrect.

        This method changes the background color of the canvas to indicate if the answer was right (green)
        or wrong (red). It also schedules the next question to be displayed after a brief pause.

        :param is_right: A boolean indicating whether the user's answer was correct (True) or incorrect (False).
        """
        if is_right:
            self.canvas.config(bg=CORRECT_ANSWER_COLOR) # Set background to light green for correct answer
        else:
            self.canvas.config(bg=INCORRECT_ANSWER_COLOR) # Set background to light red for incorrect answer

        # Wait 1 second before loading the next question
        self.window.after(1000, self.get_next_question)

