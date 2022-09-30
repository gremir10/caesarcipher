"""
implement a caesar substitution cipher
where the key is an integer from 1 - 25
"""
def caesar(txt, key):
    out_str = ""
    # force key to be in range
    key = keynumber % 26
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # alpha2 = alpha + alpha <- idk what to do with this
    for c in txt:
        if (c in alpha):
            out_str += chr((ord(c) + key - 97) + 97) # for lowercase
        else:
            out_str += chr((ord(c) + key - 65) + 65) # else if uppercase
    return out_str
print("Input text")
text = input()
print("Input key number")
keynumber = int(input())
print("Original text = " + text)
print("Key = " + str(keynumber))
print("Encrypted text = " + caesar(text, keynumber))