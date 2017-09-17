from colorama import Fore
from globals import friends, spy
from selectfriend import select_friend


def read_chat():
    friend_choice = select_friend()
    for chat in friends[friend_choice].chats:
        if chat.sent_by_me:
            # displaying chats with different colour codes
            print "[%s] %s: \n%s (no of words:%s)" % (Fore.BLUE + " " + chat.time.strftime("%d %B %Y"),
                                                      Fore.RED + " " + spy.getName(), Fore.BLACK + " " + chat.message,
                                                      " " + str(chat.no_of_words))
        else:
            print "[%s] %s: \n%s (no of words:%s)" % [Fore.BLUE + ' ' + chat.time.strftime("%d %B %Y"),
                                                      Fore.RED + " " + friends[friend_choice].name,
                                                      Fore.BLACK + " " + chat.message,
                                                      " " + str(chat.no_of_words)]

