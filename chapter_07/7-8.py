sandwich_orders = ['beef sandwich', 'tuna sandwich', 'fruit sandwich']
finished_sandwich = []
while sandwich_orders:
    print("I made your %s." % sandwich_orders[0])
    finished_sandwich.append(sandwich_orders.pop(0))
print(finished_sandwich)
