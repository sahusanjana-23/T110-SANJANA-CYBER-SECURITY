# ==========================================
# Practical : Message Authentication Code
# Student Name : Sanjana Sahu
# Class/Roll : TYCST110
# ==========================================

import tkinter as tk
from tkinter import messagebox
import hashlib
import hmac


def generate_mac():

    key = key_entry.get()
    message = message_entry.get()

    mac = hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    mac_entry.delete(0, tk.END)
    mac_entry.insert(0, mac)


def verify_mac():

    key = key_entry.get()
    original = message_entry.get()
    received = received_entry.get()

    mac1 = hmac.new(
        key.encode(),
        original.encode(),
        hashlib.sha256
    ).hexdigest()

    mac2 = hmac.new(
        key.encode(),
        received.encode(),
        hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(mac1, mac2):

        messagebox.showinfo(
            "Verification",
            "Message Verified Successfully\n\nStudent : Sanjana Sahu\nTYCST110"
        )

    else:

        messagebox.showerror(
            "Verification",
            "Verification Failed\nMessage Modified"
        )


root = tk.Tk()

root.title("MAC Authentication - Sanjana Sahu")

root.geometry("550x420")

heading = tk.Label(
    root,
    text="MESSAGE AUTHENTICATION CODE\nStudent : Sanjana Sahu (TYCST110)",
    font=("Arial", 14, "bold")
)

heading.pack(pady=10)

tk.Label(root, text="Secret Key").pack()

key_entry = tk.Entry(root, width=40)

key_entry.pack()

tk.Label(root, text="Original Message").pack()

message_entry = tk.Entry(root, width=40)

message_entry.pack()

tk.Button(
    root,
    text="Generate MAC",
    command=generate_mac
).pack(pady=10)

tk.Label(root, text="Generated MAC").pack()

mac_entry = tk.Entry(root, width=65)

mac_entry.pack()

tk.Label(root, text="Received Message").pack()

received_entry = tk.Entry(root, width=40)

received_entry.pack()

tk.Button(
    root,
    text="Verify Message",
    command=verify_mac
).pack(pady=15)

root.mainloop()