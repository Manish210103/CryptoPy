import tkinter as tk
from functools import reduce

# Function to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the least common multiple (LCM) of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)

# Function to calculate the modular inverse of a number 'a' modulo 'm'
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to solve the Chinese Remainder Theorem (CRT)
def chinese_remainder_theorem(equations):
    n_values, a_values = zip(*equations)
    N = reduce(lcm, n_values)  # Calculate the LCM of all 'n' values
    result = sum(a * N // n * mod_inverse(N // n, n) for n, a in zip(n_values, a_values)) % N  # Calculate partial results and final result
    return result

def create_input_fields():
    num_equations = int(entry.get())
    
    # Create labels and entry fields for 'n' and 'a' values for each equation
    for i in range(num_equations):
        n_label = tk.Label(window, text=f"Enter n{i + 1}:")
        n_label.pack()
        entry_n.append(tk.Entry(window))
        entry_n[i].pack()
        
        a_label = tk.Label(window, text=f"Enter a{i + 1}:")
        a_label.pack()
        entry_a.append(tk.Entry(window))
        entry_a[i].pack()
    
    create_inputs_button.config(state=tk.DISABLED)
    solve_button.config(state=tk.NORMAL)

def solve_crt():
    equations = []
    
    for i in range(len(entry_n)):
        n = int(entry_n[i].get())
        a = int(entry_a[i].get())
        equations.append((n, a))
    
    result = chinese_remainder_theorem(equations)
    
    # Display the result and steps on the Tkinter page
    result_text = "Chinese Remainder Theorem (CRT) Steps:\n\n"
    
    # Step 1: Formulate the System of Congruences
    result_text += "Step 1: Formulate the System of Congruences\n"
    for i, (n, a) in enumerate(equations, start=1):
        result_text += f"x ≡ {a} (mod {n})\n"
    
    # Step 2: Compute the Moduli Product
    result_text += "\nStep 2: Compute the Moduli Product\n"
    moduli_product = reduce(lambda x, y: x * y, [n for n, _ in equations])
    result_text += f"M = {moduli_product}\n"
    
    # Step 3: Compute the Individual Moduli
    result_text += "\nStep 3: Compute the Individual Moduli\n"
    individual_moduli = [moduli_product // n for n, _ in equations]
    for i, (n, _) in enumerate(equations, start=1):
        result_text += f"M{i} = {individual_moduli[i-1]}\n"
    
    # Step 4: Compute the Modular Inverses
    result_text += "\nStep 4: Compute the Modular Inverses\n"
    modular_inverses = [mod_inverse(individual_moduli[i-1], n) for i, (n, _) in enumerate(equations, start=1)]
    for i, inv in enumerate(modular_inverses, start=1):
        result_text += f"y{i} = {inv} (mod {equations[i-1][0]})\n"
    
    # Step 5: Calculate the Solution
    result_text += "\nStep 5: Calculate the Solution\n"
    result_text += f"x = "
    for i, (n, a) in enumerate(equations, start=1):
        individual_result = a * individual_moduli[i-1] * modular_inverses[i-1]
        result_text += f"{individual_result}"
        if i < len(equations):
            result_text += " + "
    
    # Step 6: Finalize the Solution
    result_text += "\n\nStep 6: Finalize the Solution\n"
    result_text += f"x ≡ {result} (mod {moduli_product})"
    
    result_label.config(text=result_text)

# Create a new window
window = tk.Tk()
window.title("Chinese Remainder Theorem Solver")

# Add a label widget to prompt the user for input
input_label = tk.Label(window, text="Enter the number of equations (n):")
input_label.pack()

# Add an entry widget for the user to input the number of equations
entry = tk.Entry(window)
entry.pack()

# Add a button to create input fields for 'n' and 'a' values
create_inputs_button = tk.Button(window, text="Create Input Fields", command=create_input_fields)
create_inputs_button.pack()

# Entry widgets to input 'n' and 'a' values for each equation
entry_n = []
entry_a = []

# Add a button to solve the CRT
solve_button = tk.Button(window, text="Solve CRT", command=solve_crt, state=tk.DISABLED)
solve_button.pack()

# Add a label widget to display the result and steps
result_label = tk.Label(window, text="", justify="left")
result_label.pack()

# Start the main event loop
window.mainloop()
