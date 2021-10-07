#import necessarily libraries
import urllib.parse
import requests
import hashlib
import datetime

#main api-link and user keys
main_api = "https://gateway.marvel.com:443/v1/public/characters?"
public_key = "Insert your public key here"
private_key = "Insert your private key here" 

while True:
    #user input and error handling
    name = input("Give a Marvel character, type 'quit' or 'q' to exit: ")
    if name == "quit" or name == "q":
        break

    #create url and authentication
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{private_key}{public_key}'.encode('utf-8'))
    hashed = hash_md5.hexdigest()
    url = main_api + urllib.parse.urlencode({"name":name,"ts":timestamp ,"apikey":public_key, "hash":hashed})

    #printing response
    json_data = requests.get(url).json()
    json_status = json_data["data"]["total"]

    if json_status == 1:
        print("API Status: " + name + " = a succesfull route call. \n")
        print("Here is some information about your character")
        print("================================================")
        print("Name: ", json_data["data"]["results"][0]["name"])
        print("Description: ", json_data["data"]["results"][0]["description"])

        print("Comics: ")
        for each in json_data["data"]["results"][0]["comics"]["items"]:
            print("\t", (each["name"]))
        print("================================================")
        
        print("Series: ")        
        for each in json_data["data"]["results"][0]["series"]["items"]:
            print("\t", (each["name"]))
        print("================================================")
    else:
        print("API Status: " + name + "= not succesfull route call. \n")
