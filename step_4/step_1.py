# Violating SRP - single responsibility prinsipini buzulish qoidasi.

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

    def pay(self, payment_type, security_code):
        if payment_type == 'debit':
            print('Processing debit payment type.')
            print(f'Verifying security code:{security_code}')
            self.status = 'paid'
        elif payment_type == 'credit':
            print('Processing credit payment type.')
            print(f'Verifying security code: {security_code}')
            self.status = 'paid'
        else:
            raise Exception('Unknown payment type, Please try again')


order = Order()
order.add_item('Kilka', 1, 8000)
order.add_item('Non', 2, 4000)
order.add_item('Go`sht', 1, 85000)

print(f"Total sum: {order.total_price():,.2f} so'm")
order.pay('debit', 1234)
