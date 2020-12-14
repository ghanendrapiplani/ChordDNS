#!/bin/bash

##Getting data from dig lookups


rm -f dig-NS-data.csv
touch dig-NS-data.csv
echo "NS Records runtime" >> dig-NS-data.csv
echo "Website,Runtime (seconds)" >> dig-NS-data.csv
cat ALL-IPS.txt | while read line
do
  res=$({ /usr/bin/time -f %e dig $line NS >/dev/null ; } 2>&1) 

  echo $line ", "  $res >> dig-NS-data.csv 2>&1
done
