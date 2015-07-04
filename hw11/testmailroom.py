# Spencer Tower
# sea-c42-py
# Mailroom Madness


donor_list = [['Spencer Tower', 20, 5, 10], ['Bill Gates', 100, 1000, 30],
              ['Incredible Hulk', 20, 15, 70], ['Gandalf', 1, 400, 4],
              ['Smeagle', 10, 40, 50]]


def main_menu():
    '''Print main menu options to terminal and take user input.'''
    user_input = input('''Choose from the following:\nT - Send a (T)hank You
R - Create a (R)eport\nquit - Quit the program\n> ''')

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
list - Print a list of previous donors\nquit - Return to main menu\n> ''')

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


def report():
    print('Name      |    Total   |    #   |    Average')
    for donor in donor_list:
        x = 0
        for i in donor[1:]:
            x = x + i
        print("%s | %d | %d | %d" % (donor[0], x, len(donor[1:]), x / len(donor[1:])))


def append_donation(name):
    found = False
    for donor in donor_list:
        if name == donor[0]
                found = True
                amount = input("Please enter a donation amount.\n> ")
                donor.append(float(amount))
                print(donor_list)
                break
    if (not found):
        for donor in donor_list:
            if name == donor[0]:
                if d[0] != name:
                    donor_list.append([name])
                    amount = input("Please enter a donation amount.\n> ")
                    donor_list[-1].append(float(amount))
                    print(donor_list)


def canned_letter(donor, amount):
    print('''Dear %s,
Thank you so much for your kind donation of $%s!  We here at The Foundation
for Capeless Super Heroes appreciate your generosity.  Your money will
go towards ensuring that no super hero goes another night capeless and
each one can continue to fight crime with dignity and stay super.\n''' % (donor, float(amount)))


print("Welcome to Mailroom Madness!\n")

print(main_menu())
