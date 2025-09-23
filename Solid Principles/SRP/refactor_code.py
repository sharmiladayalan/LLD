"""
    Each class has a single reason to change

    Order (calculate_total_price)
    OrderRepository (save_order)
    EmailService (send_email)
"""



class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total_price(self):
        total = sum(int(item['price']) * int(item['quantity']) for item in self.items)
        return total

class OrderRepository:
    def save_order(self, order, customer_email):
        print(f"Saving Order for {customer_email} to database...")

class EmailService:
    def send_email(self, order, customer_email):
        print(f"Sending confirmation email to {customer_email}")



order_items = [{'name': 'Laptop', 'price': '1000', 'quantity': '2'}]

customer_email = "tvk@mail.com"

order = Order(order_items)
order_repo = OrderRepository()
email_service = EmailService()

print(f"Total Price: {order.calculate_total_price()}")
order_repo.save_order(order, customer_email)
email_service.send_email(order, customer_email)