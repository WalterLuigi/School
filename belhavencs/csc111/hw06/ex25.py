#!/usr/bin/python
# Creates function break_words it splits stuff and returns them as words
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# Creates function sort_words it takes words and returns sorted words
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# Creates function print_first_word, which pops off the first word, then prints it
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
    return(word)

# Creates function print_last_word, which pops off the last word, then prints it
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
    return(word)

# Creates function sort_sentence and returns sorted words
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# Creates funtion print_first_and_last which breaks apart sentences and then prints the first and last word
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# Creates function print_first_and_last_sorted, which does exactly what the name says
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
