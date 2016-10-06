from flask import render_template
import hashlib

def scanCSV(file):
	instream = open(file,'r')
	content = instream.read().strip()
	instream.close()
	return content

def appendCSV(file, string):
	outstream = open(file,'a')
	outstream.write(string)
	outstream.close()

def genList(string):
	L1 = string.split("\n")
	L2 = []
	for a in L1:
		a = a.split(",")
		L2 += [a]
	return L2

def task(username, password, action):
	userList = genList(scanCSV('data/users.csv'))
	if (action == 'Login'):
		for account in userList:
			if (username == account[0] and hashlib.md5(password).hexdigest() == account[1]):
				m = "Successfully logged in!"
				return render_template("authenticate.html", messageAuth = m)
			if (username == account[0] and not hashlib.md5(password).hexdigest() == account[1]):
				m = "Incorrect password."
				return render_template("login.html", messageLogin = m)
		m = "Username does not exist."
		return render_template("login.html", messageLogin = m)
	else:
		exists = False
		for account in userList:
			if (username == account[0]):
				exists = True
		if (exists):
			m = "The username already exists"
			return render_template("login.html", m)
		else:
			newUser = username + "," + hashlib.md5(password).hexdigest() + "\n"
			appendCSV('data/users.csv', newUser)
			m = "Account successfully created."
			return render_template("login.html", messageLogin = m)
