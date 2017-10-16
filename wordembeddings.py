import math
import re
from collections import Counter

import numpy as np
from nltk import word_tokenize


def read_input(filenames):
    '''
    Read files from a list of file names and returns a list of text from each file

    :param filenames: a list of filenames as strings
    :return: a list of strings of text content from each file
    '''
    text_list = []
    for file in filenames:
        try:
            with open(file, 'r') as f:
                text_list.append(f.read().strip())
        except IOError:
            print("Exception while reading files")

    return text_list


def preprocess_text(text_list):
    '''
    Removes punctuation, whitespaces and converts into lower case
    :param text_list: a list of text content
    :return: a list of preprocessed text content
    '''
    for i in range(len(text_list)):
        text_str = " ".join(text_list[i].split())  # remove all whitespaces
        text_str = re.sub(r'[\?;,!\\\(\).&`\'"]', ' ', text_str)
        text_str = re.sub(r'[ ]+', ' ', text_str)
        text_str = text_str.lower()
        text_list[i] = text_str
    return text_list


def build_corpus(text_list):
    '''
    Given a list of text content, it builds a corpus from them
    by concatenating them into a single string

    :param text_list: a list of text content as strings
    :return: corpus in form of single string containing all the text
    '''
    corpus = ' '.join(text_list)
    return corpus


def build_token_list(text_list):
    '''
    Builds a list of tokens from each of text in text_list
    :param text_list: a list of text
    :return: a list of tokens
    '''
    token_list = []
    for text in text_list:
        token_list.append(word_tokenize(text))
    return token_list


def build_token_set(token_list):
    '''
    Builds a sorted set of unique tokens from a list of tokens list
    :param token_list: a list of list having tokens for each text in text_list
    :return: a sorted set of unique tokens
    '''
    tokens = [word for tkns in token_list for word in tkns]  # all the tokens from all token lists
    token_set = sorted(set(tokens))
    return token_set


def build_count_vector_matrix(D, N, token_list, token_set):
    '''

    :param D: Total number of documents
    :param N: Number of unique tokens present in corpus
    :param token_list: List of tokens in all documents
    :param token_set: Set having all the unique tokens in corpus
    :return: count vector matrix of size D x N
    '''
    M = [[0 for j in range(N)] for i in range(D)]
    unique_tokens = list(token_set)
    M = np.array(M)
    for i in range(len(token_list)):
        c = Counter(token_list[i])
        for token in set(token_list[i]):
            j = unique_tokens.index(token)
            M[i][j] = c[token]
    return M


def occur_count(word, token_list):
    '''
    Returns number of documents in which a word occurs.
    :param word: word to be searched
    :param token_list: A list of tokens list generated from multiple documents
    :return: number of documents in which word is present
    '''
    count = 0
    for tokens in token_list:
        if word in tokens:
            count += 1
    return count


def build_tfidf(term, M, token_list, unique_token_list):
    tf = []
    idf = []
    tfidf = []
    for i in range(len(token_list)):
        tf.append(M[i, unique_token_list.index(term)] / len(token_list[i]))
        idf.append(math.log(len(token_list) / occur_count(term, token_list)))
        tfidf.append(tf[i] * idf[i])

    return tfidf


def main():
    data_dir = 'data/scripts/'

    # read input files
    text_list = read_input([data_dir + 'Anna_Karenina.txt', data_dir + 'The_Fault_In_Our_Stars _John_Green.txt'])

    # text_list = ['There is a beautiful house!', 'Look! What a beautiful model']

    # preprocess text
    text_list = preprocess_text(text_list)

    corpus = build_corpus(text_list)
    docs_num = len(text_list)
    token_list = build_token_list(text_list)
    token_set = build_token_set(token_list)
    unique_token_list = list(token_set)
    unique_token_num = len(token_set)

    # count vector matrix shape D x N
    print("Count Vector matrix shape: " + str(docs_num) + " x " + str(unique_token_num))

    count_vector_matrix = build_count_vector_matrix(docs_num,
                                                    unique_token_num,
                                                    token_list,
                                                    token_set)
    term = "cancer"
    print(count_vector_matrix[:, unique_token_list.index(term)])
    tfidf = build_tfidf(term, count_vector_matrix, token_list, unique_token_list)
    print(tfidf)


if __name__ == "__main__":
    main()
