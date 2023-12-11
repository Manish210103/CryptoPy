import tkinter as tk
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1

def extended_euclidean_algorithm(a, b):
    # Initialize the table headers
    table = [["Q", "A1", "A2", "A3", "B1", "B2", "B3"]]

    # Initialize the initial values
    q, r = divmod(a, b)
    a1, a2, a3 = 1, 0, a
    b1, b2, b3 = 0, 1, b

    # Add the initial values to the table
    table.append([q, a1, a2, a3, b1, b2, b3])

    while b3 != 0:
        q, r = divmod(a3, b3)
        a1, a2, a3, b1, b2, b3 = b1, b2, b3, a1 - q * b1, a2 - q * b2, a3 - q * b3

        # Add the current iteration values to the table
        table.append([q, a1, a2, a3, b1, b2, b3])

    # Compute the GCD and the coefficients
    gcd = a3
    x, y = a1, a2

    # Check if a and b are relatively prime
    if gcd == 1:
        # Compute the inverses
        a_inv = x % b
        b_inv = y % a

        # Compute the linear combination
        linear_combination = "{}({}) + {}({}) = {}".format(a, a_inv, b, b_inv, gcd)

        # Return the results
        return table, gcd, a_inv, b_inv, linear_combination
    else:
        # Return the GCD only
        return table, gcd

def check_coprime():
    # Get the input numbers from the entry fields
    a = int(entry_a.get())
    b = int(entry_b.get())

    # Check if the input numbers are prime
    if are_coprime(a, b):
        # Compute extended Euclidean algorithm and get the table and results
        table, gcd, a_inv, b_inv, linear_combination = extended_euclidean_algorithm(a, b)

        # Clear the output text widget
        output_text.delete("1.0", tk.END)

        # Print the table
        for row in table:
            output_text.insert(tk.END, "{:<3} {:<3} {:<3} {:<3} {:<3} {:<3} {:<3}\n".format(*row))

        # Print the results
        output_text.insert(tk.END, "The numbers {} and {} are relatively prime.\n".format(a, b))
        output_text.insert(tk.END, "Their inverses are:\n")
        output_text.insert(tk.END, "a^-1 = {}\n".format(a_inv))
        output_text.insert(tk.END, "b^-1 = {}\n".format(b_inv))
        output_text.insert(tk.END, "The linear combination of {} and {} is:\n".format(a, b))
        output_text.insert(tk.END, "{}\n".format(linear_combination))
    else:
        # Compute the GCD only
        gcd = math.gcd(a, b)

        # Clear the output text widget
        output_text.delete("1.0", tk.END)

        # Print the results
        output_text.insert(tk.END, "The numbers {} and {} are not relatively prime.\n".format(a, b))
        output_text.insert(tk.END, "Their GCD is: {}\n".format(gcd))

# Create the main window
window = tk.Tk()
window.title("Coprime Checker")

# Create the input labels and entry fields
label_a = tk.Label(window, text="Enter the first number:")
label_a.pack()
entry_a = tk.Entry(window)
entry_a.pack()

label_b = tk.Label(window, text="Enter the second number:")
label_b.pack()
entry_b = tk.Entry(window)
entry_b.pack()

# Create the check button
check_button = tk.Button(window, text="Check", command=check_coprime)
check_button.pack()

# Create the output text widget
output_text = tk.Text(window, height=30, width=50)
output_text.pack()

# Start the main loop
window.mainloop()