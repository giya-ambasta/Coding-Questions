def main():
    # Read number of lines for first file
    n1 = int(input())
    
    # Create and write to input1.txt
    with open('input1.txt', 'w') as file1:
        for _ in range(n1):
            line = input()
            file1.write(line + '\n')
    
    # Read number of lines for second file
    n2 = int(input())
    
    # Create and write to input2.txt
    with open('input2.txt', 'w') as file2:
        for _ in range(n2):
            line = input()
            file2.write(line + '\n')
    
    # Read lines from both files
    with open('input1.txt', 'r') as file1, open('input2.txt', 'r') as file2:
        # Convert file contents to sets for efficient comparison
        lines1 = set(file1.read().splitlines())
        lines2 = set(file2.read().splitlines())
        
        # Find common lines
        common_lines = sorted(lines1.intersection(lines2))
        
        # Print common lines
        for line in common_lines:
            print(line)

# Execute the program
if __name__ == "__main__":
    main()
