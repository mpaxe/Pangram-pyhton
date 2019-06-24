def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    is_valid = True
    for char in alphabet:
        if char not in sentence:
            is_valid = False
            break      
    return is_valid
