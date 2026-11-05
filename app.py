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
