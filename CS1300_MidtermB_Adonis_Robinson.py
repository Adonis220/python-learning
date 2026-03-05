#BMI Calculator
Weight = input("Enter your weight in lbs or kg:")
Weight = float(Weight)
Height = input("Enter your height in inches or merters:")
Height = float(Height)
measurment_unit = input("enter nit system (I/M):")
if measurment_unit != "I" and measurment_unit != "M":
    Error = "invalid unit system"

if measurment_unit == "I":
    BMI = (Weight * 703) / (Height ** 2)
    print("Your BMI is:", BMI)
elif measurment_unit == "M":
    BMI = Weight / (Height ** 2)
    print("Your BMI is:", BMI)

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 24.5:
    print("Normal weight")
elif 25 <= BMI < 29.9:
    print("Overweight")
elif BMI >= 30:
    print("Obese")
else:
    print("Error calculating BMI.")
    print(Error)


# password strength checkr 
passcounter = 0

password = input("Enter a password: ")
if len(password) < 8:
    passlength = "Fail"
    passcounter += 1

else:
    passlength = "Pass"

if any(char.isupper() for char in password):
    uppercase = "Pass"
else:
    uppercase = "Fail"
    passcounter += 1

if any(char.islower() for char in password):
    lowercase = "Pass"
else:
    lowercase = "Fail"
    passcounter += 1
if any(char.isdigit() for char in password):
    digit = "Pass"
else:
    digit = "Fail"
    passcounter += 1

if any(not char.isalnum() for char in password):
    specialchar = "Pass"
else:
    specialchar = "Fail"
    passcounter += 1


if passcounter == 0:
    print("Password is strong.")
elif 1 <= passcounter <= 3:
    print("Password is moderate.")
elif 4 <= passcounter <= 5:
    print("Password is weak.")
else:
    print ("no password entered")

print(f"Length: {passlength}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Digit: {digit}")
print(f"Special Character: {specialchar}")
