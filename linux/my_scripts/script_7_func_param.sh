#!/bin/bash

summa=0

myFunction()
(
  summa=$(($1+$2))
  echo "I taken first parametr(50) from script:   $1"
  echo "Second parameter was given from terminal: $2"
  echo "Make summa $summa" 
  echo "function work excelent!"

)

myFunction 50 $1

