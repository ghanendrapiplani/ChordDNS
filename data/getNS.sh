
IFS=' '
#p="A-400K.txt"
#while read A-400K.txt;
#do
#  echo $i
#  read -a strarr <<< "$i"
#  echo "$strarr[0]" >> A-IPs.txt
#done
rm -f NS-IPS.txt
cat NS-400K.txt | while read line;
do
  #echo $line
  read -a strarr <<< "$line"
  echo ${strarr[0]}
  echo "$strarr" >> NS-IPS.txt
done

