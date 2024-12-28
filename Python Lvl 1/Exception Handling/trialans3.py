try:
    # Get user input
    user_input = input()
    
    # Attempt to convert input to integer
    integer_value = int(user_input)
    
    # If conversion is successful, print "Valid Integer"
    print("Valid Integer")

except ValueError:
    # If conversion fails, print "Invalid Integer"
    print("Invalid Integer")
