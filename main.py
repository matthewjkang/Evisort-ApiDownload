from auth import *
from getdocID import *
import time # Used to handle 15 minute token expiration limit 

if __name__ == '__main__':
    apiKey = input('Enter your API Key : ')
    auth = AuthHandler(apiKey) 
    maketoken = auth.check_token() # in-place : creates text file
    mytoken = get_token() #string
    docIdList = getDocID() #list of tuples [(x,y,z),(x2,y2,z2),(x3,y3,z3),...)

    if not os.path.exists('PDFs'):
        os.makedirs('PDFs')

    sep = os.sep
    print('Downloading your documents. Please wait. Do not close this window.')
    start = time.time()
    for x,y,z in docIdList: # x = documentID , y = document name , z = file extension (.pdf or .docx)
        currentTime = time.time()
        if (currentTime-start) > 840: # if it has been longer than 14 minutes, write me a new key
            mytoken = auth.generateToken()
            start = time.time()
        with open('PDFs{}{}{}{}'.format(os.sep,y,x,z), 'wb') as f:
            f.write(callAPI(mytoken,x))
    print('Done!')