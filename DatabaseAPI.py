class DatabaseAPI:
        
    # Abstract Function
    # Runs a Query on the API using the DB's specified format
    def run_query(self, query):
        pass
    
    # Abstract Function
    # Converts the results from a query into a useable data structure
    def process_results(self, data):
        pass
    