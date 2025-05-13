def read_and_write_file():
    filename = input("Enter the filename to read from: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content read successfully.")
        
        modified_content = content.upper()

        new_filename = input("Enter the new filename to write to: ")
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to {new_filename} successfully.")

    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_and_write_file()