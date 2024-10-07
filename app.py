import http.server
import socketserver
import json
import os

PORT = 8000
DATA_FILE = "data.json"

# Helper function to load data from JSON file
def load_applications():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

#Handler = http.server.CGIHTTPRequestHandler

# Custom request handler class
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/applications':
            applications = load_applications()
            self.path = 'list.html'
            with open(self.path, 'r') as file:
                content = file.read()
                # Replace placeholder with actual application data
                app_table_rows = ''.join(
                    f"<tr><td>{app['first_name']}</td><td>{app['last_name']}</td>"
                    f"<td>{app['employee_id']}</td><td>{app['start_date']}</td>"
                    f"<td>{app['end_date']}</td><td>{app['submitted_at']}</td></tr>"
                    for app in applications
                )
                content = content.replace('{{ applications }}', app_table_rows)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            return
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self) 

with socketserver.TCPServer(("0.0.0.0", PORT), MyHttpRequestHandler) as httpd:
    httpd.server_name = "test"
    httpd.server_port = PORT
    print("serving at port", PORT)
    httpd.serve_forever()
