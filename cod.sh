#!/bin/bash

file='url'
file2="play"

mkdir playloads_used
cp $file2 $file playloads_used/
echo " Made Directory"
cd playloads_used
k=1
for i in $( cat $file )
do
  ffuf -w "$file2" -u "$i/FUZZ" -t 50 -mc 200 -o "$k" -of md
  k=$((k+1))
done






