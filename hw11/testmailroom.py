# Spencer Tower
# sea-c42-py
# Mailroom Madness


donor_list = [['Spencer Tower', 20, 5, 10], ['Bill Gates', 100, 1000, 30],
              ['Incredible Hulk', 20, 15, 70], ['Gandalf', 1, 400, 4],
              ['Smeagle', 10, 40, 50]]


def main_menu():
    '''Print main menu options to terminal and take user input.'''
    user_input = input('''Choose from the following:\n
                        T - Send a (T)hank You\n
                        R - Create a (R)eport\n
                        quit - Quit the program\n> ''')

    if (user_input == "T"):
        thank_you_menu()
    elif (user_input == "R"):
        create_report()
        main_menu()
    elif (user_input == "quit"):
        exit()
    else:
        main_menu()


def thank_you_menu():
    '''Print thank you options to terminal and take user input.'''
    user_input = input('''Please enter a name or choose from the following:\n
                        list - Print a list of previous donors\n
                        quit - Return to main menu\n> ''')

    if (user_input == "list"):
        for name in donor_list:
            for i in name:
                print(name[0])
                break
        thank_you_menu()
    elif (user_input == "quit"):
        main_menu()
    else:
        append_donation(user_input)
        thank_you_menu()


def create_report():
    '''Create a report of donor names, their donation total, number of
    donations, and average donation.'''
    print('\tName\t\tTotal\t\t#\tAverage')
    for donor in donor_list:
        x = 0
        for i in donor[1:]:
            x = x + i
        print('%s\t\t$%d\t\t%d\t$%d' % (donor[0], x, len(donor[1:]),
              x / len(donor[1:])))


def append_donation(name):
    '''Append donations to donors and add new donors to donor list.'''
    found = False
    for donor in donor_list:
        if (name == donor[0]):
            amount = float(input("Please enter a donation amount.\n> "))
            donor.append(amount)
            print(canned_letter(name, amount))
            found = True
            break
    if (not found):
        amount = float(input("Please enter a donation amount.\n> "))
        donor_list.append([name, amount])
        print(canned_letter(name, amount))


def canned_letter(donor, amount):
    '''Create canned thank-you letter with donor name and donation.'''
    return('''Dear %s,\nThank you so much for your kind donation of $%s!
We here at The Foundation for Capeless Super Heroes appreciate your generosity.
Your money will go towards ensuring that no super hero goes another night
capeless and each one can continue to fight crime with dignity and stay
super.\n''' % (donor, float(amount)))


print("Welcome to Mailroom Madness!\n")

print(main_menu())
