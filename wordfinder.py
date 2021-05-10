"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Parses a file, creating an array of all the words

    [parse] = parses file, strips white space from word, adds word to array.

    [random] = returns a random word from the array


    """
    
    def __init__(self, path):

        file_to_dict = open(path)

        self.words_from_file = self.parse(file_to_dict)

        print(f"{len(self.words_from_file)} words read")
        
    def parse(self, file_to_dict):
        return [word.strip() for word in file_to_dict]

    def random(self):
        return random.choice(self.words_from_file)

    
class SpecialWordFinder(WordFinder):
    """[Extends WordFinder, updating the parse function to accomidate words that begin with #]

    [parse] = parses the document ignoring words that startwith w using the startwith method in python.
    Args:
        
    """

    def parse(self, file):
        return [word.strip() for word in file_to_dict if word.strip() and not word.startswith('#')]




    

