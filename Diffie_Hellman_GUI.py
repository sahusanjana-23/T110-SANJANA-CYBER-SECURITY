# ============================================================
# DIFFIE-HELLMAN KEY EXCHANGE - FULL SCREEN GUI
# ============================================================

import tkinter as tk
from tkinter import messagebox


# ============================================================
# FUNCTIONS
# ============================================================

def generate_public_keys():
    try:
        p = int(p_entry.get())
        g = int(g_entry.get())

        sanjana_private = int(sanjana_private_entry.get())
        priya_private = int(priya_private_entry.get())

        if p <= 1:
            messagebox.showerror("Error", "p must be greater than 1.")
            return

        if g <= 0:
            messagebox.showerror("Error", "g must be greater than 0.")
            return

        if sanjana_private <= 0 or priya_private <= 0:
            messagebox.showerror(
                "Error",
                "Private keys must be positive numbers."
            )
            return

        # ----------------------------------------------------
        # PUBLIC KEYS
        # ----------------------------------------------------

        sanjana_public = pow(g, sanjana_private, p)
        priya_public = pow(g, priya_private, p)

        # Display Sanjana Public Key
        sanjana_public_entry.config(state="normal")
        sanjana_public_entry.delete(0, tk.END)
        sanjana_public_entry.insert(0, str(sanjana_public))
        sanjana_public_entry.config(state="readonly")

        # Display Priya Public Key
        priya_public_entry.config(state="normal")
        priya_public_entry.delete(0, tk.END)
        priya_public_entry.insert(0, str(priya_public))
        priya_public_entry.config(state="readonly")

        # Clear output
        output_text.delete("1.0", tk.END)

        # ----------------------------------------------------
        # STEP 1
        # ----------------------------------------------------

        output_text.insert(
            tk.END,
            "STEP 1: PUBLIC PARAMETERS\n\n"
        )

        output_text.insert(
            tk.END,
            f"p = {p}\n"
            f"g = {g}\n\n\n"
        )

        # ----------------------------------------------------
        # STEP 2
        # ----------------------------------------------------

        output_text.insert(
            tk.END,
            "STEP 2: PRIVATE KEYS\n\n"
        )

        output_text.insert(
            tk.END,
            f"Sanjana's Private Key = {sanjana_private}\n"
            f"Priya's Private Key   = {priya_private}\n\n\n"
        )

        # ----------------------------------------------------
        # STEP 3
        # ----------------------------------------------------

        output_text.insert(
            tk.END,
            "STEP 3: SANJANA GENERATES PUBLIC KEY\n\n"
        )

        output_text.insert(
            tk.END,
            "Formula:\n"
            "Sanjana Public Key = g^a mod p\n\n"
        )

        output_text.insert(
            tk.END,
            "Calculation:\n"
            f"Sanjana Public Key = "
            f"{g} ^ {sanjana_private} mod {p}\n\n"
        )

        output_text.insert(
            tk.END,
            f"Sanjana Public Key = "
            f"{sanjana_public}\n\n\n"
        )

        # ----------------------------------------------------
        # STEP 4
        # ----------------------------------------------------

        output_text.insert(
            tk.END,
            "STEP 4: PRIYA GENERATES PUBLIC KEY\n\n"
        )

        output_text.insert(
            tk.END,
            "Formula:\n"
            "Priya Public Key = g^b mod p\n\n"
        )

        output_text.insert(
            tk.END,
            "Calculation:\n"
            f"Priya Public Key = "
            f"{g} ^ {priya_private} mod {p}\n\n"
        )

        output_text.insert(
            tk.END,
            f"Priya Public Key = "
            f"{priya_public}\n\n\n"
        )

        # ----------------------------------------------------
        # STEP 5
        # ----------------------------------------------------

        output_text.insert(
            tk.END,
            "STEP 5: PUBLIC KEY EXCHANGE\n\n"
        )

        output_text.insert(
            tk.END,
            f"Sanjana -> Priya : {sanjana_public}\n"
            f"Priya -> Sanjana : {priya_public}\n\n"
            "Private keys are NOT exchanged.\n"
        )

        messagebox.showinfo(
            "Success",
            "Public Keys Generated Successfully!"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )


# ============================================================
# GENERATE SHARED KEY
# ============================================================

def generate_shared_key():

    try:

        p = int(p_entry.get())

        sanjana_private = int(
            sanjana_private_entry.get()
        )

        priya_private = int(
            priya_private_entry.get()
        )

        sanjana_public = int(
            sanjana_public_entry.get()
        )

        priya_public = int(
            priya_public_entry.get()
        )

        # ----------------------------------------------------
        # SHARED SECRET KEYS
        # ----------------------------------------------------

        sanjana_shared = pow(
            priya_public,
            sanjana_private,
            p
        )

        priya_shared = pow(
            sanjana_public,
            priya_private,
            p
        )

        # ----------------------------------------------------
        # DISPLAY SHARED KEYS
        # ----------------------------------------------------

        sanjana_shared_entry.config(
            state="normal"
        )

        sanjana_shared_entry.delete(
            0,
            tk.END
        )

        sanjana_shared_entry.insert(
            0,
            str(sanjana_shared)
        )

        sanjana_shared_entry.config(
            state="readonly"
        )

        priya_shared_entry.config(
            state="normal"
        )

        priya_shared_entry.delete(
            0,
            tk.END
        )

        priya_shared_entry.insert(
            0,
            str(priya_shared)
        )

        priya_shared_entry.config(
            state="readonly"
        )

        # ----------------------------------------------------
        # STEP 6
        # ----------------------------------------------------

        output_text.insert(
            tk.END,
            "\n\n"
            "STEP 6: SANJANA CALCULATES SHARED SECRET\n\n"
        )

        output_text.insert(
            tk.END,
            "Sanjana Shared Secret = "
            f"{priya_public} ^ "
            f"{sanjana_private} mod {p}\n\n"
        )

        output_text.insert(
            tk.END,
            f"Sanjana Shared Secret = "
            f"{sanjana_shared}\n\n\n"
        )

        # ----------------------------------------------------
        # STEP 7
        # ----------------------------------------------------

        output_text.insert(
            tk.END,
            "STEP 7: PRIYA CALCULATES SHARED SECRET\n\n"
        )

        output_text.insert(
            tk.END,
            "Priya Shared Secret = "
            f"{sanjana_public} ^ "
            f"{priya_private} mod {p}\n\n"
        )

        output_text.insert(
            tk.END,
            f"Priya Shared Secret = "
            f"{priya_shared}\n\n\n"
        )

        messagebox.showinfo(
            "Success",
            "Shared Secret Keys Generated!"
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "First generate the Public Keys."
        )


# ============================================================
# VERIFY KEY
# ============================================================

def verify_key():

    try:

        sanjana_shared = int(
            sanjana_shared_entry.get()
        )

        priya_shared = int(
            priya_shared_entry.get()
        )

        # ----------------------------------------------------
        # STEP 8
        # ----------------------------------------------------

        output_text.insert(
            tk.END,
            "STEP 8: VERIFICATION\n\n"
        )

        output_text.insert(
            tk.END,
            f"Sanjana Shared Secret = "
            f"{sanjana_shared}\n"
        )

        output_text.insert(
            tk.END,
            f"Priya Shared Secret   = "
            f"{priya_shared}\n\n"
        )

        # ----------------------------------------------------
        # VERIFICATION
        # ----------------------------------------------------

        if sanjana_shared == priya_shared:

            output_text.insert(
                tk.END,
                "SUCCESS!\n"
            )

            output_text.insert(
                tk.END,
                "Both Sanjana and Priya have "
                "the SAME secret key.\n"
            )

            output_text.insert(
                tk.END,
                f"Shared Secret Key = "
                f"{sanjana_shared}\n"
            )

            messagebox.showinfo(
                "Verification Successful",
                "Both keys are SAME!\n\n"
                f"Shared Secret Key = "
                f"{sanjana_shared}"
            )

        else:

            output_text.insert(
                tk.END,
                "Key Exchange Failed!\n"
            )

            messagebox.showerror(
                "Verification Failed",
                "Shared keys are different."
            )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please generate the Shared Keys first."
        )


# ============================================================
# CLEAR ALL
# ============================================================

def clear_all():

    for entry in [
        p_entry,
        g_entry,
        sanjana_private_entry,
        priya_private_entry
    ]:

        entry.delete(
            0,
            tk.END
        )

    for entry in [
        sanjana_public_entry,
        priya_public_entry,
        sanjana_shared_entry,
        priya_shared_entry
    ]:

        entry.config(
            state="normal"
        )

        entry.delete(
            0,
            tk.END
        )

        entry.config(
            state="readonly"
        )

    output_text.delete(
        "1.0",
        tk.END
    )


# ============================================================
# EXIT FULL SCREEN
# ============================================================

def exit_fullscreen():

    root.attributes(
        "-fullscreen",
        False
    )


# ============================================================
# FULL SCREEN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "Diffie-Hellman Key Exchange"
)

# FULL SCREEN
root.attributes(
    "-fullscreen",
    True
)

root.configure(
    bg="#EAF2F8"
)


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Arial", 28, "bold"),
    bg="#1F618D",
    fg="white",
    pady=18
)

title.pack(
    fill="x"
)


# ============================================================
# MAIN FRAME
# ============================================================

main_frame = tk.Frame(
    root,
    bg="#EAF2F8"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=15
)


# ============================================================
# INPUT FRAME
# ============================================================

input_frame = tk.Frame(
    main_frame,
    bg="#EAF2F8"
)

input_frame.pack(
    pady=5
)


# ------------------------------------------------------------
# PUBLIC PARAMETERS
# ------------------------------------------------------------

tk.Label(
    input_frame,
    text="PUBLIC PARAMETERS",
    font=("Arial", 16, "bold"),
    bg="#EAF2F8"
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=8
)


tk.Label(
    input_frame,
    text="Prime Number (p):",
    font=("Arial", 12),
    bg="#EAF2F8"
).grid(
    row=1,
    column=0,
    padx=15,
    pady=5,
    sticky="e"
)


p_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=22
)

p_entry.grid(
    row=1,
    column=1,
    pady=5
)


tk.Label(
    input_frame,
    text="Generator (g):",
    font=("Arial", 12),
    bg="#EAF2F8"
).grid(
    row=2,
    column=0,
    padx=15,
    pady=5,
    sticky="e"
)


g_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=22
)

g_entry.grid(
    row=2,
    column=1,
    pady=5
)


# ------------------------------------------------------------
# PRIVATE KEYS
# ------------------------------------------------------------

tk.Label(
    input_frame,
    text="PRIVATE KEYS",
    font=("Arial", 16, "bold"),
    bg="#EAF2F8"
).grid(
    row=3,
    column=0,
    columnspan=2,
    pady=(12, 8)
)


tk.Label(
    input_frame,
    text="Sanjana Private Key:",
    font=("Arial", 12),
    bg="#EAF2F8"
).grid(
    row=4,
    column=0,
    padx=15,
    pady=5,
    sticky="e"
)


sanjana_private_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=22
)

sanjana_private_entry.grid(
    row=4,
    column=1,
    pady=5
)


tk.Label(
    input_frame,
    text="Priya Private Key:",
    font=("Arial", 12),
    bg="#EAF2F8"
).grid(
    row=5,
    column=0,
    padx=15,
    pady=5,
    sticky="e"
)


priya_private_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=22
)

priya_private_entry.grid(
    row=5,
    column=1,
    pady=5
)


# ============================================================
# PUBLIC KEY FRAME
# ============================================================

key_frame = tk.Frame(
    main_frame,
    bg="#EAF2F8"
)

key_frame.pack(
    pady=8
)


tk.Label(
    key_frame,
    text="Sanjana Public Key:",
    font=("Arial", 12, "bold"),
    bg="#EAF2F8"
).grid(
    row=0,
    column=0,
    padx=10
)


sanjana_public_entry = tk.Entry(
    key_frame,
    font=("Arial", 12),
    width=18,
    state="readonly"
)

sanjana_public_entry.grid(
    row=0,
    column=1,
    padx=10
)


tk.Label(
    key_frame,
    text="Priya Public Key:",
    font=("Arial", 12, "bold"),
    bg="#EAF2F8"
).grid(
    row=0,
    column=2,
    padx=10
)


priya_public_entry = tk.Entry(
    key_frame,
    font=("Arial", 12),
    width=18,
    state="readonly"
)

priya_public_entry.grid(
    row=0,
    column=3,
    padx=10
)


# ============================================================
# SHARED KEY FRAME
# ============================================================

shared_frame = tk.Frame(
    main_frame,
    bg="#EAF2F8"
)

shared_frame.pack(
    pady=8
)


tk.Label(
    shared_frame,
    text="Sanjana Shared Key:",
    font=("Arial", 12, "bold"),
    bg="#EAF2F8"
).grid(
    row=0,
    column=0,
    padx=10
)


sanjana_shared_entry = tk.Entry(
    shared_frame,
    font=("Arial", 12),
    width=18,
    state="readonly"
)

sanjana_shared_entry.grid(
    row=0,
    column=1,
    padx=10
)


tk.Label(
    shared_frame,
    text="Priya Shared Key:",
    font=("Arial", 12, "bold"),
    bg="#EAF2F8"
).grid(
    row=0,
    column=2,
    padx=10
)


priya_shared_entry = tk.Entry(
    shared_frame,
    font=("Arial", 12),
    width=18,
    state="readonly"
)

priya_shared_entry.grid(
    row=0,
    column=3,
    padx=10
)


# ============================================================
# BUTTON FRAME
# ============================================================

button_frame = tk.Frame(
    main_frame,
    bg="#EAF2F8"
)

button_frame.pack(
    pady=10
)


tk.Button(
    button_frame,
    text="Generate Public Keys",
    font=("Arial", 11, "bold"),
    width=20,
    command=generate_public_keys
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    button_frame,
    text="Generate Shared Key",
    font=("Arial", 11, "bold"),
    width=20,
    command=generate_shared_key
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    button_frame,
    text="Verify Key",
    font=("Arial", 11, "bold"),
    width=15,
    command=verify_key
).grid(
    row=0,
    column=2,
    padx=5
)


tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    width=12,
    command=clear_all
).grid(
    row=0,
    column=3,
    padx=5
)


tk.Button(
    button_frame,
    text="Exit Full Screen",
    font=("Arial", 11, "bold"),
    width=15,
    command=exit_fullscreen
).grid(
    row=0,
    column=4,
    padx=5
)


# ============================================================
# OUTPUT LABEL
# ============================================================

tk.Label(
    main_frame,
    text="STEP-BY-STEP OUTPUT",
    font=("Arial", 16, "bold"),
    bg="#EAF2F8"
).pack(
    pady=(5, 5)
)


# ============================================================
# OUTPUT FRAME
# ============================================================

output_frame = tk.Frame(
    main_frame,
    bg="#EAF2F8"
)

output_frame.pack(
    fill="both",
    expand=True,
    padx=20
)


# ============================================================
# OUTPUT TEXT
# ============================================================

output_text = tk.Text(
    output_frame,
    font=("Consolas", 12),
    wrap="word",
    bg="white",
    fg="black"
)

output_text.pack(
    side="left",
    fill="both",
    expand=True
)


# ============================================================
# SCROLLBAR
# ============================================================

scrollbar = tk.Scrollbar(
    output_frame,
    command=output_text.yview
)

scrollbar.pack(
    side="right",
    fill="y"
)

output_text.config(
    yscrollcommand=scrollbar.set
)


# ============================================================
# START PROGRAM
# ============================================================

root.mainloop()
