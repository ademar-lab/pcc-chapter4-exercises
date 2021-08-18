# Create a list containing my favorite pizzas
my_pizzas = ["peperoni", "vegetarian", "italian sausage"]
for my_pizza in my_pizzas:
    print(f"I love {my_pizza} pizza")

print("\nI really love pizza! It is my favorite food but I don't eat it very "
      "often.\nI like to think that I'm a very healthy person, so I kind of "
      "take care of what I eat. I think everybody knows pizza is not very good "
      "for you, so when I eat it I make sure I enjoy every bite.\n")

# Create a copy of my favorite pizzas
friend_pizzas = my_pizzas[:]
my_pizzas.append("hawaiian")
friend_pizzas.append("anchovies")

# Print the two different lists of pizzas
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

