def reverse(text):
    # return text[::-1]
    string = ''
    for s in reversed([letter for letter in text]):
        string += s
    
    return string

