import re
import time
import os

def get_file_path(prompt):
    """Prompt the user for a file path and return the path"""
    # Keep prompting the user until they enter a valid file path
    while True:
        # Get the file path from the user
        file_path = input(prompt)
        # Check if the file exists
        if os.path.exists(file_path):
            # Return the file path if it is valid
            return file_path
        else:
            # Print an error message if the file path is invalid
            print("Sorry, that file path is invalid. Please try again.")

start_time = time.time()  # Record the start time

# Prompt the user for the input and output file paths
input_file_path = get_file_path("Enter the path to the input file: ")
output_file_path = get_file_path("Enter the path to the output file: ")

# Open the input file
with open(input_file_path, "r", encoding="utf8") as input_file:
    # Read all the lines in the input file into a list
    lines = input_file.read()
    # Use a regular expression to extract the email addresses from the file
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", lines)
    # Open the output file
    with open(output_file_path, "w") as output_file:
        # Write the email addresses to the output file
        for email in emails:
            output_file.write(email + "\n")

start_time = time.process_time()  # Record the start time

# ... do some processing ...

elapsed_time = time.process_time() - start_time  # Calculate the elapsed time
print(f"Elapsed time: {elapsed_time:.2f} seconds")  # Print the elapsed time