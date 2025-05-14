# Ask the user for the name of the file to read
filename = input("Enter the name of the file to read (e.g., input.txt): ")

try:
    # Try to open the file in read mode
    with open(filename, 'r') as file:
        content = file.read()
        
    # Modify the content — let's just make it uppercase for this example
    modified_content = content.upper()

    # Write the modified content to a new file
    with open('output.txt', 'w') as new_file:
        new_file.write(modified_content)

    print("Done! The modified content has been saved to 'output.txt'.")

except FileNotFoundError:
    print(" Oops! The file you entered does not exist.")
except Exception as e:
    print(f" Something went wrong: {e}")

