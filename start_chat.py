from add_status import add_status
from add_friend import add_friend
# start_chat() function definition
def start_chat(spy_name,spy_age,spy_rating):
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do ? \n 1.Add status update \n 2.Close Application \n 3.Add friends"
        result = raw_input(menu_choices)
        # validating users input
        if result == "1":
            # action
            current_status_message = add_status(current_status_message)
        elif result == "2":
            show_menu = False
        elif result == "3":
            # action
            friends = add_friend()
            print "You have %d friends " %friends
        else:
            print "Wrong choice. Please try again."
