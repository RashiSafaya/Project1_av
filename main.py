from spy_details import spy
from start_chat import start_chat
from add_status import add_status

print "Let's get started!!!"
question = "Do you want to continue as " + spy.spy_salutation + spy.spy_name + "(Y/N) ? "
existing = raw_input(question)

# validating users input
if existing == "Y" or existing == "y":
    # logic here
    start_chat(spy.spy_name,spy.spy_age,spy.spy_rating)

elif existing == "N" or existing == "n":
    # new user code here
    spy_name = raw_input("What is your name SPY: ")  # defining variable.
    if spy_name.isalpha():
        if len(spy_name) > 0:
            spy_salutation = raw_input("What should we call you(Mr. or Ms.): ")
            spy_name = spy_salutation + "" + spy_name  # concatenation of name and salutation
            print "WELCOME " + spy_name + ", Glad to have you back with us!"  # assignment operator parsing is from r to l.
            print "Alright " + spy_name + ", I would like to know a little bit more about you before proceeding further."
            spy_age = 0
            spy_ratings = 0.0
            spy_is_online = False
            spy_age = int(raw_input("Enter your age: "))  # typecasting(converting string to int)
            print type(spy_age)

            if spy_age > 12 and spy_age < 50:
                print "Can you please tell us your spy rating: "
                spy_rating = float(raw_input("Enter your rating: "))
                if spy_rating > 4.7:
                    print "Great Work Spy!"
                elif spy_rating > 3.5 and spy_rating <= 4.7:
                    print "You are doing amazing Spy!"
                elif spy_rating > 2 and spy_rating <= 3.5:
                    print "Can do much better Spy!"
                else:
                    print "You need to buckle up Spy!"
                spy_is_online = True
                print "Your authentication is now complete! WELCOME %s. Your age is %d. You have a rating of %.2f" % (
                spy_name, spy_age, spy_rating)
            else:
                print "Sorry, you are not eligible to be a spy."

        else:
            print "No name given. Please try again."
    else:
        print "Enter a valid name"


else:
    print "Wrong choice. Try again"
