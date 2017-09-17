# import statements.
from spy_details import spy
from globals import spy
from start_chat import start_chat
import re
from colorama import init
init()

print "Let's get started!!!"
question = "Do you want to continue as the default user (Y/N) ? "
existing = raw_input(question)

# validating users input
if existing.upper() == "Y":
    # default user
    # working with default values of a spy
    spy_name = spy.getName()
    spy_salutation = spy.getSalutation()
    spy_age = spy.getage()
    spy_rating = spy.getrating()
    rating = spy_rating
    spy_is_online = spy.getis_online()
    spy.name = spy.salutation + "." + spy.name

    start_chat(spy.name, spy.age, spy.rating, spy.is_online)

elif existing.upper() == "N":
    # new user code here
    spy.name = raw_input("What is your name SPY: ")       # defining variable.
    pattern = '^[a-zA-Z\s]+$'
    if re.match(pattern, spy.name is not None):
        if len(spy.name) > 0 and spy.name.isalpha() is True:
            spy.salutation = raw_input("What should we call you(Mr. or Ms.): ")

        while True:
            try:
                # EXCEPTION HANDLING
                spy_age = int(raw_input("Please enter your age : "))   # typecasting(converting string to int)
                break
            except ValueError:
                print "Please enter your correct age."

        spy.name = spy.salutation + "" + spy.name  # concatenation of name and salutation
        # assignment operator parsing is from r to l.

        # starting chat application
        start_chat(spy.name, spy.age, spy.rating, spy.is_online)

    else:
        print "Invalid name. Please try again."
else:
    print "Wrong choice. Try again"
