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
username =email[:at_position]
print(f'Username: {username}')
