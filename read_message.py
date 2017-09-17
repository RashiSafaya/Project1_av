from steganography.steganography import Steganography
from select_friend import select_friend
import re
from globals import friends
from send_message import ChatMessage
from word_count import word_count

def read_message():
    # choose friend from the list
    sender = select_friend()

    encrypted_image = raw_input("Provide name of the image: ")
    secret_message = Steganography.decode(encrypted_image)

    count = word_count(secret_message)
    new_chat = ChatMessage(secret_message, False, count)
    friends[sender].chats.append(new_chat)
     # sending message when secret text contatins SOS and Save Me

    if emergency(secret_message):
        print "Help is on its way!"
    else:
        print "Secret message saved!"


def emergency(string):
    word_list = re.findall(r"[\w']+", string)
    for word in word_list:
        if word == "SOS" or word == "sos" or word == "SAVE" or word == "save":
            return True
    return False