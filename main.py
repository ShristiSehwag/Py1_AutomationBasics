# Define the file name 
file_name = "automated_file.txt"

# Define the text to write 
text = "Hello! This is an automated file with text."

# Open the file in write mode (this will create the file if it doesn't exist) 
with open(file_name, 'w') as file: 
    file.write(text) 

print(f"File '{file_name}' has been created and the message has been written.")

