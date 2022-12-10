from auth import *
from getdocID import *


if __name__ == '__main__':
    AuthHandler().check_token() # in-place : creates text file
    mytoken = get_token() #string
    docIdList = getDocID() #list of tuples [(x,y),(x2,y2),(x3,y3),...)

    if not os.path.exists('PDFs'):
        os.makedirs('PDFs')

    sep = os.sep
    for i,j in docIdList: # i = documentID , j = document name
        with open('PDFs{}{}{}.pdf'.format(os.sep,j,i), 'wb') as f:
            f.write(callAPI(mytoken,i))

#TODO : HANDLE DOCX. I DID NOT ANTICIPATE DOCX