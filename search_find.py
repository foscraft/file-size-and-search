
from sys import path


def unique_words(self,path):

    text_file = open(path, 'r')
    text = text_file.read()

    #cleaning
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]

    #finding unique
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)

    #sort
    unique.sort()

    return len(unique)