print("Pastrami was sold out.")
sandwich_orders = ['pastrami', 'beef sandwich', 'pastrami',
                   'tuna sandwich', 'fruit sandwich', 'pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
