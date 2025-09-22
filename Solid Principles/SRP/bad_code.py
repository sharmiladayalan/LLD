

"""
    ===> A class should have only one reason to change - One responsibility.

    ===> if a class have a multiple things, changes for one reason can break
         or complicate the other responsibilites.
"""

"""
    ===> Why it Matters

    ===> Keeps code focused, easier to test, simple to modify
"""

"""
    ===> Violation symptoms :
    ===> Class has methods touhing multiple concerns
"""

class Order:

    def __init__(self, items, customer_email):
        self.items = items
        self.customer_email = customer_email

    def calculate_total_price(self):
        total = sum(int(item["price"]) * int(item["quantity"]) for item in self.items)
        return total

    def save_order_to_database(self):
        print(f"Saving order for {self.customer_email} to database")
        print("Order sucessfully saved")

    def send_confirmation_mail(self):
        print(f"Sending confirmation email {self.customer_email}...")
        print("Sucessfully sended email")

order = Order([{'name' : 'laptop', 'price' : '1000', 'quantity' : '2'}], "tvk@mail.com")
print(f"Total Price : {order.calculate_total_price()}")
order.save_order_to_database()
order.send_confirmation_mail()

        
