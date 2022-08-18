#!/usr/bin/python3


"""This programs performs count words, count specific word that user inputs, find and replace"""


import re
import random
from time import sleep


# Get menu option select
def get_menu_option():
    """menu option"""
    option1 = "PRESS 1 - Replace words with random number of asterics"
    option2 = "PRESS 2 - Replace words with another words"
    option3 = "PRESS 3 - Delete words"
    option4 = "PRESS q to EXIT"
    options = [option1, option2, option3, option4]
    return options


# Get user's input
def get_input():
    """get input word to replace or delete"""
    word = str(input("\n>>> "))
    return word


# Read a file, lowercase and remove special characters
def read_file():
    """read a file function, lower*( and remove special characters"""
    data = []
    with open("text.txt", "r", encoding = "utf-8") as file:
        for line in file:
            for word in line.split():
                data.append(word.lower())
    res = [''.join(i for i in string if i.isalnum()) for string in data]
    return res


# Count total number of words in a file
def count_words():
    """count total words"""
    with open("text.txt", "r", encoding = "utf-8") as file:
        data = file.read()
        words = data.split()
        total_words = len(words)
    return total_words


# Count words that should be replaced
def count_word_to_replace(word_to_replace):
    """count word to be replaced"""
    with open("text.txt", "r", encoding = "utf-8") as file:
        count = 0
        for line in file:
            for word in line.split():
                word_lowercase = word.lower()
                word_only = re.sub(r"[^a-zA-Z0-9]", "", word_lowercase)
                if word_only == word_to_replace.lower():
                    count += 1
        return count


# Replace word and update a file with replacement
def replace_word(word_to_replace):
    """replace word with random number of asterics and save updates"""
    with open("text.txt", "r+", encoding = "utf-8") as file:
        data = file.read()
        text = re.compile(re.escape(word_to_replace), re.IGNORECASE)
        file_content = text.sub("*" * random.randint(1, 10), data)
        file.seek(0)
        file.truncate()
        file.write(file_content)


# Replace words with custom replacement
def replace_word_with_word(word_to_replace, replacement):
    """replace word with another word"""
    with open("text.txt", "r+", encoding = "utf-8") as file:
        data = file.read()
        text = re.compile(re.escape(word_to_replace), re.IGNORECASE)
        file_content = text.sub(replacement, data)
        file.seek(0)
        file.truncate()
        file.write(file_content)


# Delete word and update a file
def delete_word(word_to_delete):
    """delete word from a file and save updates"""
    with open("text.txt", "r+", encoding = "utf-8") as file:
        data = file.read()
        text = re.compile(re.escape(word_to_delete), re.IGNORECASE)
        file_content = text.sub("", data)
        file.seek(0)
        file.truncate()
        file.write(file_content)


# Main function: while loop and options
def main():
    """runtime function"""
    total_words = count_words()
    print(f"\nTotal number of words in this file: {total_words}")
    while True:
        menu = get_menu_option()
        for i in menu:
            print("\n", i)
        option = str(input("\nEnter number to select option >>> "))
        if option in ("q", "Q"):
            print("Close program")
            break
        if option == "1":
            print("\nPlease enter word to be replaced. Press 'q' to exit")
            user_input = get_input()
            word_to_replace = user_input.lower()
            data = read_file()
            count = count_word_to_replace(word_to_replace)
            if user_input in ("q", "Q"):
                print("Close program...")
                break
            if count == 0:
                print(f"No '{user_input}' word in this file")
            elif word_to_replace in data:
                print(f"{count} '{user_input}' word(s) will be replaced with asterics...\n...")
                replace_word(word_to_replace)
                sleep(2)
                print(f"{count} '{user_input}' successcully replaced...")
            else:
                print(f"No '{user_input}' word in this file")
        elif option == "2":
            print("\nPlease enter word to be replaced. Press 'q' to exit")
            user_input = get_input()
            word_to_replace = user_input.lower()
            data = read_file()
            count = count_word_to_replace(word_to_replace)
            if user_input in ("q", "Q"):
                print("Close program...")
                break
            if count == 0:
                print(f"No '{user_input}' word in this file")
            elif word_to_replace in data:
                print("\nPlease enter replacement word")
                replacement = get_input()
                replace_word_with_word(word_to_replace, replacement)
            else:
                print(f"No '{user_input}' word in this file")


if __name__ == "__main__":
    main()
