#!/bin/bash

##Benjamin Michalowicz
##Getting data from dig lookups


rm -f dig-MX-data.csv
touch dig-MX-data.csv
echo "MX Records runtime" >> dig-MX-data.csv
echo "Website,Runtime (seconds)" >> dig-MX-data.csv
cat MX-IPS.txt | while read line
do
  res=$({ /usr/bin/time -f %e dig $line MX >/dev/null ; } 2>&1) 

  echo $line ", "  $res >> dig-MX-data.csv 2>&1
done

