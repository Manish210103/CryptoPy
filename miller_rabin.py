import tkinter as tk
import random

def is_prime(n, k=5):
    # If the n is less than or equal to 3 then it is a prime number.
    if n <= 1 or n == 4:
        return False
    # Else d is initialised to (number - 1) and the remainder to 0.
    elif n <= 3:
        return True
    # Miller rabin test process starts.
    else:
        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
# This test is to check whether a number is prime or not.
def check_primality():
    n = int(entry.get())
    if is_prime(n):
        result = f"{n} is probably prime."
    else:
        result = f"{n} is composite."
    result_label.config(text=result)

# create a new window
window = tk.Tk()
window.title("Primality Test")

# add a label widget to prompt the user for input
input_label = tk.Label(window, text="Enter a number to check for primality:")
input_label.pack()

# add an entry widget for the user to input the number
entry = tk.Entry(window)
entry.pack()

# add a button to check the primality of the input number
check_button = tk.Button(window, text="Check Primality", command=check_primality)
check_button.pack()

# add a label widget to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# start the main event loop
window.mainloop()