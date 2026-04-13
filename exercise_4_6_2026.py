# user input
text = input("Enter a word or sentence: ")

# remove spaces and convert to lowercase
cleaned = text.replace(" ", "").lower()

# Check if palindrome
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

