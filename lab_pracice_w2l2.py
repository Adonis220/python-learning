# What will each line print?
message = "Hello Python!"
print(message)
print(type(message))

number = 42
print(type(number))


#exercise 1.2 
# These lines have errors. Fix them to be valid AND follow PEP 8:
first_name = "Taylor"
user_age = 21
user_class = "Computer Science"
My_Score = 100
#  test to check if correct 
print(first_name)
print(user_age)
print(user_class)
print(My_Score)

#exercise 1.3
a = 256
b = 256
print("a =", a, "id(a) =", id(a))
print("b =", b, "id(b) =", id(b))
print("Same object?", id(a) == id(b))

print()

c = 257
d = 257
print("c = {c}, id(c) = {id(c)}")
print("d = {d}, id(d) = {id(d)}")
print("Same object? {id(c) == id(d)}")

# a and b share the same id because their id's are equal to each other
#c and d share the same id because their id's are equal to each other
# a and b have a diffrent id than c and d 

