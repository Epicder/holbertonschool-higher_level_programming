#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        sentence = None
        tuple = 0, sentence
        return tuple
    else:
        tuple = len(sentence), sentence[0]
        return tuple
