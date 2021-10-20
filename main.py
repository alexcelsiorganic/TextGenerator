from nltk.tokenize import WhitespaceTokenizer
from nltk.probability import FreqDist
from nltk import Text
from nltk.util import ngrams
import random


def read_file(file_name):
    text_file = open(file_name, 'r', encoding='utf-8')
    text = text_file.read()
    text_file.close()
    return text


file_name = input()
scenario = read_file(file_name)
Tokenizer = WhitespaceTokenizer()
text_token = Tokenizer.tokenize(scenario)
freq_tokens = Text(text_token)
freq_dict = FreqDist(freq_tokens)
collection_trigrams = list(ngrams(text_token, 3))
counter = len(text_token)
Markov_dict = dict()
for (head_1, head_2 , tail) in collection_trigrams:
    head = head_1 + " " + head_2
    Markov_dict.setdefault(head, {})
    Markov_dict[head].setdefault(tail, 0)
    Markov_dict[head][tail] += 1

Markov_chain = list()
chain_sentence = list()
head_element = ""
random.seed()
while True:
    random_tuple = random.choice(collection_trigrams)
    head_element = random_tuple[0] + " " + random_tuple[1]
    test_head_element = head_element.split()
    if test_head_element[0][0].isupper() and test_head_element[0][0].isalpha() and test_head_element[0].endswith(('?', '!', '.')) is False:
        break
chain_sentence.append(head_element.split()[0])
chain_sentence.append(head_element.split()[1])
while len(Markov_chain) <= 10:
    counter = 0
    while True:
        most_probably = random.choices(list(Markov_dict[head_element].keys()),
                                       weights=list(Markov_dict[head_element].values()))[0]
        if most_probably.endswith(('?', '!', '.')):
            if len(chain_sentence) < 5:
                counter += 1
                if counter > 1:
                    head_element = chain_sentence[-1] + " " + most_probably
                    chain_sentence.append(most_probably)

                else:
                    continue
            else:
                chain_sentence.append(most_probably)
                break
        else:
            if len(chain_sentence) != 0:
                head_element = chain_sentence[-1] + " " + most_probably
                chain_sentence.append(most_probably)
            else:
                head_element = Markov_chain[-1][-1] + " " + most_probably
                chain_sentence.append(most_probably)
    Markov_chain.append(chain_sentence)
    head_element = chain_sentence[len(chain_sentence) - 2] + " " + chain_sentence[len(chain_sentence) - 1]
    chain_sentence = list()

for i in range(10):
    print(" ".join(Markov_chain[i]))
