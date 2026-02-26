
#age verifacation 

#input
age = int(input("enter your age "))

#the age check
if 0 <= age <= 120:
   print("valid age")
else:
   print("Invalid age")

#phone number check
phone = input("whats ypur phone number?")

if len(phone) >= 10:
   print("phone number has less than 10 digits")
else: 
   print("phone number valid")

password = input("please create password: ")

if len(password) < 8: 
   print("at least 8 chariters")

