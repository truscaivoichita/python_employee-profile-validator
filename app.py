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

# Step 10
# The .lower() method converts all characters in a string to lowercase. This is useful for normalizing email addresses:

# Example Code
# upperGreet = 'HELLO WORLD'
# lowerGreet = upperGreet.lower()
# print(lowerGreet)  # Output: hello world
# You can call both .strip() and .lower() on a string this way:

# Example Code
# messy = '  HELLO WORLD  '
# clean = messy.strip().lower()
# print(clean)  # Output: hello world
# Create a variable messy_email and assign it the string SARAH.DAVIS@COMPANY.COM with two leading spaces and two trailing spaces.

# Also, call .strip().lower() on messy_email and assign the result to a variable clean_email.

# Then print both so that the output reads:

# Example Code
# Original email: '  SARAH.DAVIS@COMPANY.COM  '
# Cleaned email: 'sarah.davis@company.com'
messy_email = '  SARAH.DAVIS@COMPANY.COM  '
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

# Step 11
# The .upper() method converts all characters to uppercase. This is useful for name badges or headings:

# Example Code
# name = 'sarah davis'
# badge = name.upper()
# print(badge)  # Output: SARAH DAVIS
# Create a variable named name_badge and assign it the result of calling the .upper() method on clean_name.

# Then print name_badge so that the output reads: Name badge: SARAH DAVIS.
name_badge = clean_name.upper()
print(f"Name badge: {name_badge}")

# Step 12
# You already used .find() and slicing on the email variable. Now you will use the same technique on clean_email.

# Find the position of the @ character in clean_email and store it in at_pos. Then use slicing to extract everything before @ and store it in email_user.

# Then print clean_email and email_user so that the output reads:

# Example Code
# Email: sarah.davis@company.com
# Username: sarah.davis
at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]
print(f'Email: {clean_email}')
print(f'Username: {email_user}')

# Step 13
# The .replace(old, new) method replaces every occurrence of the substring old with another, new. You can also chain it with other methods. For example:

# Example Code
# text = 'john.doe'
# name = text.replace('.', ' ').title()
# print(name)  # Output: John Doe
# Replace . with a single space in email_user, and then call .title() on the result. Assign the result to a variable named display_name.

# Then print display_name so that the output reads: Display name: Sarah Davis.
display_name = email_user.replace(".", " ").title()
print(f'Display name: {display_name}')
