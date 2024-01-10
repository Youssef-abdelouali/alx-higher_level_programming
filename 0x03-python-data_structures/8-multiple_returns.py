#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    first_character = sentence[0] if sentence_length > 0 else "None"
    result_tuple = sentence_length, first_character
    return result_tuple
