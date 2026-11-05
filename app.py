# Step 1
# In this workshop, you will practice working with Python's string methods.

# Start by creating a variable named email and assign it the string alice.johnson@company.com.

email = 'alice.johnson@company.com'

# Step 2
# Remember from a previous workshop that you can use an f-string to include a variable inside a string, by writing an f before the opening quote and wrapping the variable in {}.

# Here's a reminder of how it works:

# Example Code
# name = 'Alice'
# print(f'Hello, {name}')  # Hello, Alice
# Now, print email so that the output reads: Email: alice.johnson@company.com.
print(f'Email: {email}')

# Step 3
# Sometimes, you may want to find the position of a specific character inside a string. Python provides the built-in .find() method for this purpose. It returns an integer representing the index (position) of the first occurrence of the given substring.

# Here's an example:

# Example Code
# text = 'hello'
# print(text.find('e'))  # 1
# Now, call the .find() method on email and pass it '@' to find the position of the at sign in the email string. Assign the result to a variable named at_position.

# Then print at_position so that the output reads: Position of @: 13.
at_position = email.find("@")
print(f'Position of @: {at_position}')

# Step 4
# Now that you know the position of @ in the email, you can extract the username, which is placed before the @ sign.

# In the previous workshop, you extracted a portion of a string using slicing. As a reminder, the syntax is:

# Example Code
# text = 'hello world'
# print(text[:5])  # hello
# Use slicing on email to extract everything before at_position, and store the result in a variable named username.

# Then print username so that the output reads Username: alice.johnson.
username = email[:at_position]
print(f'Username: {username}')

# Step 5
# You can check whether a substring exists inside a string using the in keyword. It returns True if the substring exists and False otherwise. Here's an example:

# Example Code
# sentence = 'I love Python'
# print('Python' in sentence) # True
# print('Java' in sentence) # False
# Create a variable named has_at that checks if the character @ is in email.

# Then print has_at so that the output reads: Has @ symbol: True.
has_at = '@' in email
print(f'Has @ symbol: {has_at}')

# Step 6
# Create another variable named has_com that checks if .com is in email.

# Then print has_com so that the output reads: Has .com: True.
has_com = '.com' in email
print(f'Has .com: {has_com}')

# Step 7
# Real-world data is often messy with extra spaces and inconsistent casing.

# Create a variable messy_name and assign it the string sARaH dAVis with two leading spaces and two trailing spaces. Then print it so that the output reads:

# Example Code
# Original name: '  sARaH dAVis  '
# You will clean this up in the coming steps.
messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

# Step 8
# The .title() method capitalizes the first letter of each word. Here is an example:

# Example Code
# lowercase = 'hello world'
# title_case = lowercase.title()
# print(title_case)  # Output: Hello World
# Create a variable named clean_name and assign it the result of calling .title() on messy_name.
# clean_name = messy_name.title()

# Step 9
# The .strip() method removes whitespace from both ends of a string.

# Example Code
# messy = '  hello world  '
# clean = messy.strip()
# print(clean)  # Output: hello world
# You can chain .strip() and .title() to remove whitespace from both ends of a string and capitalize the first letter of each word:

# Example Code
# messy = '  hello world  '
# clean = messy.strip().title()
# print(clean)  # Output: Hello World
# Update the value of clean_name to call .strip() on messy_name before .title().

# After that, print clean_name so that the output reads Cleaned name: 'Sarah Davis'.
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")
