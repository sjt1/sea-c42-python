

def mainPrompt():
    a = input("Choose from the following:", "T - Send a (T)hank You",
        "R - Create a Report", "quit - Quit the program")

    if (a == "T"):
        thankYouMenu()

    elif (a == "R"):
        report()

    elif (a == "quit"):
        quitProgram()

'''
def report(): ***
    generate a list for each donor *Sorted by total donation amount*:
Full Name, Total, Number of Donations
    traverse list of donors and maps their names to their donation lists.
Sum their list of donations and print out their info starting with
donor who has the highest sum.
'''

def thankYouMenu():
    a = input("Please enter a name, or choose from the following:",
        "list - Print a list of previous donors", "quit - Return to main menu")

    if (a == "list"):
        print(donors)

    elif (a == "quit"):
        mainPrompt()

    elif (a == ""):
        Check that the name is in the database - iterate over names.

        if (name is in database):
            prompt user to enter an amount
            call function numberVerify()

        if (name is not in database):
            add name to database
            and prompt user to enter amount
            call function numberVerify()

'''

donors = ["Spencer Tower", "Bill Gates", "Incredible Hulk", "Gandalf",
"Smeagle"]

donations = [[100], [50]]

def donorList()
print(donors)  print alphabetically

for i in donors:

    if a == a donor name
    print("Please enter a donation amount or 'quit'")


'''
print("""Dear %s,
    Thank you so much for you kind donation of %s.  We here at the
    foundation for Super Heros in Need of Capes greatly appreciate your
    generosity!  Your money will go to ensuring that no superhero goes
    capeless and each can continue to fight crime with dignity.""") % donor, donation





'''

donors.append()
donations.append() top list
donations.append() nested lists





def quitProgram():
    quit the program


def numberVerify(n):
    if (n != float or int):
        call the function thankYouMenu()

    else:
        call the function sendThankYou()


def sendThankYou(fullName, amount):
    sub fullName and amount into placeholders of canned thank you letter.
    Print Thank You letter to terminal.

def list():
    a for loop that iterates over the list of donor names and returns
    them in alphabetical order.



Print("Welcome to Mailroom Madness!")

mainPrompt()


'''