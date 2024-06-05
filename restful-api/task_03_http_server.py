#!/usr/bin/python3

import http.server as srv
import socketserver
import json
PORT = 8000
class Server(srv.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            jout = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(jout.encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            jout = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(jout.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')
            
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Server) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()
