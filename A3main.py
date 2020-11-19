import web_server
import writeDFA
import kbe_requestor

from http.server import BaseHTTPRequestHandler, HTTPServer
#import BaseHTTPServer
import time
import requests
import json

def main():

    HOST_NAME = '127.0.0.1' 
    PORT_NUMBER = 1234 

    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), web_server.MyHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

    return


main()