import tkinter as tk
import subprocess

def choose_option():
    choice = option_var.get()
    if choice == 1:
        subprocess.call(["python", "extended_euc.py"])
    elif choice == 2:
        subprocess.call(["python", "miller_rabin.py"])
    elif choice == 3:
        subprocess.call(["python", "crt.py"])
    elif choice == 4:
        subprocess.call(["python", "linearcongruence.py"])
    elif choice == 5:
        window.destroy()

# create a new window
window = tk.Tk()
window.title("Choose an Option")

# add a frame widget to create a box around the process label
process_frame = tk.Frame(window, bg="white", padx=10, pady=10)
process_frame.pack()

# add a label widget to display the possible processes
process_label = tk.Label(process_frame, text="----------------------------------\nPossible Processes:\n----------------------------------\n1. Extended Euclidean Algorithm\n2. Miller-Rabin Primality Test\n3.Chinese Remainder Theorem\n4.Linear Congruence\n5. Exit\n------------------------------------", font=("Arial", 16, "bold"), bg="white", fg="black", padx=100,pady=10, anchor="e")
process_label.pack(side="left")

# add a label widget to prompt the user for input
input_label = tk.Label(window, text="Choose an option:", font=("Arial", 12))
input_label.pack()

# add a drop-down menu to select an option
option_var = tk.IntVar()
option_var.set(1)
option_menu = tk.OptionMenu(window, option_var, 1, 2, 3, 4, 5)
option_menu.pack()

# add a button to submit the choice
submit_button = tk.Button(window, text="Submit", font=("Arial", 12), command=choose_option)
submit_button.pack()

# start the main event loop
window.mainloop()
