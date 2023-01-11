#!/bin/bash

for myfile in `ls *.txt`; do 
	cat $myfile 
done

for x in {1..10}; do 
	echo "X = $x"
done

for (( i=1; i<=10; i++ )); do 
	echo "Nomer I = $i"
done
