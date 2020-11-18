import web_server
import writeDFA
import kbe_requestor

main()

def main():

    HOST_NAME = '127.0.0.1' 
    PORT_NUMBER = 1234 

    #1. Setup servers
    URL = "http://127.0.0.1:3030/kbe"
    requestor = kbe_requestor(URL)
    #2. When form submit:
        #How can we do an action when the form submits??
        #1. Post to Fuseki
        #2. Get from Fuseki
        #3. Make DFA file
    return
