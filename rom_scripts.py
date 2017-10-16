import collections
import os
import re

DATA_DIR = 'data/scripts/'
files = os.listdir(DATA_DIR)
corpus = []  # holds a list of all stories

for file in files:
    with open(DATA_DIR + file, "r") as f:
        corpus.append(f.read().lower())  # append this story to corpus list

replace_pattern = "(\n)+"
target_character = "\n"
re.compile(replace_pattern, re.IGNORECASE)

bag = collections.Counter()  # holds frequncies of each words in corpus
max_word_length = 0

for story in corpus:
    # story = story.translate(str.maketrans("", "", string.punctuation))
    story = re.sub(replace_pattern, target_character, story)
    story = story.split()
    for word in story:
        if len(word) == 39:
            # if len(word) > max_word_length:
            #    max_word_length = len(word)
            print(word)

        bag[word] += 1

print(max_word_length)
