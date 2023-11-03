
import random
# string.punctuation will give the all sets of punctuation. 
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            # The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
            # Use the maketrans() method to create a mapping table.
            # str.maketrans(<string specifying the characters you want to replace>, <replace with the corresponding character in this string>, <which characters to remove>) 
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
               

    def generate(self, prompt, length=10):
        # get the lask token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, [])
            if not options:
                continue
            # use random.choice method to pick a current option
            
            # add the random choice to the output string
    
        return output
