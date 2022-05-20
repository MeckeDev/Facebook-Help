word = input("Word: ")
char = input("Char: ")

def find_chars(word, char):
    """ returns the occurences of a specific Letter in the given Word """
    occ = 0
    [occ := occ + 1 for x in word if x == char]
    return occ

print(find_chars(word, char))