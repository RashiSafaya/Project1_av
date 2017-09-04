from steganography.steganography import Steganography
from select_friend import select_friend
from datetime import datetime
from globals import friends

def read_message():
    # choose friend from the list
    sender = select_friend()

    encrypted_image = raw_input("Provide name of the image: ")
    secret_message = Steganography.decode(encrypted_image)
    print secret_message

    new_chat = {
        "message": secret_message,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"