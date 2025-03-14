def read_file(filename):
 
    with open(filename, 'r') as file:
        return file.readlines()

def write_file(filename, content):
 
    with open(filename, 'w') as file:
        file.writelines(content)

def modify_content(lines):
   
    return [line.upper() for line in lines]


input_filename = input("Enter the filename to read: ")
output_filename = input("Enter the filename to write the modified content: ")
try:
     
    lines = read_file(input_filename)   
    modified_lines = modify_content(lines)
        
    write_file(output_filename, modified_lines)   
    print(f"Modified content has been written to '{output_filename}'.")
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except IOError:
    print(f"Error: The file '{input_filename}' cannot be read.")
)

