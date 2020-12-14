#!/bin/bash

##Getting data from dig lookups


rm -f dig-A-data.csv
touch dig-A-data.csv
echo "A Records runtime" >> dig-A-data.csv
echo "Website,Runtime (seconds)" >> dig-A-data.csv
cat ALL-IPS.txt | while read line
do
  res=$({ /usr/bin/time -f %e dig $line A >/dev/null ; } 2>&1) 

  echo $line ", "  $res >> dig-A-data.csv 2>&1
done
