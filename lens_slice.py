# Your code below:

#create new list 'toppings'
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#create new list 'prices', keeps track of how much each kind of slice costs
prices = [2,6,1,3,2,7,2]

#count number of times 2 appears in prices list
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#find length of 'toppings' list
num_pizzas = len(toppings)
print(num_pizzas)

#print statement:
print(f"We sell {num_pizzas} different kinds of pizza!")

#create 2d list with 'toppings' and 'prices'
pizza_and_prices = [[2,"pepperoni"], [6,"pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7,"anchovies"], [2,"mushrooms"]] 
#print(pizza_and_prices)

#sort 'pizza_and_prices' ascending order
pizza_and_prices.sort()
#print(pizza_and_prices)

#store first element as 'cheapest_pizza'
cheapest_pizza = pizza_and_prices[0]

#Dude walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!." Store last element in list as 'priciest_pizza'
priciest_pizza = pizza_and_prices[-1]

#remove anchovies from list - man got last slice
pizza_and_prices.pop(-1)
#print(pizza_and_prices)

#add new topping- 'peppers'
pizza_and_prices.insert(4, [2.5, "peppers"])
#print(pizza_and_prices)

#slice pizza_and_prices list & store 3 lowest coast pizzas for the 3 broke mice
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
