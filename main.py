# File Creation
with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("12345\n")
    file.write("Another line with text and numbers: 9876\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File reading process completed.")

# File Appending
with open("my_file.txt", "a") as file:
    file.write("Appending line 1\n")
    file.write("Appending line 2\n")
    file.write("Appending line 3\n")
