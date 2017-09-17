# import statements.

from spydetails import spy
from globals import spy
from startchat import start_chat
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
    spy_is_online = spy.getis_online()
    spy_name = str(spy_salutation) + "." + str(spy_name)
    print  "Welcome " + spy_name + "\nhappy to have you "
    print spy_name + " is of %d years and has a rating of %f" % (spy_age, spy_rating)
    start_chat()




elif existing.upper() == "N":
    # new user code here
    name = raw_input("What is your name SPY: ")  # defining variable.
    pattern = '^[a-zA-Z\s]+$'
    if re.match(pattern,str(name)) != None:
        if len(name) > 0 and name.isalpha():
            salutation =raw_input("What is your salutation(Mr/Ms) SPY:")
            name=salutation+" "+name
            if len(salutation) > 0 and salutation.isalpha() is True:
                age = int(raw_input("What is your age SPY: "))
                pattern = '^[0-9]+$'
                if re.match(pattern, str(age)) != None and (12 < age < 50):
                    rating = float(raw_input("What is your rating SPY: "))
                    pattern = '^[0-9]+\.[0-9]+$'
                    if re.match(pattern, str(rating)) is not None:
                        if rating > 4.7:
                            print "Great Work Spy!"
                        elif 3.5 < rating <= 4.7:
                            print "You are doing amazing Spy!"
                        elif 2 <rating <= 3.5:
                            print "Can do much better Spy!"
                        else:
                            print "You need to buckle up Spy!"
                        spy_is_online = True
                        spy.setSpy(name,salutation,age,rating,spy_is_online)
                        welcome_message = "Authentication complete. Welcome\n " \
                                          "Name : " + name + "\n" \
                                                                 "Age: " + str(age) + "\n" \
                                                                                          "Rating: " + str(
                            rating) + "\n" \
                                          "You are awesome \n "
                        print welcome_message
                        start_chat()

                    else:
                        print "Enter correct rating"
                else:
                    print "Enter correct age"
            else:
                print "Enter correct salutation"
        else:
            print "Enter correct name"
    else:
        print "Enter correct name"

else:
    print "WRONG VALUE"
