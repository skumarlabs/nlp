import numpy as np
import tensorflow as tf
import sys, time


doc1 = "cat dog rabbit"
doc2 = "cat lion tiger cat"
num_docs = 2

text_dictionary = []
dict_len = 0
word_idx = []

def read_text(filename):
    with open(filename, "r") as f:
        text = ''
        for i in range(1000):
            text += f.readline().replace('\n', '')
        #text = f.read().replace('\n', '')
    return text

def create_word2idx(text1, text2):
    text_dictionary = list(set((text1 + text2).split()))
    dict_len =len(text_dictionary)
    word_idx = np.zeros((dict_len, num_docs), dtype=np.int32)
    t_init = time.time()
    for i in range(dict_len):
        word_idx[i][0] = text1.count(text_dictionary[i])
        word_idx[i][1] = text2.count(text_dictionary[i])
        if i%1000 == 0:
            #sys.stdout.write("reading " + str(i) + " of " + str(dict_len) +'\r')
            print("reading " + str(i) + " of " + str(dict_len) + "time taken: "+str(time.time()-t_init) +"s \r")
            sys.stdout.flush()
    return word_idx



def print_matrix(matrix, i, j):
    for row in range(i):
        for column in range(j):
            print(matrix[row][column], end=" ")
        print("\n")

def getDistance(word1, word2, word3):
    v1 = word_idx[text_dictionary.index(word1)]
    v2 = word_idx[text_dictionary.index(word2)]
    v3 = word_idx[text_dictionary.index(word3)]
    v4 = v1 -v2 + v3
    return v4


def findClosest(v):
    min = np.inf
    index = -1
    for i in range(dict_len):

        dist = np.linalg.norm(v - word_idx[i])
        if  dist < min:
            min = dist
            index = i

    print(text_dictionary[index])



def main():
    datadir = 'data/'
    print('reading input..')
    text1 = read_text(filename=datadir+'/enwiki-20170620-pages-articles.xml-1')
    print('reading input 1 done')
    text2 = read_text(filename=datadir+'/enwiki-20170620-pages-articles.xml-2')
    print('reading input 2 done')
    create_word2idx(text1, text2)
    #print_matrix(word_idx, dict_len, num_docs)
    #findClosest(getDistance('cat', 'dog', 'lion'))
    print('to you')


if __name__ == "__main__":
    main()


