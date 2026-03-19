colors = ["red", "blue", "white"]
numbers = [10, 20, 30]
print(f"colors: {colors}")
print(f"numbers: {numbers}")

temp = [72, 75, 78]
temp[0] = 70
print(temp)

word = "hello"
#word[0] = "J"
#type error due to being string and not mutable 

original = [10, 20, 30]
alist = original
alist[1] = 200
#origioal is now [10, 200, 30] because alist and original are referencing the same list in memory.
print(f"original: {original}")
print(f"alist: {alist}")

animals = ["cat", "dog", "bird", "fish", "hamster"]
print(animals[0])
print(animals[-1])

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
months[1] = "February"
print(months)
print(len(months))
print(len(months) // 2)
print(len(months) - 1)

data = [100, 200, 300]
empty = []
if len(data) > 0:
   print(data[0])
else:
    print("The list is empty.")


if len(empty) > 0:
    print(empty[0])
else:
    print("The 'empty' list is empty.")


if len(data) > 1:
    temp = data[0]
    data[0] = data[-1]
    data[-1] = temp
print(data)
#print(empty[0])
#index error because empty list has no elements to access at index 0

                                                                                   