# from http.server import BaseHTTPRequestHandler, HTTPServer

# class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

#     def do_GET(self):       # this is a function that should be called anytime a user visits my web server via GET request
#                             # 'self' here refers to the web server (ie the class above)

#         self.send_response(200)     # send response code of 200 - meaning the request is assumed to be OK

#         self.send_header("Content-type", "text/html")   # a hash/dictionary that has a header/key Content type and a value of html text
#         self.end_headers();

#         self.wfile.write(b"<!DOCTYPE html>")        #web page only needs Hello World, but this requires wrapping it in html
#                                                     # wfile.write method writes out or prints the contents in the parentheses / b = bytes
#         self.wfile.write(b"<html lang='en'>")
#         self.wfile.write(b"<head>")
#         self.wfile.write(b"<title>hello, title</title>")
#         self.wfile.write(b"<body>")
#         self.wfile.write(b"Hello World, finally")
#         self.wfile.write(b"</body>")
#         self.wfile.write(b"</html>")

# port = 5000

# server_address = ("0.0.0.0", port)                  # configuring server to listen on a port so you can run it
#                                                     #define server's address as 0.0.0.0 which is what IDE uses by default

# httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

# httpd.serve_forever()

#     # this is a long and ridiculous way to generate an http web server using python / this code must be thrown away 
#     # using flask will automate this all