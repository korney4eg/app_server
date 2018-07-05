#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import time

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
  
  #Handler for the GET requests
  def do_GET(self):
    if self.path == '/slowly':
      time.sleep(15) 
      message = 'Am I too slow'
    elif self.path == '/release-kraken':
      message = 'Looks like it should start leaking'
    else:
      message = 'working normally'
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    self.wfile.write(message)
    return

try:
  #Create a web server and define the handler to manage the
  #incoming request
  server = HTTPServer(('', PORT_NUMBER), myHandler)
  print 'Started httpserver on port ' , PORT_NUMBER
  
  #Wait forever for incoming htto requests
  server.serve_forever()

except KeyboardInterrupt:
  print '^C received, shutting down the web server'
  server.socket.close()
