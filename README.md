# nlp
Some usefull commands for text pre-processing

To get split a large text file into a specified number(n) of files withoout breaking a sentence.
#n= 10; a=(`wc -l yourfile`) ; lines=`echo $a/$n | bc -l` ; split -l=$lines -d  file.txt file


