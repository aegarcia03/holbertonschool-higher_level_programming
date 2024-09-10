#!/usr/bin/python3
def multiple_returns(sentence):

    length = len(sentence)
# check if the sentence is empty, if so returb a tuple
    if not sentence:
        return (0, None)
    else:
# if not empty, return the tuple
        return (length, sentence[0])
