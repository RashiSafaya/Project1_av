from steganography.steganography import Steganography
from selectfriend import select_friend
from datetime import datetime
from globals import friends
from wordcount import word_count


# save the messages
class ChatMessage:
    def __init__(self, message, sent_by_me, no_of_words):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
        self.no_of_words = no_of_words


def send_message():
    # choose a friend
    friend_choice = select_friend()

    # prepare the message
    original_image = raw_input("What is the name of the image? ")
    output_image = raw_input("Provide name of the output image: ")
    text = raw_input("What do you want to write? ")
    # Encrypt message
    if text:
        Steganography.encode(original_image, output_image, text)
        # counting the no of words in the message
        count = word_count(text)
        new_chat = ChatMessage(text, True, count)
        friends[friend_choice].chats.append(new_chat)

        # removing spy with a msg 100 words long
        if count > 100:
            del friends[friend_choice]
            print "You have been removed!"
        else:
            print "Secret message was sent!"  # success message
    else:
        print "Enter the secret text!"

