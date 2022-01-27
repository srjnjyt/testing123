def rot13(word, number):
    word1 = ''
    
    for c in word:
        t = ord(c) + number
        if t < 123:
            word1 = word1 + chr(t)
        else:
            word1 = word1 + chr(t - 26)
    return word1

print(rot13('banana', 13))
