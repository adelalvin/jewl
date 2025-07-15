import tkinter as tk

def only_numbers(char):
    # Allow digits and at most one dot (for decimals)
    if char in "0123456789.":
        # Only one dot allowed
        widget = root.focus_get()
        if char == ".":
            # Don't allow more than one dot in the field
            value = widget.get()
            if "." in value:
                return False
        return True
    return False

def calculate_price(*args):
    try:
        weight = float(weight_entry.get())
        rate = float(rate_entry.get())
        making_per_gram = float(making_entry.get())
        other = float(other_entry.get())
        profit_percent = float(profit_entry.get())

        gold_price = weight * rate
        making_total = weight * making_per_gram
        subtotal = gold_price + making_total + other
        profit = (profit_percent / 100) * subtotal
        total_before_tax = subtotal + profit
        vat = 0.05 * total_before_tax  # 5% VAT
        final_price = total_before_tax + vat

        results = [
            ("Gold Price", f"AED {gold_price:,.2f}"),
            ("Making Charges (Total)", f"AED {making_total:,.2f}"),
            ("Other Charges", f"AED {other:,.2f}"),
            ("Subtotal", f"AED {subtotal:,.2f}"),
            (f"Profit (@{profit_percent:.2f}%)", f"AED {profit:,.2f}"),
            ("Total Before Tax", f"AED {total_before_tax:,.2f}"),
            ("VAT (5%)", f"AED {vat:,.2f}")
        ]

        # Update grid labels
        for i, (label, value) in enumerate(results):
            result_labels[i][1].config(text=value, bg="white", font=table_font)
            result_labels[i][0].config(bg="white", font=table_font)

        # Final Price: Highlighted in green
        result_labels[-1][0].config(text="Final Price", bg="#44bb66", font=final_font, fg="white")
        result_labels[-1][1].config(text=f"AED {final_price:,.2f}", bg="#44bb66", font=final_font, fg="white")
    except Exception:
        for row in result_labels:
            row[1].config(text="--", bg="white", font=table_font)
            row[0].config(bg="white", font=table_font)
        result_labels[-1][1].config(text="--", bg="#44bb66", font=final_font, fg="white")
        result_labels[-1][0].config(bg="#44bb66", font=final_font, fg="white")

def reset_fields():
    weight_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    making_entry.delete(0, tk.END)
    other_entry.delete(0, tk.END)
    profit_entry.delete(0, tk.END)
    other_entry.insert(0, "0")
    profit_entry.insert(0, "0")
    # Reset result labels
    for i, (row_label, row_value) in enumerate(result_labels):
        row_label.config(bg="white", font=table_font, fg="black")
        row_value.config(text="--", bg="white", font=table_font, fg="black")
    # Final Price: Highlighted in green
    result_labels[-1][0].config(bg="#44bb66", font=final_font, fg="white")
    result_labels[-1][1].config(bg="#44bb66", font=final_font, fg="white")

root = tk.Tk()
root.title("Jewelry Store Gold Price Calculator - UAE")
root.geometry("720x730")
root.configure(bg="#f7f7f7")

# Font settings
large_font = ("Arial", 24)
entry_font = ("Arial", 24)
table_font = ("Arial", 20)
final_font = ("Arial", 28, "bold")

# Only allow numbers in input boxes
vcmd = (root.register(only_numbers), "%S")

# Inputs
tk.Label(root, text="Gold Weight (grams):", font=large_font, bg="#f7f7f7").pack(pady=7)
weight_entry = tk.Entry(root, font=entry_font, width=16, validate="key", validatecommand=vcmd)
weight_entry.pack(pady=7, ipady=10)

tk.Label(root, text="Gold Rate per gram (AED):", font=large_font, bg="#f7f7f7").pack(pady=7)
rate_entry = tk.Entry(root, font=entry_font, width=16, validate="key", validatecommand=vcmd)
rate_entry.pack(pady=7, ipady=10)

tk.Label(root, text="Making Charges per gram (AED):", font=large_font, bg="#f7f7f7").pack(pady=7)
making_entry = tk.Entry(root, font=entry_font, width=16, validate="key", validatecommand=vcmd)
making_entry.pack(pady=7, ipady=10)

tk.Label(root, text="Other Charges (AED):", font=large_font, bg="#f7f7f7").pack(pady=7)
other_entry = tk.Entry(root, font=entry_font, width=16, validate="key", validatecommand=vcmd)
other_entry.pack(pady=7, ipady=10)
other_entry.insert(0, "0")

tk.Label(root, text="Profit Margin (%):", font=large_font, bg="#f7f7f7").pack(pady=7)
profit_entry = tk.Entry(root, font=entry_font, width=16, validate="key", validatecommand=vcmd)
profit_entry.pack(pady=7, ipady=10)
profit_entry.insert(0, "0")

# Reset Button
reset_btn = tk.Button(root, text="Reset", font=large_font, width=10, bg="#ef5350", fg="white", command=reset_fields)
reset_btn.pack(pady=7)

# Results Table
table_frame = tk.Frame(root, bg="#f7f7f7")
table_frame.pack(pady=15)

labels = [
    "Gold Price",
    "Making Charges (Total)",
    "Other Charges",
    "Subtotal",
    "Profit (%)",
    "Total Before Tax",
    "VAT (5%)",
    "Final Price"
]

result_labels = []
for i, label in enumerate(labels):
    row_label = tk.Label(table_frame, text=label, anchor="w", width=24, font=table_font, bg="white", pady=7)
    row_value = tk.Label(table_frame, text="--", anchor="e", width=16, font=table_font, bg="white", pady=7)
    row_label.grid(row=i, column=0, sticky="w", padx=(7, 5), pady=3)
    row_value.grid(row=i, column=1, sticky="e", padx=(5, 7), pady=3)
    result_labels.append((row_label, row_value))

# Final Price initial highlight (green)
result_labels[-1][0].config(bg="#44bb66", font=final_font, fg="white")
result_labels[-1][1].config(bg="#44bb66", font=final_font, fg="white")

# Bindings for auto-calc
for entry in [weight_entry, rate_entry, making_entry, other_entry, profit_entry]:
    entry.bind("<KeyRelease>", calculate_price)

root.mainloop()
pip install pyinstaller
