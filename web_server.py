#******************************
#Web UI Example (web server) - HTML FORM
# Changed code to display values you have previously sent in the form.
# https://www.w3schools.com/python/ref_string_find.asp
# https://www.w3schools.com/python/ref_string_split.asp
#******************************
# https://wiki.python.org/moin/BaseHttpServer
# https://www.w3schools.com/graphics/svg_intro.asp

from http.server import BaseHTTPRequestHandler, HTTPServer
#import BaseHTTPServer
import time
import requests
import json

import table_processer as tp

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 

class Status():
    status = False

    def set(self):
        self.status = True

    def reset(self):
        self.status = False

    def get(self):
        return self.status

status = Status()

class MyHandler(BaseHTTPRequestHandler):

    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        #Parse incoming parameters
        thePath = s.path

        pname = "Enter table name"
        ttLenght = "Tabletop lenght"
        ttWidth = "Tabletop width"
        ttHeight = "Tabletop height"
        legHeight = "Leg height"
        legDiameter = "Leg diameter"



        if thePath.find("product_info") != -1:
        #Parse parameters.
        #/product_info?pname=Rocket&theight=8000&ttlenght=150
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

            #Send the dictionary to a function that processes the table, uploads it to Fuseki
            #and creates a DFA file:
            tp.process_table(key_value_dict)


        s.wfile.write(bytes("<p>Your accessed path: %s</p>" % s.path, "utf-8"))

        s.wfile.write(bytes('<!DOCTYPE html>', 'utf-8'))
        s.wfile.write(bytes('<html>', 'utf-8'))
        s.wfile.write(bytes('<body>', 'utf-8'))
        s.wfile.write(bytes('<h2>Products details</h2>', 'utf-8'))
        s.wfile.write(bytes('<form action="/product_info">', 'utf-8'))

        s.wfile.write(bytes('<label for="pname">Product name:</label><br>', 'utf-8'))
        s.wfile.write(bytes('<input type="text" id="pname" name="pname" value="' + pname + '"><br><br>', 'utf-8'))

        s.wfile.write(bytes('<label for="ttLength">Tabletop length (cm):</label><br>', 'utf-8'))
        s.wfile.write(bytes('<input type="text" id="ttLength" name="ttLength" value="'+ ttLenght +'"><br><br>', 'utf-8'))

        s.wfile.write(bytes('<label for="ttWidth">Tabletop width (cm):</label><br>', 'utf-8'))
        s.wfile.write(bytes('<input type="text" id="ttWidth" name="ttWidth" value="'+ ttWidth +'"><br><br>', 'utf-8'))

        s.wfile.write(bytes('<label for="ttHeight">Tabletop height (cm):</label><br>', 'utf-8'))
        s.wfile.write(bytes('<input type="text" id="ttHeight" name="ttHeight" value="' + ttHeight + '"><br><br>', 'utf-8'))

        s.wfile.write(bytes('<label for="legHeight">Leg height (cm):</label><br>', 'utf-8'))
        s.wfile.write(bytes('<input type="text" id="legHeight" name="legHeight" value="' + legHeight + '"><br><br>', 'utf-8'))

        s.wfile.write(bytes('<label for="legDiameter">Leg diameter (cm):</label><br>', 'utf-8'))
        s.wfile.write(bytes('<input type="text" id="legDiameter" name="legDiameter" value="' + legDiameter + '"><br><br>', 'utf-8'))

        s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
        s.wfile.write(bytes('</form>', 'utf-8'))
        s.wfile.write(bytes('<p>If you click the "Submit" button, the form-data will be sent to a page called "/product_info".</p>', 'utf-8'))
        s.wfile.write(bytes('</body></html>', 'utf-8'))
        

def checkStatus(data):
        data_ = json.loads(data)
        url = 'http://escop.rd.tut.fi:3000/RTU/SimCNV8/services/Z1'
        headers = {"Content-Type": "application/json"}
        # call get service with headers and params
        response = requests.post(url,json=data_)
        print("code:" + str(response.status_code))
        print("******************")
        print("headers:"+ str(response.headers))
        print("******************")
        print("content:"+ str(response.json()))
        if response.json()["PalletID"] != -1:
            status.set()
        else:
            status.reset()

if __name__ == '__main__':
        server_class = HTTPServer
        httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
        print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))