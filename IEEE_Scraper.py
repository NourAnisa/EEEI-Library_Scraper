from DatabaseAPI import *

import requests
import urllib.parse
import json

# -------------------------------------------------------------
# IEEE API Tool
# Spec:  # https://developer.ieee.org/docs/read/metadata_api_details/Leveraging_Boolean_Logic
# -------------------------------------------------------------

class IEEEDatabaseAPI(DatabaseAPI):
    
    # Sorry, this is limited to 200 by IEEE
    MAX_PAPERS = 200
    
    # This is the API Key we Got
    API_KEY = '3hqfbd89kyyfmx8rd9gqesgj'
    
    # This is the URL to the API
    URL = 'http://ieeexploreapi.ieee.org/api/v1/search/articles?max_records=' + str(MAX_PAPERS)
    
    
    def __init__(self):
        print("Creating IEEE Database")
        print("URL:", self.URL)
        print("API_KEY:", self.API_KEY)
        print()
    
    
    def run_query(self, query):
        query_url = self.URL + '&querytext=(' + urllib.parse.quote(query) + ')' + '&apikey=' + self.API_KEY
        print("Attempting IEEE Query")
        print("URL:" + query_url)
        print()
        
        #file = open("response.json", "r")
        #return self.process_results(file.read())    
        
        response = requests.get(query_url)
        print(response.text)
        
        # As a backup, we grab the raw JSOn
        output = open(query + "_raw.txt", "w",  encoding="utf-8")
        output.write(response.text)
        output.close()
        
        input("Results Obtained. Press Any Key to Begin Processing")
        
        return self.process_results(response.text)
    
    
    def process_results(self, data):
        j = json.loads(data)
        
        count = 0
        unique_terms = {}     
        
        for article in j['articles']:
            count += 1
            
            print("-----------------------------------------------------------")
            print(article['title'])
            print("-----------------------------------------------------------")
            
            # Extracts IEEE Terms from the JSON
            if 'ieee_terms' in article['index_terms']:
                ieee_terms = article['index_terms']['ieee_terms']['terms']
                print("IEEE Terms Found:", len(ieee_terms))
                
                for term in ieee_terms:
                    if term in unique_terms:
                        unique_terms[term] += 1
                    else:
                        unique_terms[term] = 1
            
            # Extracts Author Terms from the JSON
            if 'author_terms' in article['index_terms']:
                author_terms = article['index_terms']['author_terms']['terms']
                print("Author Terms Found:", len(author_terms))
                
                for term in author_terms:
                    if term in unique_terms:
                        unique_terms[term] += 1
                    else:
                        unique_terms[term] = 1
            
            print()
        
        print("Processing Complete.  Processed", count, "papers")
        
        if j['total_records'] > self.MAX_PAPERS:
            print("WARNING:", j['total_records'], "records found. Modify your query to get a narrower search")
        
        return unique_terms