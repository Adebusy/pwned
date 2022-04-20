import requests

import hashlib

psd = input("Enter your Password ") #   Geting imput from user

sh_psd = hashlib.sha1(psd.encode()).hexdigest() # Encoding the Entered Password...

sh_prefix = sh_psd[0:5] # Getting the first five characters...

sh_postfix = sh_psd[5:].upper() # Convert Characters after the five selected onces to upper case...

url = "https://api.pwnedpasswords.com/range/" + sh_prefix

payload={}

headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

pwd_dict = {}

psd_list = response.text.split("\r\n") # breaks it into seperate lines..

for pwds in psd_list:    
    pwds_hash = pwds.split(":") # looks for all values in the left column...
    print(pwds_hash)
    pwd_dict[pwds_hash[0]] = pwds_hash[1] # first half of the first hash and first half of the second hash...

if sh_postfix in pwd_dict.keys(): # Check if sh_lostfix is in pwd_dict...
    print("Password has being compromised {0} Times".format(pwd_dict[sh_postfix]))
else:
    print("Password is Unique and safe to use...")
