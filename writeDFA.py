def write_DFA(template_path, param_dict):

    templatefile = open(template_path, "r")
    newfile = open("DFAs/"+ str(param_dict["pname"]) + ".dfa", "w+")

    for line in templatefile:


        #Check if <* is start of a word
        print(line)
        #print("\n")
        newfile.write(line)

    templatefile.close()
    newfile.close()

if __name__ == "__main__":
    
    #temp_path = "C:/Users/Bruker/OneDrive - NTNU/Coding/Automatisering av ingeniørarbeid/Assignment 3/DFAs/table.dfa"
    temp_path = "DFAs/template/table.dfa"
    param_dict = {"pname": "Taaaable"}

    write_DFA(temp_path, param_dict)

