def main_menu():

    a = input('''Choose from the following:

T - Send a (T)hank You

R - Create a Report

quit - Quit the program

>''')

    if (a == "T"):
        print("thankYou()")

    elif (a == "R"):
        print("report()")

    elif (a == "quit"):
        exit()


def thank_you_menu():
    a = ('''Please enter a name or choose from the following:

list - Print a list of previous donors

quit - Return to main menu''')

    if (a == "list"):
        print(donor_list)

    elif (a == quit):
        main_menu()

    elif (a == ""):
        x = input("""Please enter a donation amount or 'quit':

> """)
        addName(x)
























__main__

print("Welcome to Mailroom Madness!")  # make new line after

print(main_prompt())
