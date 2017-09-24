import find_analogies as fa


def main():
    datadir = 'data/'
    print('reading input..')
    text1 = fa.read_text(filename=datadir+'/enwiki-20170620-pages-articles.xml-1')
    print('reading input 1 done')
    text2 = fa.read_text(filename=datadir+'/enwiki-20170620-pages-articles.xml-2')
    print('reading input 2 done')
    fa.create_word2idx(text1, text2)
    #print_matrix(word_idx, dict_len, num_docs)
    #findClosest(getDistance('cat', 'dog', 'lion'))
    print('to you')


if __name__ == "__main__":
    main()
