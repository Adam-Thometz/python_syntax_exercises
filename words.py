def print_upper_words(words):
    """print out words on separate lines all in uppercase
    
    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"]) 
    returns 'HELLO' 'HEY' 'GOODBYE 'YO' 'YES'
    """
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """print out words on separate lines all in uppercase but only if they start with the letter E
    
    print_upper_words2(["hello", "elated", "goodbye", "Edward", "yes"])
    returns 'ELATED' 'EDWARD'
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """print out words in uppercase only if they start with a certain letter from a passed object
    
    print_upper_words3(["hello", "elated", "goodbye", "Edward", "yes"], ["h", "y", "e"])
    returns 'HELLO' 'ELATED' 'EDWARD' 'YES'
    """
    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter):
                print(word.upper())

print('Third function............')