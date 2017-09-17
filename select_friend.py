from globals import friends


def select_friend():
    counter = 0
    for friend in friends:
        print "%d." % (counter+1)+ friend.getName()
        counter = counter + 1

    result = int(raw_input("Select from the list : "))
    return result - 1
