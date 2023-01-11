#!/bin/bash

counter=0

while [ $counter -lt 10 ]; do 
	echo "current counter is $counter"
	counter=$(($counter+1))
	# let counter=counter+1
	# let counter+=1
done
echo "done!"

