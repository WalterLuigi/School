#!/usr/bin/env python

# Creates dictionary with word type as key and value as list of words
wordtypes = {
    'direction': ['north', 'south', 'east', 'west', 
    'down', 'up', 'left', 'right', 'forward', 'backward', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
    'noun': ['door', 'bear', 'princess', 'cabinet']
}

# Reverses the above words and sticks them all in a dictionary with the word as the key
# and the type as the value, then assigns to vocab
vocab = {word: word_type for word_type, words in wordtypes.items() for word in words}

def scan(sentence):
    tokens = []
    sentence = sentence.lower()
    for word in sentence.split():
        try:
            word_type = vocab[word]
        except KeyError:
            try:
                value = int(word)
            except ValueError:
                tokens.append(('error', word))
            else:
                tokens.append(('number', value))
        else:
            tokens.append((word_type, word))
    return tokens


def main():
    # Prompts user for input to pass to our scanner
    sentence = input('> ')
    # Scans it
    scan(sentence)


# If this code isn't imported as part of a module then main() runs
if __name__ == '__main__':
    main()