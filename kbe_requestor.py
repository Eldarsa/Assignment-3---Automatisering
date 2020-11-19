# importing the requests library - MAKING UPDATE/DELETE REQUEST TO FUSEKI example. - removes all the things w.r.t. the cube.
import requests 

if __name__ == "__main__":

    URL = "http://127.0.0.1:3030/kbe/query"

    """
    Use of POST with requests module:
    https://www.w3schools.com/python/ref_requests_post.asp
    """
    #the dictionary that will be filled in
    param_dict = {
    "pname": "",
    "ttLength": 0,
    "ttWidth": 0,
    "ttHeight": 0,
    "legHeight": 0,
    "legDiameter": 0 
    }

    query= 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>' +\
    'Select ?table ?ttheight ?ttLength ?ttWidth ?legHeight ?legDiameter' +\
    '{' +\
    '?table a kbe:Table.' +\
    '?table kbe:hasHeight ?ttheight.' +\
    '?table kbe:hasLegLength ?legHeight.' +\
    '?table kbe:hasWidth ?ttWidth.' +\
    '?table kbe:hasLength ?ttLength.' +\
    '?table kbe:hasDiameter ?legDiameter' +\
    '}'

    # defining a query params 
    PARAMS = {'query':query} 
    
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 

    #Checking the result
    data = r.json()

    #Saving the values in param_dict
    pname = data['results']['bindings'][-1]['table']['value'] #index -1 to get the last table that was created
    param_dict['pname'] = pname
    ttLength = data['results']['bindings'][-1]['ttLength']['value']
    param_dict['ttLength'] = ttLength
    ttWidth = data['results']['bindings'][-1]['ttWidth']['value']
    param_dict['ttWidth'] = ttWidth
    ttHeight = data['results']['bindings'][-1]['ttheight']['value']
    param_dict['ttHeight'] = ttHeight
    legHeight = data['results']['bindings'][-1]['legHeight']['value']
    param_dict['legHeight'] = legHeight
    legDiameter =data['results']['bindings'][-1]['legDiameter']['value']
    param_dict['legDiameter'] = legDiameter

    print(param_dict)
    

    


class kbe_requestor():

    def __init__(self, URL):
        self.baseURL = URL

    def insert(self, param_dict):
        URL = self.baseURL + "/update"

        print(param_dict)

        query = query = 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>' + \
        'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>' +\
        'INSERT' +\
        '{' + \
        'kbe:'+param_dict["pname"] +' a kbe:Table. ' + \
        'kbe:'+param_dict["pname"] +' kbe:hasHeight "' +str(param_dict["ttHeight"]) + '"^^xsd:float. ' + \
        'kbe:'+param_dict["pname"] +' kbe:hasLegLength "'+ str(param_dict["legHeight"])+ '"^^xsd:float. ' + \
        'kbe:'+param_dict["pname"] +' kbe:hasWidth "'+ str(param_dict["ttWidth"])+ '"^^xsd:float. ' + \
        'kbe:'+param_dict["pname"] +' kbe:hasLength "'+ str(param_dict["ttLength"])+ '"^^xsd:float. ' + \
        'kbe:'+param_dict["pname"] +' kbe:hasDiameter "'+ str(param_dict["legDiameter"])+ '"^^xsd:float. ' + \
        '}' + \
        'WHERE' + \
        '{' + \
        '}'



        # defining a query params 
        PARAMS = {'update': query} 
        
        # sending get request and saving the response as response object 
        r = requests.post(url = URL, data = PARAMS) 

        #Checking the result
        print("Result:", r.text)

        return

    def select(self):

        URL = self.baseURL + "/query"
        #the dictionary that will be filled in
        param_dict = {
        "pname": "",
        "ttLength": 0,
        "ttWidth": 0,
        "ttHeight": 0,
        "legHeight": 0,
        "legDiameter": 0 
        }

        query= 'PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>' +\
        'Select ?table ?ttheight ?ttLength ?ttWidth ?legHeight ?legDiameter' +\
        '{' +\
        '?table a kbe:Table.' +\
        '?table kbe:hasHeight ?ttheight.' +\
        '?table kbe:hasLegLength ?legHeight.' +\
        '?table kbe:hasWidth ?ttWidth.' +\
        '?table kbe:hasLength ?ttLength.' +\
        '?table kbe:hasDiameter ?legDiameter' +\
        '}'

        # defining a query params 
        PARAMS = {'query':query} 
        
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 

        #Checking the result
        data = r.json()

        #Saving the values in param_dict
        pname = data['results']['bindings'][0]['table']['value'] #index -1 to get the last table that was created
        pname = pname.split("#",1)[1] 
        param_dict['pname'] = pname
        ttLength = data['results']['bindings'][0]['ttLength']['value']
        print("ny")
        param_dict['ttLength'] = int(ttLength)
        ttWidth = data['results']['bindings'][0]['ttWidth']['value']
        param_dict['ttWidth'] = int(ttWidth)
        ttHeight = data['results']['bindings'][0]['ttheight']['value']
        param_dict['ttHeight'] = int(ttHeight)
        legHeight = data['results']['bindings'][0]['legHeight']['value']
        param_dict['legHeight'] = int(legHeight)
        legDiameter =data['results']['bindings'][0]['legDiameter']['value']
        param_dict['legDiameter'] = int(legDiameter)

        print("her kommer det nye params: \n", param_dict)
        return param_dict
    
