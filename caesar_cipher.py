'''# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Negate the shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Ensure the shift wraps around correctly
    shift_amount = shift_amount % len(alphabet)

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter  # Leave non-alphabet characters unchanged

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    if restart != "yes":
        should_continue = False
        print("Goodbye!")'''


import tkinter as tk
from tkinter import messagebox
from art import logo  # If you want to include your logo in a GUI format

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Negate the shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Ensure the shift wraps around correctly
    shift_amount = shift_amount % len(alphabet)

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            # Leave non-alphabet characters unchanged
            output_text += letter

    return output_text

# Create a basic GUI window using Tkinter
def cipher_app():
    # Function to handle button click
    def on_click():
        direction = direction_var.get()
        text = entry_text.get()
        shift = int(entry_shift.get())
        result = caesar(text, shift, direction)
        messagebox.showinfo("Result", f"Here is the {direction}d result: {result}")

    # Setup main window
    root = tk.Tk()
    root.title("Caesar Cipher")
    
    # Create and arrange widgets
    tk.Label(root, text="Enter text:").pack()
    entry_text = tk.Entry(root)
    entry_text.pack()

    tk.Label(root, text="Enter shift amount:").pack()
    entry_shift = tk.Entry(root)
    entry_shift.pack()

    direction_var = tk.StringVar(value="encode")
    tk.Radiobutton(root, text="Encode", variable=direction_var, value="encode").pack()
    tk.Radiobutton(root, text="Decode", variable=direction_var, value="decode").pack()

    tk.Button(root, text="Submit", command=on_click).pack()

    # Run the application
    root.mainloop()

# Run the GUI application
cipher_app()
