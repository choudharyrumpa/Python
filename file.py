import re   # Regular expressions for finding patterns like emails

# Open the file safely using 'with' (it closes automatically after use)
with open("file.txt", "r") as f:
    data = f.read()  # Read the entire content of the file

# Print the file content (optional - remove if not needed)
print("File Content:\n", data)

# Use regex to extract all email addresses from the text
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)

# Print all extracted emails
print("\nExtracted Emails:")
for email in emails:
    print(email)

# If no emails found, inform the user
if not emails:
    print("No email addresses found in the file.")
