def perform_integer_division():
    try:
        # Read number of test cases
        t = int(input())
        
        # Process each test case
        for _ in range(t):
            try:
                # Read input line and split into numerator and denominator
                a, b = map(int, input().split())
                
                # Perform integer division
                result = a // b
                print(result)
            
            except ZeroDivisionError:
                # Handle division by zero
                print("division by zero")
            
            except ValueError:
                # Handle invalid input values
                print("invalid literal for int() with base 10")
    
    except ValueError:
        # Handle invalid input for number of test cases
        print("Invalid number of test cases")

# Run the program
perform_integer_division()
