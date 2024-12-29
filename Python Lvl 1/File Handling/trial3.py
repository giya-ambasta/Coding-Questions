# Create the file with predefined content
def create_file():
    content = """Rugrats is an American animated television series.
The series premiered on August 11, 1991.
It was produced as part of Nickelodeon's commitment broadcast on December 11, 2001.
A picture book entitled The Rugrats'
Kwanzaa was adapted from the script.
The episode was released on VHS in 2001"""
    
    with open('test.txt', 'w') as file:
        file.write(content)

# Main program
def main():
    # Create the file first
    create_file()
    
    # Take input for line number
    n = int(input())
    
    # Open and read the file
    with open('test.txt', 'r') as file:
        # Read all lines
        lines = file.readlines()
        
        # Print lines starting after nth line
        for line in lines[n:]:
            print(line.strip())

# Execute the program
if __name__ == "__main__":
    main()
