

"""
    ==> Open and Close Principle (OCP);

    ==> A class should be open for extension but closed for modification ;

    ==> Open For Extension => We can add new behavior without touching exsiting code ;;

    ==> Closed for Modification => We don't risk breaking exsiting functionality by editing core logic ;;
"""

"""
    ==> You should be able to add new features by creating new classes, not by modifiying existing code ;;
"""

"""
    ==> Image a Billing System ;;

    *** Bad Way ***
    ==> If it has a gaint if / elif ladder to handle Credit_card, Paypal, upi, every time a new payment
        type comes, you modify the the core billing code

        its voilate (OCP);;

    *** Good Way ***
    ==> Instead of, if you define a PaymentProcess interface and add new Processors like CreditCardProcessor, PaypalProcessor, etc, 
        the billing system doesn't change

        respect (OCP);;
"""

class PaymentService:
    def process_payment(self, payment_type : str, amount : float):
        if payment_type == "Card":
            print(f"Processing {amount} using Card")
        elif payment_type == "Paypal":
            print(f"Processing {amount} using Paypal")
        elif payment_type == "Upi":
            print(f"Processing {amount} using Upi")
        else:
            raise ValueError("Unsupported Payment Type")
        
payment_serivce = PaymentService()
payment_serivce.process_payment("Card", 2000)
payment_serivce.process_payment("Upi", 4000)


"""
    ==> Problem
    ==> To add Bitcoin or strip, you must modify Process_payment

    ==> the class is not clossed for modification
"""
        

