# Initialize the variables
foods = []
prices = []
total = 0

# Continuous input loop
while True:
    food = input("Enter a food item (or type 'done' to finish): ")
    if food.lower() == 'done':
        break

    try:
        price = float(input(f"Enter the price for {food}: R"))
    except ValueError:
        print("Please enter a valid number for the price.")
        continue

    foods.append(food)
    prices.append(price)
    total += price

# Output the results
print("\nYou entered the following items:\n")
for i in range(len(foods)):
    print(f"{foods[i]} - R{prices[i]:.2f}")

print(f"\nTotal: R{total:.2f}")
