# Spencer Tower
# sea-c42-py
# Mailroom Madness
from operator import itemgetter


donor_list = [['Spencer Tower', 20, 5, 10], ['Bill Gates', 100, 1000, 30],
              ['Incredible Hulk', 20, 15, 70], ['Gandalf', 1, 400, 4],
              ['Smeagle', 10, 40, 50]]    # List of donors


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
        main_menu()

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
            for i in name:
                print(name[0])
                break

        print("")    # Adds a blank line

        thank_you_menu()

    elif (user_input == "quit"):
        main_menu()

    elif (user_input in donor_list):
        x = input("""Please enter a donation amount or 'quit':

> """)
        donation(int(x))
        print_canned_letter(user_input, x)

    elif (user_input not in donor_list):
        donor_list.append([user_input])
        print(donor_list)
        x = input("""Please enter a donation amount or 'quit':

> """)
        donation(float(x))
        print_canned_letter(user_input, x)


def report():
    for donor in donor_list[0:]:
        for i in donor[0:]:
            x = 0
            x = x + i
            print(x)
            break


#  def iterate_inner_list(x):


def donation(amount):
    if (amount == int or float):
        donor_list.append(float(amount))


def print_canned_letter(donor, amount):

    print('''Dear %s,
Thank you so much for your kind donation of $%s!  We here at The Foundation
for Capeless Super Heroes appreciate your generosity.  Your money will
go towards ensuring that no super hero goes another night capeless and
each one can continue to fight crime with dignity and stay super.''' % (donor, float(amount)))


print("Welcome to Mailroom Madness!\n")

print(main_menu())
