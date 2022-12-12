# THIS ONLY WORKS FOR THE gyg WORKSPACE
# DIFFERENT WORKSPACES REQUIRE YOU TO GENERATE THE API KEY FOR THAT WORKSPACE

import requests
import os

class AuthHandler:
    def __init__(self):
        self.apikey = input('Enter your API Key : ')

    def generateToken(self): 
        # Generates api token from api key
        # INPUT  : self
        # OUTPUT : Api Token (string)
        url = 'https://api.evisort.com/v1/auth/token'
        head = {'EVISORT-API-KEY': self.apikey}
        res = requests.post(url,headers=head)
        api_token = res.json()
        return api_token['token']

    def check_token(self): 
        # If text file containing api token does NOT exists, it creates one.
        # If text file DOES exists, it checks if the token stored in that file works or not
            # If the text stored token is expired or incorrect, it clears the text file and rewrites a new token into the file.
            # If the text stored token is good, then it does nothing
        # INPUT : self
        # OUTPUT : Nothing, or newly generated text file

        if not os.path.exists('token.txt'): # token.txt file has not been written
            print('created a text file, containing a valid token')
            with open('token.txt','w') as file:
                file.write(self.generateToken())

        # token.txt file HAS been written, we just need to check if the token has expired or something
        else:
            with open('token.txt','r') as file:
                mytoken = file.read()
                # file gets closed implicitly 
            req = requests.get("https://api.evisort.com/v1/documents",headers={"Authorization": "Bearer {}".format(mytoken)}) # checks the api response for the token in text file
            if req.status_code == 401: # Expired Token OR Missing Token:
                print(req.text)
                print('token is bad. writing you a new one')
                with open('token.txt','w') as file:
                    file.write(self.generateToken()) #token has expired, so I went ahead and wrote you a new one
            else:
                print('token is good')
        # Why did i write this function? Simple. I did not want a new API token to be created if the last one was still valid.

def get_token():
    with open('token.txt') as file:
        token = file.read()
    return token

def callAPI(token,docID):
    url = "https://api.evisort.com/v1/documents/{}/content".format(docID)
    headers = {
        "accept": "*/*",
        "Authorization": "Bearer {}".format(token)
    }
    req = requests.get(url,headers=headers)
    return req.content


