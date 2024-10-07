import http.server
import socketserver

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    httpd.server_name = "test"
    httpd.server_port = PORT
    print("serving at port", PORT)
    httpd.serve_forever()
