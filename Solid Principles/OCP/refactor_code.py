
"""
    ==> We difne a common abstarction for processor and extnd it for new payment type
"""

from abc import ABC, abstractmethod

class PaymentInterface(ABC):
     @abstractmethod
     def pay(self, amount : float):
          pass
     
class CardPayment(PaymentInterface):
     def pay(self, amount):
          print(f"processing {amount} Using Card Payment")

class PaypalPayment(PaymentInterface):
     def pay(self, amount):
          print(f"processing {amount} Using Paypal Payment")

class UpiPayment(PaymentInterface):
     def pay(self, amount):
          print(f"processing {amount} Using Upi Payment")

class GpayPayment(PaymentInterface):
     def pay(self, amount):
          print(f"processing {amount} Using Gpay Payment")

card_payment = CardPayment()
paypal_payment = PaypalPayment()
upi_payment = PaypalPayment()

card_payment.pay(3000)
paypal_payment.pay(5000)
upi_payment.pay(3000.05)


"""
    ==> Payment is never change
    ==> Adding BitcoinPayment = just create a new class
    ==> The system is extensible without modification
"""
