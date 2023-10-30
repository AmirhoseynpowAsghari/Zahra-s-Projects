all_customers = {}

def create_customer_dict():
    name = str(input("Hey! What's your name? "))
    product = str(input("What do you want? "))
    price = str(input("What is the price of " + product + "? "))
    number = int(input("How many " + product + " do you want? "))
    total_price = int(price) * number
    customer_dict = {"name": name, "Product": product, "price": price, "number": number, "Total Price (You must pay)": total_price}
    return customer_dict

while True:
    customer_dict = create_customer_dict()
    if customer_dict["name"] in all_customers:
        # Update existing customer dictionary
        existing_dict = all_customers[customer_dict["name"]]
        existing_dict["Product"] += ", " + customer_dict["Product"]
        existing_dict["price"] += ", " + customer_dict["price"]
        existing_dict["number"] += customer_dict["number"]
        existing_dict["Total Price (You must pay)"] += customer_dict["Total Price (You must pay)"]
    else:
        # Add new customer dictionary to all customers
        all_customers[customer_dict["name"]] = customer_dict
    print(all_customers)
