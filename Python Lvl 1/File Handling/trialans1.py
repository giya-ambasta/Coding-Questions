# Open the file in read mode
with open('test.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    
    # Split the content into words
    words = content.split()
    
    # Print even-length words
    for word in words:
        if len(word) % 2 == 0:
            print(word)
