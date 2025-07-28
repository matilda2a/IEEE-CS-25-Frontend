#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

username = form.getvalue("username", "")
password = form.getvalue("password", "")
mobile = form.getvalue("mobile", "")
email = form.getvalue("email", "")
subject = form.getvalue("subject", "")
hidden = form.getvalue("hidden_field", "")

print(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Form Result</title>
</head>
<body>
    <h2>Received Data:</h2>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Password:</strong> {password}</p>
    <p><strong>Mobile:</strong> {mobile}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Subject:</strong> {subject}</p>
    <p><strong>Hidden Field:</strong> {hidden}</p>
</body>
</html>
""")
