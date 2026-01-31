import tkinter as tk
from tkinter import messagebox
import os


def xor_encrypt(plaintext, key):
    encrypted = ""
    for i in range(len(plaintext)):
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
        encrypted += encrypted_char
    return encrypted


def xor_decrypt(ciphertext, key):
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted_char = chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
        decrypted += decrypted_char
    return decrypted


def encrypt_decrypt():
    choice = choice_var.get()
    text = text_input.get("1.0", tk.END).strip()
    key = key_input.get("1.0", tk.END).strip()

    if not text or not key:
        messagebox.showerror("Error", "Please enter both text and key.")
        return

    if choice == "Encrypt":
        encrypted = xor_encrypt(text, key)
        decrypted = xor_decrypt(encrypted, key)
        result_text.delete("1.0", tk.END)
        # result_text.insert(tk.END, "Encrypted: \n" + encrypted + "\n\nDecrypted: \n" + decrypted)
        result_text.insert(tk.END, encrypted)

    else:
        decrypted = xor_decrypt(text, key)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decrypted)


# Create the main window
root = tk.Tk()
root.title("XOR Encrypt/Decrypt Tool")
root.geometry("600x500")

# Choice selection
choice_var = tk.StringVar(value="Encrypt")
choice_frame = tk.Frame(root)
choice_frame.pack(pady=10)

encrypt_radio = tk.Radiobutton(choice_frame, text="Encrypt", variable=choice_var, value="Encrypt")
encrypt_radio.pack(side=tk.LEFT)

decrypt_radio = tk.Radiobutton(choice_frame, text="Decrypt", variable=choice_var, value="Decrypt")
decrypt_radio.pack(side=tk.LEFT)

# Text input
text_label = tk.Label(root, text="Enter your text:")
text_label.pack(pady=5)
text_input = tk.Text(root, height=5, width=60)
text_input.pack(pady=5)

# Key input
key_label = tk.Label(root, text="Enter key:")
key_label.pack(pady=5)
key_input = tk.Text(root, height=2, width=60)
key_input.pack(pady=5)

# Encrypt/Decrypt button
button = tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt)
button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=5)
result_text = tk.Text(root, height=10, width=60)
result_text.pack(pady=5)

# Run the application
root.mainloop()
