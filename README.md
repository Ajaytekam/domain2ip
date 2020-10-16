# domain2ip.py   

Perform DNS Lookup on given list of domain name and return IP addresses. Simply takes domainlist as an input. (saparated by newline '\n') and return their IP address.  

**Usage :**  

```shell  
cat domains.txt  | ./domain2ip.py
```   

Where domains.txt contains list of domain names (separated by newline `\n`).    

**Example :**    

```shell  
$ cat domains.txt | ./domain2ip.py  
```   
Output :  

```shell    
finance.google.com,216.58.200.142
encrypted.google.com,216.58.200.142
id.google.com,172.217.31.195
adwords.google.com,74.125.24.100
www.google.com,172.217.163.164
earth.google.com,216.58.200.142
jobs.google.com,216.58.200.142
europe.google.com,142.250.76.68
security.google.com,216.58.200.142
code.google.com,172.217.163.46
sandbox.google.com,74.125.24.81
download.google.com,172.217.163.68
wap.google.com,216.58.200.142
vpn.google.com,64.9.224.68
wave.google.com,142.250.76.78
relay.google.com,216.58.197.46
documents.google.com,172.217.31.206
feeds.google.com,108.170.217.160
```  

Show only IP addresses  

```shell  
$ cat domains.txt | ./domain2ip.py -ip  
```   

Output :  

```shell   
216.58.196.163
216.58.196.174
172.217.163.36
64.9.224.68
216.58.196.164
216.58.196.174
216.58.196.174
216.58.196.174
172.217.160.142
216.58.196.174
216.58.196.174
74.125.24.81
172.217.166.100
172.217.160.142
172.217.194.102
142.250.67.46
216.58.197.46
108.170.217.160
```  

Help Menu :  

```shell  
$ ./domain2ip.py -h  

usage: domain2ip.py [-h] [-ip]

optional arguments:
  -h, --help     show this help message and exit
  -ip, --ipaddr  Prints IP address only
```  

**Use case :** It is useful in subdomain reconnaissance when you dont have ip addresses of enumerated subdomain, and by using the script you can feed the output to port scanner like `masscan` etc.   
