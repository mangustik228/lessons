#!/bin/bash

if [ "$1" == "Vasya"]; then
	echo "Privet $1"
elif [ "$1" == "Trump" ]; then
	echo "Hello $1"
else echo "Zdarova $1"
fi 

x=$2
echo "Starting CASE selection..." 
case $x in 
	1) echo "This is one";;
    [2-9]) echo "Two-Nine";;
  "Petya") echo "Privet $x";;
        *) echo "Parametr Unknown, sorry!"
esac 

y=$3
case $y in 
	1) z="one";;
	2) z="two";;
	*) z="nothing"
esac
echo "Variable = $z"

echo "Login: "
read log

read -p "Password: " pas 

echo "Your login: $log, your passwd: $pas"




