from customers.customer_manager import CustomerManager

# Initial dictionary of customers (students will enhance this later)
customers = {
    "cust_101": {"name": "Alice", "location": "New York", "purchases": ["Laptop", "Mouse"]},
    "cust_102": {"name": "Bob", "location": "Los Angeles", "purchases": ["Phone", "Charger"]},
    "cust_103": {"name": "Charlie", "location": "New York", "purchases": ["Tablet", "Headphones"]}
}

customer_manager = CustomerManager(customers)

print("\nAll Customers:")
customer_manager.display_customers()

customer_manager.filter_customers_by_city('New York')
customer_manager.get_unique_locations()
customer_manager.update_customer_location("cust_102", "San Francisco")

# Unique locations are not yet implemented (students will add them)
print("\nUnique Locations: (Not Implemented Yet)")

