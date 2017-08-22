from steganography.steganography import Steganography
from select_friend import select_friend

def read_message():
    # choose friend from the list
    sender = select_friend()

    encryptd_image = raw_input("Provide name of the image: ")
    secret_message = Steganography.decode(encryptd_image)
    print secret_message