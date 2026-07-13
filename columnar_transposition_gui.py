import tkinter as tk
from tkinter import messagebox


def encrypt(message, key):
    col = len(key)
    row = (len(message) + col - 1) // col

    message += 'X' * (row * col - len(message))

    matrix = []
    index = 0

    for i in range(row):
        matrix.append(list(message[index:index + col]))
        index += col

    order = sorted(list(enumerate(key)), key=lambda x: x[1])

    cipher = ""

    for pos, ch in order:
        for r in range(row):
            cipher += matrix[r][pos]

    return cipher


def decrypt(cipher, key):
    col = len(key)
    row = len(cipher) // col

    order = sorted(list(enumerate(key)), key=lambda x: x[1])

    matrix = [['' for _ in range(col)] for _ in range(row)]

    index = 0

    for pos, ch in order:
        for r in range(row):
            matrix[r][pos] = cipher[index]
            index += 1

    plain = ""

    for r in range(row):
        for c in range(col):
            plain += matrix[r][c]

    return plain.rstrip('X')


def do_encrypt():
    msg = msg_entry.get().upper()
    key = key_entry.get().upper()

    if msg == "" or key == "":
        messagebox.showerror("Error", "Please enter Message and Key")
        return

    result.config(text="Encrypted : " + encrypt(msg, key),
                  fg="green")


def do_decrypt():
    msg = msg_entry.get().upper()
    key = key_entry.get().upper()

    if msg == "" or key == "":
        messagebox.showerror("Error", "Please enter Message and Key")
        return

    result.config(text="Decrypted : " + decrypt(msg, key),
                  fg="blue")


def clear():
    msg_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    result.config(text="")


root = tk.Tk()
root.title("Columnar Transposition Cipher")
root.geometry("620x420")
root.configure(bg="#EAF8FF")

header = tk.Label(root,
                  text="🔐 Columnar Transposition Cipher",
                  bg="#6A1B9A",
                  fg="white",
                  font=("Arial",20,"bold"),
                  pady=10)
header.pack(fill="x")

tk.Label(root,
         text="Enter Message",
         bg="#EAF8FF",
         font=("Arial",12,"bold")).pack(pady=10)

msg_entry = tk.Entry(root,
                     width=40,
                     font=("Arial",14))
msg_entry.pack()

tk.Label(root,
         text="Enter Key",
         bg="#EAF8FF",
         font=("Arial",12,"bold")).pack(pady=10)

key_entry = tk.Entry(root,
                     width=20,
                     font=("Arial",14))
key_entry.pack()

frame = tk.Frame(root,bg="#EAF8FF")
frame.pack(pady=20)

tk.Button(frame,
          text="Encrypt",
          bg="green",
          fg="white",
          font=("Arial",12,"bold"),
          width=12,
          command=do_encrypt).grid(row=0,column=0,padx=10)

tk.Button(frame,
          text="Decrypt",
          bg="blue",
          fg="white",
          font=("Arial",12,"bold"),
          width=12,
          command=do_decrypt).grid(row=0,column=1,padx=10)

tk.Button(frame,
          text="Clear",
          bg="orange",
          fg="white",
          font=("Arial",12,"bold"),
          width=12,
          command=clear).grid(row=0,column=2,padx=10)

result = tk.Label(root,
                  text="",
                  bg="#EAF8FF",
                  font=("Arial",15,"bold"))
result.pack(pady=20)

tk.Button(root,
          text="Exit",
          bg="red",
          fg="white",
          font=("Arial",12,"bold"),
          width=18,
          command=root.destroy).pack()

footer = tk.Label(root,
                  text="Transposition Technique | Columnar Cipher",
                  bg="#263238",
                  fg="white")
footer.pack(side="bottom",fill="x")

root.mainloop()