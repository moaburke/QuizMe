"""
Quiz Setup Class

Author: Moa Burke
Date: 29 Oct 2024
Description:
    This class implements a graphical user interface (GUI) for the QuizMe application using Tkinter.
    It allows users to set up quiz parameters, including selecting a category and the number of questions.
    The interface features a dropdown for category selection and buttons for choosing the number of questions,
    culminating in a 'Proceed' button that confirms the user's selections.

Key Features:
- Customizable quiz category selection from predefined options.
- Selection of the number of questions through interactive buttons.
- User-friendly design with a cohesive color scheme and responsive elements.

Dependencies:
- Tkinter (Python standard GUI library)
"""

from tkinter import *
from tkinter import ttk, messagebox, Frame

# UI Color Scheme and Fonts
MAIN_COLOR = "#375362" # Primary background color
SECONDARY_COLOR = "#fafafa"  # Secondary background or text color
ACCENT_COLOR = "#ff9051" # Accent color for buttons and highlights
FONT_NAME = "Bahnschrift SemiLight Condensed" # Font for application text

# UI Element Configuration
CURSOR_HAND = "hand2" # Hovering cursor for interactive elements

# Border and Highlight Settings
BORDER_WIDTH = 2 # Width of borders around UI elements (in pixels).
HIGHLIGHT_THICKNESS = 0 # Thickness of the highlight around focused elements (set to 0 for no highlight).

class QuizSetup:

    def __init__(self):
        """
        GUI class for setting up quiz parameters including difficulty, category,
        and number of questions. Initializes and displays a main window with options.
        """
        self.category_code = 0  # Code corresponding to quiz category
        self.number_of_questions = 0 # Number of quiz questions selected by user

        # Create the main application window
        self.window = Tk()
        self.window.title("QuizMe by Moa Burke") # Set window title
        self.window.config(padx=20, pady=30, bg=MAIN_COLOR) # Padding and background color

        # Display the welcome message at the top of the setup screen
        self.create_welcome_message()

        # Dropdown and buttons for selecting number of questions
        self.create_number_of_questions_selector()

        # Display dropdown menu for selecting quiz category
        self.create_category_selector()

        # Add a 'Proceed' button to confirm selected settings
        self.create_proceed_button()

        # Run the Tkinter main loop to keep the window open
        self.window.mainloop()

    def create_welcome_message(self):
        """Creates and displays the main welcome messages at the top of the screen."""
        # Main title label
        self.welcome_message_top = Label(
            text="QuizMe",
            width=12,
            bg=SECONDARY_COLOR,
            fg=MAIN_COLOR,
            font=(FONT_NAME, 40, "bold"),
        )
        self.welcome_message_top.pack(pady=(50, 5)) # Add top padding

        # Subtitle with app description
        self.welcome_message_bottom = Label(
            text="Challenge Your Knowledge Across Different Categories!",
            bg=MAIN_COLOR,
            fg=ACCENT_COLOR,
            font=(FONT_NAME, 15, "bold"),
            wraplength=280,  # Adjusts text wrapping if needed
        )
        self.welcome_message_bottom.pack(pady=(10, 40)) # Vertical padding for spacing

    def create_number_of_questions_selector(self):
        """Sets up options for selecting the number of questions."""
        # Label for the number of questions selection
        self.number_of_questions_label = Label(
            text="Number of Questions:",
            bg=MAIN_COLOR,
            fg=SECONDARY_COLOR,
            font=(FONT_NAME, 14)
        )
        self.number_of_questions_label.pack()

        # Create a frame to hold the buttons for question selection
        button_frame = Frame(self.window, bg=MAIN_COLOR)
        button_frame.pack(pady=5)  # Add vertical padding

        # Default selection value for the dropdown
        self.selected_option = StringVar(self.window, "10")

        # Options for the number of questions
        options_number_of_questions = [10, 15, 20, 25, 30]

        # Create a custom button for each option
        for value in options_number_of_questions:
            button = Button(
                button_frame,
                text=str(value),
                bg=SECONDARY_COLOR,  # Default background color
                fg=MAIN_COLOR,
                font=("Arial", 10, "bold"),
                width=5,
                command=lambda v=value: self.select_option(v, button_frame), # Passes value to selection method
                pady=8,
                bd=0,
                cursor=CURSOR_HAND  # Changes cursor to hand on hover
            )
            button.pack(side="left", padx=5)  # Pack horizontally with spacing

            # Highlight the default button for 10 questions
            if value == 10:
                button.config(bg=ACCENT_COLOR, fg=SECONDARY_COLOR)  # Set initial selected color

    def create_category_selector(self):
        """Creates a dropdown menu to select quiz categories from predefined options."""
        # Create and display a label for category selection
        self.category_label = Label(
            text="Category:",
            bg=MAIN_COLOR,
            fg=SECONDARY_COLOR,
            font=(FONT_NAME, 14)
        )
        self.category_label.pack(pady=(7, 0)) # Padding above the label

        # Define available categories along with their corresponding codes
        self.options_category = [
            {"category": "General Knowledge", "code": 9},
            {"category": "Entertainment: Film", "code": 11},
            {"category": "Entertainment: Music", "code": 12},
            {"category": "Entertainment: Video Games", "code": 15},
            {"category": "Science & Nature", "code": 17},
            {"category": "Science: Computers", "code": 18},
            {"category": "Geography", "code": 22},
            {"category": "History", "code": 23},
        ]

        # Initialize a variable to store the selected category, defaulting to the first option
        self.value_category = StringVar(self.window)
        self.value_category.set(self.options_category[0]['category'])  # Set the default category to the first in the list

        # Create a list of category names for the dropdown menu
        category_list = [item['category'] for item in self.options_category]

        # Create the dropdown menu for category selection
        set_category = OptionMenu(self.window, self.value_category, *category_list)
        set_category.config(
            width=30,
            bg=SECONDARY_COLOR,
            fg=MAIN_COLOR,
            font=(FONT_NAME, 14),
            highlightthickness=HIGHLIGHT_THICKNESS,
            pady=10,
            bd=0, # No border around the dropdown menu
            indicatoron=False, # Disable the indicator to create a more seamless appearance
            cursor=CURSOR_HAND   # Change cursor on hover
        )
        set_category.pack(pady=5)

        # Customize the appearance of the dropdown menu options
        dropdown_menu = set_category['menu']
        dropdown_menu.config(
            bg=SECONDARY_COLOR,
            font=(FONT_NAME, 14),
            activebackground=ACCENT_COLOR, # Background color when an option is highlighted
            activeforeground=SECONDARY_COLOR, # Text color when an option is highlighted
        )

    def create_proceed_button(self):
        """Creates and configures the 'Proceed' button to confirm selections."""
        # Button for proceeding
        self.button_proceed = Button(
            text="PROCEED",
            command=self.get_quiz_settings,
            bg=ACCENT_COLOR,
            fg=SECONDARY_COLOR,
            width=30,
            height=2,
            font=(FONT_NAME, 15, "bold"),
            borderwidth=BORDER_WIDTH,
            highlightthickness=HIGHLIGHT_THICKNESS,
            bd=0, # Sets the button's border width to zero
            cursor=CURSOR_HAND  # Sets the cursor to a hand when hovering over the button
        )
        self.button_proceed.pack(pady=30)

    def select_option(self, value, button_frame):
        """
        Updates selected number of questions and adjusts button colors
        to indicate selected option.

        :param value: Number of questions selected by the user.
        :param button_frame: Frame containing the question number buttons.
        """
        # Set the selected option to the user's choice
        self.selected_option.set(value)

        # Iterate through all children of the button frame to update their colors
        for btn in button_frame.winfo_children():
            # Check if the child is a button
            if isinstance(btn, Button):
                # If the button's text matches the selected value, apply the selected color scheme
                if btn.cget("text") == str(value):
                    btn.config(bg=ACCENT_COLOR, fg=SECONDARY_COLOR)  # Highlight selected button
                else:
                    # Reset colors for buttons that are not selected
                    btn.config(bg=SECONDARY_COLOR, fg=MAIN_COLOR) # Default color for unselected buttons

    def get_quiz_settings(self):
        """
        Retrieves and stores the selected quiz settings (category and question count).
        This method is triggered when the 'Proceed' button is clicked.
        """
        # Get the name of the selected category from the dropdown
        category = self.value_category.get()

        # Match the selected category name to its corresponding code in options_category
        category_code = None
        for value in self.options_category:
            if value["category"] == category:
                category_code = value["code"] # Retrieve category code when found
                break

        # Store the category code in the instance variable
        self.category_code = category_code

        # Convert selected question count to an integer and store it
        self.number_of_questions = int(self.selected_option.get())

        # Close the setup window after settings are successfully retrieved
        self.exit_settings()

    def exit_settings(self):
        """Destroys the main window to end the setup process."""
        self.window.destroy()

