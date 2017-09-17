
import re

def word_count(string):
    while True:
        count = len(re.findall("[a-zA-Z_]+", string))
    return count