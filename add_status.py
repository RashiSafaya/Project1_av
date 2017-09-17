from globals import spy

def add_status():
    updated_status_message = None
    # logic
    status_messages = ["Spy mode ON", "No message, only call"]
    default = raw_input("Do you want to select from older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
        status_messages.append(updated_status_message)

    elif default.upper() == "Y":
        if spy.current_status_message is not None:
            item_position = 1
            for message in status_messages:
                print str(item_position) + ". " + str(message)
                item_position = item_position + 1
            message_selection = int(raw_input("Choose from the previous status: "))
            if len(status_messages) >= message_selection:
                updated_status_message = status_messages[message_selection - 1]
            else:
                print "Select a proper status"
        else:
            print "No previous status. "
    else:
        print "Wrong choice. Please try again"

    return updated_status_message
