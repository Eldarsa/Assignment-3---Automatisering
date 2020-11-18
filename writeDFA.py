def write_DFA(template_path, param_dict):

    #Open template and new file to write to:
    templatefile = open(template_path, "r")
    data = templatefile.readlines()
    newfile = open("DFAs/"+ str(param_dict["pname"]) + ".dfa", "w+")

    #All parameters to change and what to change them with chronologically sorted to lists: 
    temp_mark = ["<*TABLE_TEMPLATE*>", "<*LEG_RADIUS*>", "<*LEG_HEIGHT*>", "<*TT_HEIGHT*>", "<*TT_LENGTH*>", "<*TT_WIDTH*>"]
    new_params = [param_dict["pname"], param_dict["legDiameter"] / 2, param_dict["legHeight"], param_dict["ttHeight"], param_dict["ttLength"], param_dict["ttWidth"]]

    #Replace all parameters and write to new file line for line
    for line in data:
        if temp_mark:
            line = line.split()
            for i in range(0,len(line)):
                if line[i] == temp_mark[0]:
                    marker_to_replace = temp_mark.pop(0) #Parameter replaced, can be removed from list for efficiency
                    replacement = new_params.pop(0) #Parameter inserted, can be removed from list for efficiency
                    line[i] = str(replacement) #Insert parameter
                    break
                else:
                    pass
            line = " ".join(line)
            print(line)
            newfile.write(line + "\n")
        else:
            print(line)
            newfile.write(line)

    #Close files
    templatefile.close()
    newfile.close()

if __name__ == "__main__":
    
    #temp_path = "C:/Users/Bruker/OneDrive - NTNU/Coding/Automatisering av ingeniørarbeid/Assignment 3/DFAs/table.dfa"
    temp_path = "DFAs/template/table.dfa"
    param_dict = {"pname": "Taaaable", "legHeight": 50, "ttHeight": 10, "ttLength": 100, "ttWidth": 50, "legDiameter": 10}

    write_DFA(temp_path, param_dict)

