import re

def validate_name(name):
	return len(name) > 0 and ' ' not in name

def validate_pswd(password):
	return len(password) >= 8 and re.match(r"[0-9]", password) and re.match(r"[a-z][A-Z]", password) and  re.match(r'.*[!@#$%^&*(),.?":{}|<>].*', password)

def validate_email(email):
	return "@" in email and "." in email


if __name__ == "__main__":

	username = input("username:")
	password = input("password:")
	email = input("email:")

	print("Validation of username: " + str(validate_name(username)))
	print("Password validation: " + str(validate_password(password)))
	print("Email validation: " + str(validate_email(email)))
