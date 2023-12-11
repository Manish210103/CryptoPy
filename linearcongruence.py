from tkinter import *

def solve():
    a = int(a_entry.get())
    b = int(b_entry.get())
    n = int(n_entry.get())
    d = gcd(a, n)
    steps = []
    steps.append(f"gcd({a},{n}) = {d}")
    # If GCD is 1 and if the remainder of b and is 0 the finding it has a unique or no solution.
    if d == 1:
        if b % d == 0:
            x = pow(a, -1, n) * b % n
            steps.append(f"The unique solution is x = {x}")
        else:
            steps.append("The equation has no solution")
    # If there is solution finding how many solutions are there.
    elif d > 1 and b % d == 0:
        a1 = a // d
        b1 = b // d
        n1 = n // d
        x0 = pow(a1, -1, n1) * b1 % n1
        solutions = [x0 + k * n1 for k in range(d)]
        steps.append(f"Equation has {d} solutions")
        steps.append(f"x = {x0} + k({n1})")
        steps.append(f"x = {', '.join(str(x0 + k * n1) for k in range(d))}")
    else:
        steps.append("The equation has no solution")
    result_label.config(text="\n".join(steps))
# Finding the GCD and appending it to steps list.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

root = Tk()
root.title("Linear Congruence Solver")
# Getting the input in the tkinter box by get().
a_label = Label(root, text="Enter a:")
a_label.pack()
a_entry = Entry(root)
a_entry.pack()

b_label = Label(root, text="Enter b:")
b_label.pack()
b_entry = Entry(root)
b_entry.pack()

n_label = Label(root, text="Enter n:")
n_label.pack()
n_entry = Entry(root)
n_entry.pack()

solve_button = Button(root, text="Solve", command=solve)
solve_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()