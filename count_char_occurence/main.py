""" Module to count the Occurrences of a Char in a Word """
word_input = input("Word: ")
char_input = input("Char: ")


def find_chars(word, char):
    """ returns the occurrences of a specific Letter in the given Word """
    occ = 0
    count = [occ := occ + 1 for x in word if x == char]
    return count


print(find_chars(word_input, char_input))
