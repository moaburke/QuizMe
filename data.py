"""
Question Data Fetcher

Author: Moa Burke
Date: 29 Oct 2024
Description:
    This module contains a function to fetch quiz question data from the Open Trivia Database API.
    It retrieves a specified number of true/false questions from a given category, handling errors
    and rate limits appropriately.

Usage:
- Call fetch_question_data with the desired number of questions and category code to retrieve
  a list of quiz questions.
"""

import requests
import time

def fetch_question_data(number_of_questions, category_code):
    """
    Fetches quiz question data from the Open Trivia Database API.

    :param number_of_questions: The number of questions to retrieve (must be an integer).
    :param category_code: The category code for the quiz questions.
    :return: A list of question data if successful, None if unsuccessful.

    This function ensures that the number of questions is a positive integer and
    handles potential HTTP errors and response validation. If the request fails due to
    rate limiting, it waits before retrying. If no valid data is found after several
    attempts, it returns None.
    """

    # Ensure number_of_questions is an integer
    number_of_questions = int(number_of_questions)

    # Start with a valid_param flag as False
    valid_param = False

    # Loop to retry fetching questions until valid data is obtained or number_of_questions reaches zero
    while not valid_param and number_of_questions > 0:
        parameters = {
            "amount": number_of_questions,
            "category": category_code,
            "type" : "boolean", # Specifies that the questions are true/false type
        }

        try:
            # Make a GET request to the Open Trivia Database API with the specified parameters
            response = requests.get(url="https://opentdb.com/api.php", params=parameters)
            response.raise_for_status()  # Raises an error for HTTP error responses

            # Parse the JSON response data
            response_data = response.json()

            # Check if the response indicates a successful request
            if response_data["response_code"] == 0: # Set flag to true since valid data is received
                return response_data["results"] # Return the list of questions
            else:
                # Handle invalid request responses
                print("Invalid request for amount:", number_of_questions)
                print("Response Code:", response_data["response_code"])
                number_of_questions -= 1 # Decrement the number of questions to retry
                print("Trying with amount:", number_of_questions)

        except requests.exceptions.HTTPError as e:
            # Handle specific HTTP errors
            if response.status_code == 429:
                print("Too many requests. Waiting before retrying...")
                time.sleep(2)  # Wait before retrying due to rate limits
            else:
                print(f"Request failed: {e}") # Print the error message
                break  # Exit on other request failures

    return None  # Return None if no valid data was found after retries