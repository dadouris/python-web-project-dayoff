'''
CGI, short for Common Gateway Interface, is a protocol that enables
web servers to communicate with external programs or scripts to generate
dynamic content for web applications.
'''
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import json
from datetime import datetime
import os

DATA_FILE = "data.json"

# Helper function to load data from JSON file
def load_applications():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Helper function to save data to JSON file
def save_application(application):
    applications = load_applications()
    applications.append(application)
    with open(DATA_FILE, 'w') as file:
        json.dump(applications, file)

print("Executing SCRIPT")

form = cgi.FieldStorage() 

first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')
Emp_ID  = form.getvalue('Emp_ID')
Date_S  = form.getvalue('Date_S')
Date_E  = form.getvalue('Date_E')

if first_name ==None: first_name ="UNKNOWN"
if last_name==None:last_name = "UNKNOWN"


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Your application is successfuly submitted ({},{},{},{},{})</h2>".format(first_name, last_name, Emp_ID, Date_S, Date_E))
print("</body>")
print("</html>")

'''
from time import gmtime, strftime, time
timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
with open("logfile.txt", "a") as myfile:
    myfile.write(timestamp+" button pressed by <"+first_name+" "+last_name+">\n")
'''
# Create a new application
application = {
    'first_name': first_name,
    'last_name': last_name,
    'employee_id': Emp_ID,
    'start_date': Date_S,
    'end_date': Date_E,
    'submitted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}

# Save the application to the file
save_application(application)

