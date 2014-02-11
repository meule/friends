#!/usr/bin/python

"""
Save this file as server.py
>>> python server.py 0.0.0.0 8001
serving on 0.0.0.0:8001

or simply

>>> python server.py
Serving on localhost:8000

You can use this to test GET and POST methods.

https://snipt.net/raw/f8ef141069c3e7ac7e0134c6b58c25bf/
http://stackoverflow.com/questions/13146064/simple-python-webserver-to-save-file

"""

import SimpleHTTPServer
import SocketServer
import logging
#import cgi

import sys

from os import curdir
from os.path import join as pjoin

dataFile='friends.json'

if len(sys.argv) > 2:
    PORT = int(sys.argv[2])
    I = sys.argv[1]
elif len(sys.argv) > 1:
    PORT = int(sys.argv[1])
    I = ""
else:
    PORT = 8000
    I = ""


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    store_path = pjoin(curdir, dataFile)

    def do_GET(self):
        logging.warning("======= GET STARTED =======")
        logging.warning(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.warning("======= POST STARTED =======")
        logging.warning(self.headers)

        length = self.headers['content-length']
        data = self.rfile.read(int(length))

        with open(self.store_path, 'a') as fh:
            fh.write('\n'+data.decode())

        self.send_response(200)

        #SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "@rochacbruno Python http server version 0.1 (for testing purposes only)"
print "Serving at: http://%(interface)s:%(port)s" % dict(interface=I or "localhost", port=PORT)
httpd.serve_forever()

