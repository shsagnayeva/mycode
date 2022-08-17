#!/usr/bin/python3


"""This programs performs count words in a file, count specific word that user inputs to replace, find and replace"""


import re
import random
from time import sleep


# Get user's input
def get_input():
    word_to_replace = str(input("\nPlease enter word to replace: \n(press 'q' for exit) \n>>> "))
    word_to_replace = word_to_replace.lower()
    return word_to_replace


# Count total nummber of words in a file
def count_words():
    with open("text.txt", "r") as file:
        count = 0
        for line in file:
            for word in line.split():
                count +=1
    return count


# Count words that should be replaced
def count_word_to_replace(word_to_replace):
    with open("text.txt", "r") as file:
        count = 0
        for line in file:
            for word in line.split():
                word_lowercase = word.lower()
                word_only = re.sub(r"[^a-zA-Z0-9]", "", word_lowercase)
                if word_only == word_to_replace.lower():
                    count +=1
        return count


# Replace word and update a file with replacement
def replace_word(word_to_replace):
    with open("text.txt", "r+") as file:
        data = file.read()
        text = re.compile(re.escape(word_to_replace), re.IGNORECASE)
        file_content = text.sub("*" * random.randint(1, 10), data)
        file.seek(0)
        file.truncate()
        file.write(file_content)


# Read a file
def read_file():
    data = []
    with open("text.txt", "r") as file:
        for line in file:
            for word in line.split():
                data.append(word.lower())
    res = [''.join(i for i in string if i.isalnum()) for string in data]
    return res


# Main function: while loop and options
def main():
    total_words = count_words()
    print(f"\nTotal number of words in this file: {total_words}")

    while(True):
        data = read_file()
        user_input = get_input()
        count = count_word_to_replace(user_input)

        if user_input == "q":
            print("Close program...")
            break

        elif count == 0:
            print(f"No '{user_input}' word in this file")

        elif user_input in data:
            print(f"{count} '{user_input}' word(s) will be replaced...\n...Replace in progress...\n")
            replace_word(user_input)
            sleep(2)
            print(f"{count} '{user_input}' successcully replaced...")

        else:
            print(f"No '{user_input}' word in this file")


if __name__ == "__main__":
    main()
