import kbe_requestor
import writeDFA

template_path = "DFAs/template/table.dfa"

#This function is used in web_server in a way that interconnects the two files properly
def process_table(param_dict):

    #Set the initial URL connecting to the Fuseki-server
    URL = "http://127.0.0.1:3030/kbe"
    requestor = kbe_requestor.kbe_requestor(URL)

    requestor.insert(param_dict)
 
    tableParams = requestor.select(param_dict["pname"])

    writeDFA.write_DFA(template_path, tableParams)
    
    return