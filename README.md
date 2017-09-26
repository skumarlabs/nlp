# nlp
Some usefull commands for text pre-processing

To get split a large text file into a specified number(n) of files withoout breaking a sentence.
#n= 10; a=(`wc -l yourfile`) ; lines=`echo $a/$n | bc -l` ; split -l=$lines -d  file.txt file

To process wikipedia dump,use wp2txt or modify xml2txt.pl as per your needs and run as below:
perl xml2txt.p enwiki-20170620-pages-articles.xml > enwiki.txt





