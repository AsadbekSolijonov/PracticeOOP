# OCP - Open Closed Principle

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
    def pay(self, orr, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, orr, security_code):
        print('Processing debit payment type.')
        print(f'Verifying security code:{security_code}')
        orr.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, orr, security_code):
        print('Processing credit payment type.')
        print(f'Verifying security code:{security_code}')
        orr.status = 'paid'


class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, orr, security_code):
        print('Processing PayPal payment type.')
        print(f'Verifying security code: {security_code}')
        orr.status = 'paid'


order = Order()
order.add_item('Kilka', 1, 8000)
order.add_item('Non', 2, 4000)
order.add_item('Go`sht', 1, 85000)

print(f"Total sum: {order.total_price():,.2f} so'm")
payment = DebitPaymentProcessor()
payment.pay(order, 1234)
