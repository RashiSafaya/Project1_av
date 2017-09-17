# import statements.


import re
from globals import spy
from addfriend import add_friend
from addstatus import add_status
from readmessage import read_message
from sendmessage import send_message
from readchat import read_chat


# start_chat() function definition
def start_chat():
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
                    print "Your Current status is: " + str(current_status_message)
                    spy.current_status_message = add_status()
                    print "Your new status is: " + str(spy.current_status_message)
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
