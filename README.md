# Evisort-ApiDownload
Uses the '/documents/{evisortId}/content' endpoint of the Evisort API.  
Downloads PDF's & DocX from specific Evisort search queries.  

Input : Excel file exported from Evisort search  
* The excel column that contains docID is extracted, and turned into a list. 
* Each item in that list is then used to ping the API and download the document.  
Output : Folder containing all PDFs from that search  

## Usage
* download this project 
* export the search results from your query / queries as an excel sheel
* drag the excel sheet into the project folder
* drag the folder into terminal
* python3 main.py

## Todo
* It works. You are going to need your own API key. (Under the integrations tab in a workspace)
* Create an __init__ function for AuthHandler class that asks the user for their API key. This way, the user does not need to create a secret.py file.
* Speed might be an issue. Look into whether or not implementint multiprocessing / threading would speed things up. 500 documents took 10 minutes.  