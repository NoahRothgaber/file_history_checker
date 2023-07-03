import os
from os import path

history_file_path = ""


def file_create():
    history_file_name = input("Please enter the file name for your history file, please no spaces...\n")
    while history_file_name.lower() == "exit":
        print("The filename cannot be named exit as it is reserved for a system function")
        history_file_name = input("Please enter the file name for your history file, please no spaces...\n")
    while os.path.exists(f'history_files/{history_file_name}'):
        print("File exists in path")
        history_file_name = input("Please enter the file name for your history file, please no spaces")
    with open(f'history_files/{history_file_name}', "w") as history_file:
        print(f'File created in history_files with the name {history_file_name}')
        history_file.close()
    global history_file_path
    history_file_path = f'history_files/{history_file_name}'


def file_write():
    done_operations = False
    with open(history_file_path, "a") as history_file_add:
        while not done_operations:
            link = input("Please enter the url to track history of... if done type \"done\"\n")
            if link == "done":
                done_operations = True
            else:
                history_file_add.write(link + "\n")


def existing_file():
    user_file_name = ""
    print("The files in the history directory are the following...")
    for file in os.listdir("history_files"):
        print(file)
    proper_file = False
    while not proper_file:
        user_file_name = input("Please enter the name of the file you'd like to work with, "
                               "if you're here by mistake type exit...\n")
        if user_file_name.lower() == "exit":
            proper_file = True
        elif not os.path.exists(f'history_files/{user_file_name}'):
            print("Please enter a valid history file")
        else:
            print(f'Selected file {user_file_name}')
            with open(f'history_files/{user_file_name}', "r") as history_file:
                print("Printing History...")
                for url in history_file:
                    print(url)
            proper_file = True
    return user_file_name


def add_or_check():
    user_choice = ""
    while user_choice != "add" and user_choice != "check":
        user_choice = input("Would you like to (add) to the file or (check) for links in the file?")
        if user_choice != "add" and user_choice != "check":
            print("Please enter \"add\" or \"check\"")
    return user_choice



def welcome():
    complete = False
    global history_file_path
    while not complete:
        user_input = input("Would you like to (create) a file or use an (existing) one, or the current (session) one? "
                           "Type (exit) to quit\n")
        while user_input.lower() != "existing" and user_input.lower() != "create" and user_input.lower() != "session" \
                and user_input.lower() != "exit":
            print("invalid choice")
            user_input = input("Would you like to (create) a file or use an (existing) one?\n")

        if user_input.lower() == "create":
            file_create()
            file_write()
        elif user_input.lower() == "existing":
            file_name = existing_file()
            if file_name != "exit":
                history_file_path = f'history_files/{file_name}'
                user_choice = add_or_check()
                if user_choice == "check":
                    check_link()
                else:
                    file_write()

        elif user_input.lower() == "session":
            if history_file_path == "":
                print("no session file found")
            else:
                print(f'Opening {history_file_path}')
                user_choice = add_or_check()
                if user_choice == "check":
                    check_link()
                else:
                    file_write()
            #  TODO
        else:
            print("exiting...")
            exit()


def check_link():
    total_lines = 0
    with open(history_file_path, "r") as file:
        for line in file:
            total_lines += 1
        if total_lines != 0:
            done_links = False
            while not done_links:
                line_count = 0
                file.seek(0)  # bring file back to the top
                link = input("Please enter the link you want to check history on...\n")
                for line in file:
                    line_count += 1
                    if line.strip() == link:
                        print(f'This link was checked on line(s) {line_count}')
                    else:
                        print("Link was not found in file")
                user_input = ""
                while user_input != "n" and user_input != "y":
                    user_input = input("Would you like to check another link? (y) or (n)...\n")
                if user_input == "n":
                    done_links = True
        else:
            print("History file empty...")



welcome()
