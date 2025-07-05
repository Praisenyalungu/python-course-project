import tkinter as tk
from tkinter import messagebox
from datetime import datetime

foods = []
prices = []

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

def update_total():
    total = sum(prices)
    total_label.config(text=f"Total: R{total:.2f}")

def clear_cart():
    foods.clear()
    prices.clear()
    cart_listbox.delete(0, tk.END)
    update_total()

def save_cart():
    if not foods:
        messagebox.showinfo("Empty Cart", "There is nothing to save.")
        return

    try:
        with open("shopping_cart.txt", "w") as file:
            file.write("Shopping Cart\n")
            file.write("-" * 30 + "\n")
            for food, price in zip(foods, prices):
                file.write(f"{food} - R{price:.2f}\n")
            file.write("-" * 30 + "\n")
            file.write(f"Total: R{sum(prices):.2f}\n")
            file.write(f"Saved on: {datetime.now()}\n")
        messagebox.showinfo("Saved", "Cart saved to shopping_cart.txt!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Shopping Cart App")
root.geometry("400x500")
root.config(bg="#f0f0f0")

tk.Label(root, text="Shopping Cart", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Food Item:", bg="#f0f0f0").pack()
food_entry = tk.Entry(root, width=30)
food_entry.pack(pady=5)

tk.Label(root, text="Price (R):", bg="#f0f0f0").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack(pady=5)

tk.Button(root, text="Add to Cart", command=add_item, bg="#4CAF50", fg="white").pack(pady=10)

cart_listbox = tk.Listbox(root, width=45, height=10)
cart_listbox.pack(pady=10)

total_label = tk.Label(root, text="Total: R0.00", font=("Arial", 14), bg="#f0f0f0")
total_label.pack(pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Clear Cart", command=clear_cart, bg="#f44336", fg="white").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Save Cart", command=save_cart, bg="#2196F3", fg="white").grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Exit", command=exit_app, bg="#555", fg="white").grid(row=0, column=2, padx=10)

root.mainloop()
