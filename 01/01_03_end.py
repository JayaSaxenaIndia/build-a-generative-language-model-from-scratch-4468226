
import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens):
            if (len(tokens) - 1)  == i:
                break
            self.graph[token].append(tokens[i + 1])
               

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
            current = random.choice(options)
            # add the random choice to the output string
            output += f" {current}"
        return output

'''
To run: 
# This is how your code will be called.
# Todo:  Your answer should be the largest value in the numbers list.
text = """
कुछ काम करो, कुछ काम करो
जग में रह कर कुछ नाम करो
यह जन्म हुआ किस अर्थ अहो
समझो जिसमें यह व्यर्थ न हो
कुछ तो उपयुक्त करो तन को
नर हो, न निराश करो मन को

संभलो कि सुयोग न जाय चला
कब व्यर्थ हुआ सदुपाय भला
समझो जग को न निरा सपना
पथ आप प्रशस्त करो अपना
अखिलेश्वर है अवलंबन को
नर हो, न निराश करो मन को
जब प्राप्त तुम्हें सब तत्त्व यहाँ
फिर जा सकता वह सत्त्व कहाँ
तुम स्वत्त्व सुधा रस पान करो
उठके अमरत्व विधान करो
दवरूप रहो भव कानन को
नर हो न निराश करो मन को
निज गौरव का नित ज्ञान रहे
हम भी कुछ हैं यह ध्यान रहे
मरणोंत्‍तर गुंजित गान रहे
सब जाय अभी पर मान रहे
कुछ हो न तज़ो निज साधन को
नर हो, न निराश करो मन को
प्रभु ने तुमको दान किए
सब वांछित वस्तु विधान किए
तुम प्राप्‍त करो उनको न अहो
फिर है यह किसका दोष कहो
समझो न अलभ्य किसी धन को
नर हो, न निराश करो मन को 

किस गौरव के तुम योग्य नहीं
कब कौन तुम्हें सुख भोग्य नहीं
जान हो तुम भी जगदीश्वर के
सब है जिसके अपने घर के 
फिर दुर्लभ क्या उसके जन को
नर हो, न निराश करो मन को 

करके विधि वाद न खेद करो
निज लक्ष्य निरन्तर भेद करो
बनता बस उद्यम ही विधि है
मिलती जिससे सुख की निधि है
समझो धिक् निष्क्रिय जीवन को
नर हो, न निराश करो मन को
कुछ काम करो, कुछ काम करो
"""

chain = Answer.MarkovChain()
chain.train(text)
sample_prompt = "न"
print(chain.generate(sample_prompt))
show_hints = True
show_expected_result = True
result = chain.generate(sample_prompt)
'''

''' Sample output:
न निराश करो मन को न निराश करो निज साधन को
Great work! You got the right answer.
Your code returned: न हो कुछ काम करो कुछ काम करो कुछ काम करो
--- -- -- -- -- -- -- -- -- -- -- --
'''
