def main():
    # Read number of lines to input
    n = int(input())
    
    # Open file and write input lines
    with open('input1.txt', 'w') as file:
        for _ in range(n):
            line = input()
            file.write(line + '\n')
    
    # Read file and analyze contents
    with open('input1.txt', 'r') as file:
        # Initialize counters
        alphabet_count = 0
        numeric_count = 0
        space_count = 0
        word_count = 0
        line_count = 0
        
        # Read file contents
        for line in file:
            line_count += 1
            
            # Count characters
            for char in line:
                if char.isalpha():
                    alphabet_count += 1
                elif char.isdigit():
                    numeric_count += 1
                elif char.isspace():
                    space_count += 1
        
        # Count words by splitting line
        words = ' '.join(line.strip() for line in open('input1.txt')).split()
        word_count = len(words)
        
        # Print results
        print(f"Alphabets: {alphabet_count}")
        print(f"Numerics: {numeric_count}")
        print(f"Spaces: {space_count}")
        print(f"Words: {word_count}")
        print(f"Lines: {line_count}")

# Execute the program
if __name__ == "__main__":
    main()
