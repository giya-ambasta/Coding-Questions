# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()
    
    # Reverse the entire string
    reversed_content = content[::-1]
    
    # Print the reversed string
    print(reversed_content)
