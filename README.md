# Some usefull commands for text pre-processing

## To get split a large text file into a specified number(n) of files withoout breaking a sentence.

n= 10; a=(`wc -l yourfile`) ; lines=`echo $a/$n | bc -l` ; split -l=$lines -d  file.txt file

## To process wikipedia dump,use wp2txt or modify xml2txt.pl as per your needs and run as below:
perl xml2txt.p enwiki-20170620-pages-articles.xml > enwiki.txt

## Print every word in text to a line
tr -sc 'A-Za-z' '\n' < data/enwiki-20170620-pages-articles.xml-1 | less

## Remove other characters from text:
tr -sc 'A-Za-z .' ' ' < enwiki-20170620-pages-articles.xml-1 | less
tr -cd '[[:alnum:]]._-'````

## tr -sc '[[:alnum:]][[:punct:]][[:blank:]]\n' ' ' < enwiki-20170620-pages-articles.xml-1 | less

## Print each word in a new line: alphabetic order
tr -sc 'A-Za-z' '\n' < enwiki | sort | uniq -c | less

## Print each word in a new line: numeric order
tr -sc 'A-Za-z' '\n' < enwiki | sort | uniq -c | sort -n -r | less

## Print each word in a new line: numeric order: case in-sensitive
tr -sc 'A-Z' 'a-z' < enwiki | tr -sc 'A-Za-z' '\n' | sort | uniq -c | sort -n -r | less

## to escape single quote
tr -sc "\342\200\231\262\47"

## normalizing ans stemming : get only having 'ing'
tr -sc 'A-Z' 'a-z' < enwiki | tr -sc 'A-Za-z' '\n' | grep '[aeiou].*ing$' | sort | uniq -c | sort -n -r | less

## sentence segmentation
## minimum edit distance






