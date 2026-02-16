class CustomerManager:
    def __init__(self, customers):
        self.customers = customers

    def display_customers(self, customers=None):
        if customers is None:
            customers = self.customers
        
        """Displays all customer records."""
        for cust_id, details in customers.items():
            print(
                f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}"
            )

    def filter_customers_by_city(self, city):
        filtered_customers = {
            cust_id: details # output
            for cust_id, details in self.customers.items() # loop
            if details["location"].lower() == city.lower() #filter
        }

        if filtered_customers:
            print(f"\nCustomers in {city}:")
            self.display_customers(filtered_customers)
        else:
            print(f"\nNo customers found in {city}.")

    def get_unique_locations(self):
        customer_locations = {customer["location"] for customer in self.customers.values()}
        print(f"\nUnique customer locations:", customer_locations)
        
    
    def update_customer_location(self, cust_id, new_location):
        customers = self.customers
        if cust_id in customers:
            old_location = customers[cust_id]["location"]
            customers[cust_id]["location"] = new_location
            print(f"\nUpdated {customers[cust_id]['name']}'s location from {old_location} to {new_location}.")
        else:
            print("\nCustomer not found.")
        
           