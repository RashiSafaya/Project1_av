# import statements.
from globals import friends, spy
from spydetails import spy


# add new friends.
def add_friend():
    new_friend = spy()
    print "Enter your friend's details \n"
    new_friend.name = raw_input("Enter the name of your friend: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.? ")
    new_friend.name = new_friend.name + " " + new_friend.salutation  # concatenation.
    new_friend.age = int(raw_input("Age?"))
    new_friend.rating = float(raw_input("Spy rating?"))

    # validating input
    if len(new_friend.name) > 0 and 12 < new_friend.age < 60:
        print " "+str(spy.rating)
        if new_friend.rating >= spy.rating:
            # add_friend
            friends.append(new_friend)
            print "Friend Added"
    else:
        print "Sorry invalid entry. We can not add your friend due to some error. Please check your details again."

    # returning number of friends
    return len(friends)
