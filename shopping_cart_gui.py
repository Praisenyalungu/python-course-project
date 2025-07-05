import tkinter as tk
from tkinter import messagebox

# Global lists
foods = []
prices = []

# Add item function
def add_item():
    food = food_entry.get()
    try:
        price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for price.")
        return

    if food:
        foods.append(food)
        prices.append(price)
        cart_listbox.insert(tk.END, f"{food} - R{price:.2f}")
        update_total()
        food_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Missing Item", "Please enter a food item.")

# Update total cost
def update_total():
    total = sum(prices)
    total_label.config(text=f"Total: R{total:.2f}")

# Clear cart
def clear_cart():
    foods.clear()
    prices.clear()
    cart_listbox.delete(0, tk.END)
    update_total()

# Exit app
def exit_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("Shopping Cart App")
root.geometry("400x450")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="Shopping Cart", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

# Food entry
tk.Label(root, text="Food Item:", bg="#f0f0f0").pack()
food_entry = tk.Entry(root, width=30)
food_entry.pack(pady=5)

# Price entry
tk.Label(root, text="Price (R):", bg="#f0f0f0").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack(pady=5)

# Add button
tk.Button(root, text="Add to Cart", command=add_item, bg="#4CAF50", fg="white").pack(pady=10)

# Cart display
cart_listbox = tk.Listbox(root, width=45, height=10)
cart_listbox.pack(pady=10)

# Total
total_label = tk.Label(root, text="Total: R0.00", font=("Arial", 14), bg="#f0f0f0")
total_label.pack(pady=5)

# Bottom buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Clear Cart", command=clear_cart, bg="#f44336", fg="white").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Exit", command=exit_app, bg="#555", fg="white").grid(row=0, column=1, padx=10)

# Run the app
root.mainloop()
