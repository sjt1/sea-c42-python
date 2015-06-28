

def main_menu():
    '''Print main menu options to terminal and take user input.'''

    user_input = input('''Choose from the following:
T - Send a (T)hank You

R - Create a Report

quit - Quit the program

> ''')

    if (user_input == "T"):
        thank_you_menu()

    elif (user_input == "R"):
        report()

    elif (user_input == "quit"):
        exit()

    else:
        main_menu()  # make it do nothing instead


def thank_you_menu():
    '''Print thank you options to terminal and take user input.'''

    user_input = input('''Please enter a name or choose from the following:

list - Print a list of previous donors

quit - Return to main menu

> ''')

    if (user_input == "list"):
        for name in donor_list:
            print(name)

        print("")    # Adds a blank line

        thank_you_menu()

    elif (user_input == "quit"):
        main_menu()

    elif (user_input == ""):
        x = input("""Please enter a donation amount or 'quit':

> """)
        donation(user_input)


donor_list = ["Spencer Tower", "Bill Gates"]    # List of donors

donation_list = [100, 100]    # List of donations


def donation(amount):
    if (amount == int or float):
        donation_list.append(amount)
        print(donation_list)


def donors(name):
    donors.append(name)


print("Welcome to Mailroom Madness!\n")

print(main_menu())
