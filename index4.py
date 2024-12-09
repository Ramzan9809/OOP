class Currency:
    def __init__(self, value):
        self.value = value
    
    def convert_to_som(self, exchange_rate):
        return round(self.value * exchange_rate)

    def print_valuta(self, currency_name):
        print(f'{self.value} {currency_name}')
    
class Dollar(Currency):
    exchange_rate = 86.80

    def convert_to_som(self):
        return super().convert_to_som(self.exchange_rate)

    def print_value(self):
        super().print_value('USD')

class Euro(Currency):
    exchange_rate = 91.12

    def convert_to_som(self):
        return super().convert_to_som(self.exchange_rate)

    def print_value(self):
        super().print_value('EURO')

dollar_list = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
euro_list = [Euro(5), Euro(10), Euro(50), Euro(100)]
for dollar in dollar_list:
    dollar.print_value()
    print(f'= {dollar.convert_to_som()} SOM')

# currency_in_usd = Currency(100, 'USD')
# amount_in_som = currency_in_usd.convert_to_som()
# print(f'{currency_in_usd.amount} {currency_in_usd.currency_code} = {amount_in_som:.2f} KGS')

# currency_in_eur = Currency(50, 'EUR')
# amount_in_som_eur = currency_in_eur.convert_to_som()
# print(f'{currency_in_eur.amount} {currency_in_eur.currency_code} = {amount_in_som_eur:.2f} KGS')
