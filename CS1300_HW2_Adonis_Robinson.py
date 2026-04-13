#problem 1-----------------------------------------------------------------
# 1. Gather input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
hobby = input("Enter your favorite hobby: ")
# 2. Convert names to title case
first_name = first_name.title()
last_name = last_name.title()
hobby = hobby.title()
# 3. Calculate age
current_year = 2026
age = current_year - birth_year
# 4. Create borders
top_border = "=" * 36
bottom_border = "-" * 36
# 5. Display formatted profile card
print(top_border)
print("USER PROFILE CARD")
print(top_border)
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print(bottom_border)
print("Thank you for creating your profile!")
print(top_border)
#problem 2-----------------------------------------------------------------
# Display title
print("=== TEXT ANALYZER ===")
# 1. Get user input
sentence = input("Enter a sentence: ")
# --- Analysis ---
print("\n--- Analysis Results ---")
# Total characters (with spaces)
total_chars = len(sentence)
# Total characters (without spaces)
chars_no_spaces = len(sentence.replace(" ", ""))
# Number of words
word_count = len(sentence.split())
# Number of vowels (case insensitive)
vowels = "aeiou"
vowel_count = 0
for char in sentence.lower():
	if char in vowels:
		vowel_count += 1
# Uppercase and lowercase versions
upper_version = sentence.upper()
lower_version = sentence.lower()
# Reversed sentence
reversed_sentence = sentence[::-1]
# Starts with capital letter
starts_capital = sentence[0].isupper() if sentence else False
# Ends with proper punctuation
ends_punctuation = sentence.endswith((".", "!", "?"))
# Display results
print(f"Total characters (with spaces): {total_chars}")
print(f"Total characters (without spaces): {chars_no_spaces}")
print(f"Number of words: {word_count}")
print(f"Number of vowels: {vowel_count}")
print(f"Uppercase version: {upper_version}")
print(f"Lowercase version: {lower_version}")
print(f"Reversed: {reversed_sentence}")
print(f"Starts with capital: {'Yes' if starts_capital else 'No'}")
print(f"Ends with punctuation: {'Yes' if ends_punctuation else 'No'}")
#problem 3-----------------------------------------------------------------
# user input
text = input("Enter a word or sentence: ")
# remove spaces and convert to lowercase
cleaned = text.replace(" ", "").lower()
# Check if palindrome
if cleaned == cleaned[::-1]:
	print("Palindrome")
else:
	print("Not a palindrome")