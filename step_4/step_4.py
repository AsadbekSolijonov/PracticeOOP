# Liskov Substitution - Liskov almashtirish
from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for index in range(len(self.items)):
            total += self.quantities[index] * self.prices[index]
        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, orr):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, orr):
        print('Processing debit payment type.')
        print(f'Verifying security code:{self.security_code}')
        orr.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, orr):
        print('Processing credit payment type.')
        print(f'Verifying security code:{self.security_code}')
        orr.status = 'paid'


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def pay(self, orr):
        print('Processing paypal payment type.')
        print(f'Verifying email address :{self.email}')
        orr.status = 'paid'


order = Order()
order.add_item('Kilka', 1, 8000)
order.add_item('Non', 2, 4000)
order.add_item('Go`sht', 1, 85000)

print(f"Total sum: {order.total_price():,.2f} so'm")
payment = PayPalPaymentProcessor('iamsolijonovasadbek@gmail.com')
payment.pay(order)
