#!/usr/bin/python3


"""This program performs: count all  words, count word that user inputs, find, replace and delete"""


import re
import random
from time import sleep


FILENAME = "text.txt"


def get_menu_option():
    """Function defines and returns menu options"""
    option0 = "PRESS 0 - Count word in a file"
    option1 = "PRESS 1 - Replace word with random number of asterisks"
    option2 = "PRESS 2 - Replace word with another word"
    option3 = "PRESS 3 - Delete word"
    option4 = "PRESS q to EXIT"
    # Create list of menu options
    options = [option0, option1, option2, option3, option4]
    return options


def get_input():
    """Get input word to count, replace or delete"""
    # Get input and convert it into string
    word = str(input("\n>>> "))
    # Remove spaces from input string
    pattern = re.compile(r'\s+')
    word = re.sub(pattern, '', word)
    return word


def read_file():
    """Read the file"""
    # Create an empty list to append data
    data = []
    with open(FILENAME, "r", encoding = "utf-8") as file:
        for line in file:
            # Split string to get separate strings (words)
            for word in line.split():
                # Append words in a list and apply lower() method to get lowercase words
                data.append(word.lower())
    # Remove special characters, isalnum() returns True if all characters are letters and numbers
    file_content = [''.join(i for i in string if i.isalnum()) for string in data]
    return file_content


def count_total_words():
    """Count total number of words in the file"""
    with open(FILENAME, "r", encoding = "utf-8") as file:
        data = file.read()
        # Split words and count total number of words in a file
        words = data.split()
        total_words = len(words)
    return total_words


def count_word(word_to_count):
    """Count word that user inputs"""
    with open(FILENAME, "r", encoding = "utf-8") as file:
        count = 0
        for line in file:
            for word in line.split():
                word_lowercase = word.lower()
                # Ignore special characters
                word_only = re.sub(r"[^a-zA-Z0-9]", "", word_lowercase)
                if word_only == word_to_count.lower():
                    count += 1
        return count


def replace_word(word_to_replace):
    """Replace word that user inputs with random number of asterisks and save updates"""
    with open(FILENAME, "r+", encoding = "utf-8") as file:
        data = file.read()
        # Compile regex pattern, ignore special characters and ignorecase
        text = re.compile(re.escape(word_to_replace), re.IGNORECASE)
        # Replace word with random number of integers (1, 10)
        file_content = text.sub("*" * random.randint(1, 10), data)
        # Set the reference point in the begining of the file
        file.seek(0)
        # Truncate method resizes the file, if no parameter uses current file size
        file.truncate()
        # Write new content to the file
        file.write(file_content)


def replace_word_with_word(word_to_replace, replacement):
    """Replace word with another word that user inputs"""
    with open(FILENAME, "r+", encoding = "utf-8") as file:
        data = file.read()
        # Compile regex pattern, ignore special characters and ignorecase
        text = re.compile(re.escape(word_to_replace), re.IGNORECASE)
        # Replace word with another word
        updated_file_content = text.sub(replacement, data)
        # Set the reference point in the begining of the file
        file.seek(0)
        # Truncate method resizes the file, if no parameter uses current file size
        file.truncate()
        # Write new content to the file
        file.write(updated_file_content)


def delete_word(word_to_delete):
    """Delete word from a file and save updates"""
    with open(FILENAME, "r+", encoding = "utf-8") as file:
        data = file.read()
        # Compile regex pattern, ignore special characters and ignorecase
        text = re.compile(re.escape(word_to_delete), re.IGNORECASE)
        # Replace word with an empty string
        file_content = text.sub("", data)
        # Remove multiple spaces between words
        file_content_spaces =  re.sub(r" {2,}" , " ", file_content)
        # Remove spaces before special characters
        updated_file_content = file_content_spaces.replace(" .",  ".")
        updated_file_content = updated_file_content.replace(" ,", ",")
        # If first word of the sentence was removed and there was comma after this word
        updated_file_content = updated_file_content.replace(".,", ".")
        # Set the reference point in the begining of the file
        file.seek(0)
        # Truncate method resized the file, if no parameter uses current file size
        file.truncate()
        # Write new content to the file
        file.write(updated_file_content)


def main():
    """Runtime function"""
    total_words = count_total_words()
    print(f"\nTotal number of words in this file: {total_words}\n")
    # Infinite while loop
    while True:
        # Print menu options
        menu = get_menu_option()
        for i in menu:
            print(i)
        option = str(input("\nEnter number to select option >>> "))
        # Exit program option
        if option in ("q", "Q"):
            print("\nClosing program...\n")
            sleep(1)
            print("Program closed\n")
            break
        # Edit options
        if option in ("0", "1", "2", "3"):
            print("\nPlease enter a word: ")
            user_input = get_input()
            word = user_input.lower()
            data = read_file()
            count = count_word(word)
            # If there is no word in a file
            if count == 0:
                print(f"No '{user_input}' word in this file\n")
            # Option0: count word
            elif word in data and option == "0":
                print(f"Total number of '{user_input}' word in this file: {count}\n")
            # Option1: replace word with asterisks
            elif word in data and option == "1":
                print(f"{count} '{user_input}' word(s) will be replaced with asterics...\n")
                replace_word(word)
                sleep(1)
                print(f"{count} '{user_input}' successfully replaced")
            # Option2: replace word with another word
            elif word in data and option == "2":
                print("\nPlease enter replacement word: ")
                replacement = get_input()
                print(f"{count} '{user_input}' word(s) will be replaced with {replacement}...\n")
                replace_word_with_word(word, replacement)
                sleep(2)
                print(f"{count} '{user_input} successfully relaced with '{replacement}'")
            # Option3: delete word form a file
            elif word in data and option == "3":
                print(f"{count} '{user_input} word(s) will be deleted...\n...")
                delete_word(word)
                sleep(2)
                print(f"{count} '{user_input}' successfully deleted")
                sleep(1)
                print(f"\nTotal number of words in this file updated: {count_total_words()}")
            else:
                print(f"No '{user_input}' word in this file")


if __name__ == "__main__":
    main()
