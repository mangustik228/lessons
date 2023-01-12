#!/bin/bash

myfunction() 

(
    echo "this is text from function!"
    echo "Script name is:      $0"
    echo "First parameter is:  $1"
    echo "Second parameter is: $2"
    echo "This is new line from vim"
)

myfunction first_parameter $1
