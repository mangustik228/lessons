#!/bin/bash

myComputer="Asus Tuf"
myOs=`uname -a`
echo "This script name is $0"
echo "Privet $1"
echo "Hello $myOs"

num1=50
num2=45
summa=$((num1+num2))
echo "$num1 + $num2 = $summa"

myhost=`hostname`
mygtw="8.8.8.8"

ping -c 4 $myhost
ping -c 4 $mygtw
echo "Done!"

