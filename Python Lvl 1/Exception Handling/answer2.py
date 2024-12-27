def calculate_sum(count, numbers):
    """
    Calculate sum of numbers with exception handling
    
    Args:
        count (int): Expected number of values
        numbers (list): List of number strings
    """
    try:
        # Check if number of values matches expected count
        if len(numbers) < count:
            raise IndexError("list index out of range")
        
        # Convert string numbers to integers and calculate sum
        total_sum = sum(int(num) for num in numbers[:count])
        print(total_sum)
    
    except IndexError:
        # Handle insufficient number of values
        print("list index out of range")
    
    except ValueError:
        # Handle invalid number conversion
        print("Invalid input")

def main():
    try:
        # Read count of values
        count = int(input())
        
        # Read space-separated numbers
        numbers = input().split()
        
        # Call sum calculation function
        calculate_sum(count, numbers)
    
    except ValueError:
        # Handle invalid count input
        print("Invalid input")

# Execute the main function
if __name__ == "__main__":
    main()
