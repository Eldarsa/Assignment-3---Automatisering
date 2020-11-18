# importing the requests library - MAKING UPDATE/DELETE REQUEST TO FUSEKI example. - removes all the things w.r.t. the cube.
import requests 

if __name__ == "__main__":

    URL = "http://127.0.0.1:3030/kbe/update"

    """
    Use of POST with requests module:
    https://www.w3schools.com/python/ref_requests_post.asp
    """

    query = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#> ' + \
    'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> ' + \
    'INSERT ' + \
    '{ ' + \
    'kbe:table_id a kbe:table. ' + \
    'kbe:table_id kbe:hasLegHeight "50"^^xsd:float. ' + \
    'kbe:table_id kbe:hasLegRadius tableTop. ' + \
    'kbe:table_id kbe:hasDiameter diameter. ' + \
    'kbe:table_id kbe:hasTableTopHeight length. ' + \
    'kbe:TableTop kbe:hasTableTopLength length. ' + \
    'kbe:TableTop kbe:hasTableTopWidth width. ' + \
    '}  ' + \
    'WHERE ' + \
    '{ ' + \
    'kbe:table_id ?pred ?obj. ' + \
    '}'



    # defining a query params 
    PARAMS = {'update': query} 
    
    # sending get request and saving the response as response object 
    r = requests.post(url = URL, data = PARAMS) 

    #Checking the result
    print("Result:", r.text)


class kbe_requestor():

    def __init__(self, URL):
        self.URL = URL

    