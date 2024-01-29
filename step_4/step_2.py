# SRP - Single Responsibility

class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor:
    def pay_debit(self, orr, security_code):
        print('Processing debit payment type.')
        print(f'Verifying security code:{security_code}')
        orr.status = 'paid'

    def pay_credit(self, orr, security_code):
        print('Processing credit payment type.')
        print(f'Verifying security code: {security_code}')
        orr.status = 'paid'


order = Order()
order.add_item('Kilka', 1, 8000)
order.add_item('Non', 2, 4000)
order.add_item('Go`sht', 1, 85000)

print(f"Total sum: {order.total_price():,.2f} so'm")
payment = PaymentProcessor()
payment.pay_debit(order, 1234)
