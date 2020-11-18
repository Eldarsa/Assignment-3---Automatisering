
thePath = "/product_info?pname=Enter+table+name&ttLength=Tabletop+lenght&ttWidth=Tabletop+width&ttHeight=Tabletop+height&legHeight=Leg+height&legDiameter=Leg+diameter"

split_by_q = thePath.split("?")
param_str = split_by_q[1]
key_value_pairs = param_str.split("&")

key_value_dict = dict() #Save to dict so that it is easier to move around
for pair in key_value_pairs:
    parts = pair.split("=")
    key_value_dict[parts[0]] = parts[1]

pname = key_value_dict["pname"]
ttLenght = key_value_dict["ttLength"]
ttWidth = key_value_dict["ttWidth"]
ttHeight = key_value_dict["ttHeight"]
legHeight = key_value_dict["legHeight"]
legDiameter = key_value_dict["legDiameter"]

print(key_value_dict)
print(legDiameter)