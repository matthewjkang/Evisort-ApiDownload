# THIS ONLY WORKS FOR THE GetYourGuide WORKSPACE
# DIFFERENT WORKSPACES REQUIRE YOU TO GENERATE THE API KEY FOR THAT WORKSPACE

import requests
import os
import secret

exdoclist = [13388374,15303085,13388595]

class apiDownload:

    def generateToken(self):
        url = 'https://api.evisort.com/v1/auth/token'
        head = {'EVISORT-API-KEY': secret.api_key}
        res = requests.post(url,headers=head)
        api_token = res.json()
        return api_token['token']

    def check_token(self):

        # token.txt file has not been written
        if not os.path.exists('token.txt'):
            with open('token.txt','w') as file:
                file.write(self.generateToken())

        # token.txt file HAS been written, we just need to check if the token has expired or something
        else:
            with open('token.txt','r') as file:
                mytoken = file.read()
                # file gets closed implicitly 
            req = requests.get("https://api.evisort.com/v1/documents",headers={"Authorization": "Bearer {}".format(mytoken)}) 
            if req.status_code == 401: # Expired Token:
                with open('token.txt','w'):
                    file.write(self.generateToken())
                print('token has expired, so I went ahead and wrote you a new one')
            else: # Token is good
                print('token is not expired. Here is the status code and response body')
                print(req.status_code)
                print(req.text)

    def callAPI(self,docID):
        url = "https://api.evisort.com/v1/documents/{}/content".format(docID)
        headers = {
            "accept": "*/*",
            "Authorization": "Bearer {}".format(self.token)
        }


apiDownload().check_token()