from auth import *
from getdocID import *

if __name__ == '__main__':
    AuthHandler().check_token() # in-place : creates text file
    mytoken = get_token() #string
    docIdList = getDocID() #list of tuples [(x,y),(x2,y2),(x3,y3),...)

    if not os.path.exists('PDFs'):
        os.makedirs('PDFs')

    sep = os.sep
    print('Downloading your documents. Please wait. Do not close this window.')
    for x,y,z in docIdList: # x = documentID , y = document name , z = file extension (.pdf or .docx)
        with open('PDFs{}{}{}{}'.format(os.sep,y,x,z), 'wb') as f:
            f.write(callAPI(mytoken,x))
    print('Done!')