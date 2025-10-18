# File Handling in Python

try:
    # Opening a file in write mode ('w')
    file = open("example.txt", "w")
    
    # Writing data to the file
    file.write("Hello, this is a file handling example!\n")
    file.write("Python makes working with files easy.\n")
    print(" Data written successfully!")

    # Closing the file
    file.close()

    # Reopening the same file in read mode ('r')
    file = open("example.txt", "r")
    
    # Reading and displaying file content
    content = file.read()
    print("\n File Content:")
    print(content)

except FileNotFoundError:
    print(" Error: File not found.")

except IOError:
    print(" Error: Problem while reading or writing the file.")

finally:
    # Ensuring the file is closed properly
    file.close()
    print(" File closed successfully.")
