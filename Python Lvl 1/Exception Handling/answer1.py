def display(name, deposit_amount, cost_per_day):
    """
    Function to validate and display customer details
    
    Args:
        name (str): Customer name
        deposit_amount (float): Deposit amount
        cost_per_day (float): Cost per day
    """
    try:
        # Type checking for input parameters
        if not isinstance(name, str):
            raise ValueError("Invalid name type")
        
        # Convert inputs to float and validate
        deposit = float(deposit_amount)
        cost = float(cost_per_day)
        
        # Print details if validation passes
        print(name)
        print(deposit)
        print(cost)
    
    except (ValueError, TypeError):
        # Handle any type conversion or validation errors
        print("Invalid Input format")

def main():
    try:
        # Read input from user
        name = input()
        deposit_amount = input()
        cost_per_day = input()
        
        # Call display function with inputs
        display(name, deposit_amount, cost_per_day)
    
    except Exception:
        # Catch any unexpected errors
        print("Invalid Input format")

# Execute the main function
if __name__ == "__main__":
    main()
