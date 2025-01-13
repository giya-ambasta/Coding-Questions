def find_highest_price_item():
    # Read number of items
    n = int(input())
    
    # Create an empty dictionary to store items and prices
    items_dict = {}
    
    # Input items and prices
    for _ in range(n):
        # Split input into item name and price
        item, price = input().split()
        
        # Convert price to float and store in dictionary
        items_dict[item] = float(price)
    
    # Find item with maximum price
    highest_price_item = max(items_dict, key=items_dict.get)
    
    # Print item with its price
    print(f"{highest_price_item} {items_dict[highest_price_item]}")

# Call the function
find_highest_price_item()
