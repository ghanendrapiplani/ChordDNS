import socket
import dns.resolver
from time import sleep

file = open("../../data/top1A.txt", "r")
output = open("../../data/Final-400K.txt", "w+")
i = 0



#print("Done with the file")
for line in iter(file.readline, b''):
    line = line.strip("\n")
    
    front = line[:4]
    if(front == "www."):
        line = line [3:]

    #print(line)
    try:
        query = dns.resolver.query(line, "A")
        query2 = dns.resolver.query(line, "MX")
        query3 = dns.resolver.query(line, "NS")

        query2 = str(query2[0])[2:].strip()
        #print(query2)
        output.write(line + " " + str(query[0])+ " "+  query2  + " " + str(query3[0]) + "\n")

    except Exception as e:
        #print(e)
        continue
    #exit(0)

    i+=1
    if(i % 10000 ==0): print (str(i) + " records completed")
    if(i>400000): break
print("done")

