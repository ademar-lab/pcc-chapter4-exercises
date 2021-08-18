# Store the foods a buffet offers
foods_offered = ("lasagna", "pasta", "scrambled eggs", "waffles", "ice cream")

for food in foods_offered:
    print(food)

# This assignment should be rejected
try:
    foods_offered[1] = "fruit cocktail"
except:
    print("\nYou can't assign a tuple's item\n")

# Rewrite the whole tuple 
foods_offered = ("lasagna", "pasta", "scrambled eggs", "quesadillas", "pozole")

print(f"This is the new rewritten menu:")
for food in foods_offered:
    print(food)
