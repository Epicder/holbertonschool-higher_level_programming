#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        sentence = None
        tuple = len(sentence), sentence[0]
        return tuple
    else:
        tuple = len(sentence), sentence[0]
        return tuple
