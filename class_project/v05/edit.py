#!/usr/bin/python3


"""This program performs: count all  words, count word that user inputs, find, replace and delete"""


import re
import random
from time import sleep


FILENAME = "text.txt"

# Get menu options
def get_menu_option():
    """menu options"""
    option0 = "PRESS 0 - Count word in a file"
    option1 = "PRESS 1 - Replace word with random number of asterisks"
    option2 = "PRESS 2 - Replace word with another word"
    option3 = "PRESS 3 - Delete word"
    option4 = "PRESS q to EXIT"
    options = [option0, option1, option2, option3, option4]
    return options


# Get user's input
def get_input():
    """get input word to count, replace or delete"""
    word = str(input("\n>>> "))
    return word


# Read a file, lowercase and remove special characters
def read_file():
    """read a file function"""
    data = []
    with open(FILENAME, "r", encoding = "utf-8") as file:
        for line in file:
            for word in line.split():
                data.append(word.lower())
    res = [''.join(i for i in string if i.isalnum()) for string in data]
    return res


# Count total number of words in a file
def count_total_words():
    """count total words"""
    with open(FILENAME, "r", encoding = "utf-8") as file:
        data = file.read()
        words = data.split()
        total_words = len(words)
    return total_words


# Count word number
def count_word(word_to_count):
    """count word"""
    with open(FILENAME, "r", encoding = "utf-8") as file:
        count = 0
        for line in file:
            for word in line.split():
                word_lowercase = word.lower()
                word_only = re.sub(r"[^a-zA-Z0-9]", "", word_lowercase)
                if word_only == word_to_count.lower():
                    count += 1
        return count


# Replace word and update a file with replacement
def replace_word(word_to_replace):
    """replace word with random number of asterisks and save updates"""
    with open(FILENAME, "r+", encoding = "utf-8") as file:
        data = file.read()
        text = re.compile(re.escape(word_to_replace), re.IGNORECASE)
        file_content = text.sub("*" * random.randint(1, 10), data)
        file.seek(0)
        file.truncate()
        file.write(file_content)


# Replace words with custom replacement
def replace_word_with_word(word_to_replace, replacement):
    """replace word with another word"""
    with open(FILENAME, "r+", encoding = "utf-8") as file:
        data = file.read()
        text = re.compile(re.escape(word_to_replace), re.IGNORECASE)
        file_content = text.sub(replacement, data)
        file.seek(0)
        file.truncate()
        file.write(file_content)


# Delete word and update a file
def delete_word(word_to_delete):
    """delete word from a file and save updates"""
    with open(FILENAME, "r+", encoding = "utf-8") as file:
        data = file.read()
        text = re.compile(re.escape(word_to_delete), re.IGNORECASE)
        file_content = text.sub("", data)
        updated_file_content =  re.sub(r' {2,}' , ' ', file_content)
        file.seek(0)
        file.truncate()
        file.write(updated_file_content)


# Main function: while loop and options
def main():
    """runtime function"""
    total_words = count_total_words()
    print(f"\nTotal number of words in this file: {total_words}")
    while True:
        menu = get_menu_option()
        for i in menu:
            print("\n", i)
        option = str(input("\nEnter number to select option >>> "))
        if option in ("q", "Q"):
            print("\nClosing program...\n")
            sleep(1)
            print("Program closed\n")
            break
        if option in ("0", "1", "2", "3"):
            print("\nPlease enter a word: ")
            user_input = get_input()
            word = user_input.lower()
            data = read_file()
            count = count_word(word)
            if count == 0:
                print(f"No '{user_input}' word in this file")
            elif word in data and option == "0":
                print(f"Total number of '{user_input}' word(s) in this file: {count}")
            elif word in data and option == "1":
                print(f"{count} '{user_input}' word(s) will be replaced with asterics...\n...")
                replace_word(word)
                sleep(1)
                print(f"{count} '{user_input}' successfully replaced...")
            elif word in data and option == "2":
                print("\nPlease enter replacement word: ")
                replacement = get_input()
                replace_word_with_word(word, replacement)
                sleep(2)
                print(f"{count} '{user_input} word(s) successfully relaced with '{replacement}'")
            elif word in data and option == "3":
                print(f"{count} '{user_input} will be deleted...\n...")
                delete_word(word)
                sleep(2)
                print(f"{count} '{user_input}' word(s) successfully deleted...")
                sleep(1)
                print(f"\nTotal number of word in this file updated: {count_total_words()}")
            else:
                print(f"No '{user_input}' word in this file")


if __name__ == "__main__":
    main()
