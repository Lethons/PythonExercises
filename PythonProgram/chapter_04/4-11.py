pizza_list = ['cheese pizza', 'mushroom pizza', 'pepperoni pizza']
friend_pizzas = pizza_list[:]
pizza_list.append('hum pizza')
friend_pizzas.append('beef pizza')
print("My favorite pizzas are:")
for pizza in pizza_list:
    print(pizza)
print("My friend favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
