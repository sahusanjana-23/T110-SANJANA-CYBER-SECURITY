# ============================================================
# DIFFIE-HELLMAN KEY EXCHANGE
# STEP-BY-STEP COMMAND LINE PROGRAM
# ============================================================

print("=" * 60)
print("        DIFFIE-HELLMAN KEY EXCHANGE")
print("=" * 60)

# STEP 1: Public Parameters
print("\nSTEP 1: PUBLIC PARAMETERS")

p = int(input("Enter prime number (p): "))
g = int(input("Enter generator (g): "))

print("\np =", p)
print("g =", g)

# STEP 2: Private Keys
print("\n\nSTEP 2: PRIVATE KEYS")

sanjana_private = int(input("Enter Sanjana's private key: "))
priya_private = int(input("Enter Priya's private key: "))

print("\nSanjana's Private Key =", sanjana_private)
print("Priya's Private Key   =", priya_private)

# STEP 3: Sanjana Public Key
print("\n\nSTEP 3: SANJANA GENERATES PUBLIC KEY")

sanjana_public = pow(g, sanjana_private, p)

print("\nFormula:")
print("Sanjana Public Key = g^a mod p")

print("\nCalculation:")
print("Sanjana Public Key =", g, "^", sanjana_private, "mod", p)

print("\nSanjana Public Key =", sanjana_public)

# STEP 4: Priya Public Key
print("\n\nSTEP 4: PRIYA GENERATES PUBLIC KEY")

priya_public = pow(g, priya_private, p)

print("\nFormula:")
print("Priya Public Key = g^b mod p")

print("\nCalculation:")
print("Priya Public Key =", g, "^", priya_private, "mod", p)

print("\nPriya Public Key =", priya_public)

# STEP 5: Public Key Exchange
print("\n\nSTEP 5: PUBLIC KEY EXCHANGE")

print("\nSanjana -> Priya :", sanjana_public)
print("Priya -> Sanjana :", priya_public)

print("\nPrivate keys are NOT exchanged.")

# STEP 6: Sanjana Shared Secret
print("\n\nSTEP 6: SANJANA CALCULATES SHARED SECRET")

sanjana_shared = pow(priya_public, sanjana_private, p)

print("\nSanjana Shared Secret =", priya_public, "^", sanjana_private, "mod", p)

print("\nSanjana Shared Secret =", sanjana_shared)

# STEP 7: Priya Shared Secret
print("\n\nSTEP 7: PRIYA CALCULATES SHARED SECRET")

priya_shared = pow(sanjana_public, priya_private, p)

print("\nPriya Shared Secret =", sanjana_public, "^", priya_private, "mod", p)

print("\nPriya Shared Secret =", priya_shared)

# STEP 8: Verification
print("\n\nSTEP 8: VERIFICATION")

print("\nSanjana Shared Secret =", sanjana_shared)
print("Priya Shared Secret   =", priya_shared)

if sanjana_shared == priya_shared:
    print("\nSUCCESS!")
    print("Both Sanjana and Priya have the SAME secret key.")
    print("Shared Secret Key =", sanjana_shared)
else:
    print("\nKey Exchange Failed!")

print("\n" + "=" * 60)
print("             PROGRAM COMPLETED")
print("=" * 60)
