# Evisort-ApiDownload
Uses the '/documents/{evisortId}/content' endpoint of the Evisort API.  
Downloads PDF's & DocX from specific Evisort search queries.  

### Overview
**Input** : Excel file exported from Evisort search  
* The excel column that contains docID is extracted, and turned into a list. 
* Each item in that list is then used to ping the API and download the document.  

**Output** : Folder containing all PDF / DocX from that search  

### Usage
* download this project 
* export the search results from your query / queries as an excel sheel  
* drag the excel sheet into the project folder  
* drag the folder into terminal  
* python3 main.py  
* Enter your API Key  

**USAGE TUTORIAL** : https://www.loom.com/share/fb33a42ffe6a4651a027fcbd4fca794d

### Todo
* It works. You are going to need your own API key. (Under the integrations tab in a workspace)  
* Speed might be an issue. Look into whether or not multiprocessing / threading would speed things up. 500 documents took 10 minutes.  