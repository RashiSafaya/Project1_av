# import statements.

import re
from globals import spy
from add_friend import add_friend
from add_status import add_status
from read_message import read_message
from send_message import send_message
from read_chat import read_chat

# start_chat() function definition
def start_chat():

    # validating users details.
    error_message = None  # variable for storing error messages.
    pattern = '^[0-9]+$'
    if re.match(pattern, str(spy.age) is None) and not (12 < spy.age < 50):
            # invalid age.
        error_message = "Invalid age. Provide correct details."
        print error_message
    else:
        spy.rating = float(raw_input("What is your spy rating?"))         # typecasting(int to float)
        pattern = '^[0-9]+\.[0-9]+$'
        if re.match(pattern, str(spy.rating) is not None):
            rating = spy.rating
            if spy.rating > 4.7:
                print "Great Work Spy!"
            elif 3.5 < spy.rating <= 4.7:
                print "You are doing amazing Spy!"
            elif 2 < spy.rating <= 3.5:
                print "Can do much better Spy!"
            else:
                print "You need to buckle up Spy!" \

            spy_is_online = True
            welcome_message = "Authentication complete. Welcome\n " \
                              "Name : " + spy.name + "\n" \
                              "Age: " + str(spy.age) + "\n" \
                              "Rating: " + str(spy.rating) + "\n" \
                              "You are awesome \n "


            print welcome_message

            # displaying menu for user.

            show_menu = True
            while show_menu:
                menu_choices = "What do you want to do ? \n " \
                               "1.Add status update \n " \
                               "2.Add a friend \n " \
                               "3.Add a secret message \n " \
                               "4.Read a secret message \n " \
                               "5.Read chats \n " \
                               "6.Close Application \n "

                result = int(raw_input(menu_choices))

            # validating users input
                if result == 1:
                    current_status_message = spy.current_status_message
                    print "Your Current status is: " +str(current_status_message)
                    spy.current_status_message = add_status()
                    print "Your new status is: " +str(spy.current_status_message)
                elif result == 2:
                    no_of_friends = add_friend()
                    print "You have %d friends " % no_of_friends
                elif result == 3:
                    send_message()
                elif result == 4:
                    read_message()
                elif result == 5:
                    read_chat()
                elif result == 6:
                    show_menu = False
                else:
                    print "Wrong choice. Please try again."
        else:
            print "Invalid value. Please try again with a valid value."


