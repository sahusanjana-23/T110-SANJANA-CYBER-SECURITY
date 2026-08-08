print("SANJANA SAHU T110")
# RSA DIGITAL SIGNATURE SYSTEM - CLI
# Integrity and Authenticity Verification

import hashlib
import base64

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
# RSA KEY GENERATION
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()


# GENERATE DIGITAL SIGNATURE


def generate_signature(message):

    message_bytes = message.encode("utf-8")

    # SHA-256 Hash
    message_hash = hashlib.sha256(message_bytes).hexdigest()

    # RSA Private Key se Signature
    signature = private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Signature ko readable format mein convert
    signature_text = base64.b64encode(signature).decode("utf-8")

    return message_hash, signature_text

# VERIFY DIGITAL SIGNATURE

def verify_signature(message, signature_text):

    message_bytes = message.encode("utf-8")

    try:

        # Signature ko bytes mein convert
        signature = base64.b64decode(signature_text)

        # RSA Public Key se verification
        public_key.verify(
            signature,
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Current message ka hash
        current_hash = hashlib.sha256(
            message_bytes
        ).hexdigest()

        return True, current_hash

    except Exception:

        current_hash = hashlib.sha256(
            message_bytes
        ).hexdigest()

        return False, current_hash

# MAIN PROGRAM

print("=" * 60)
print("          RSA DIGITAL SIGNATURE SYSTEM")
print("       Integrity & Authenticity Verification")
print("=" * 60)

# Enter message
message = input("\nEnter your message: ")

# Generate signature
original_hash, signature = generate_signature(message)

print("\n" + "-" * 60)
print("DIGITAL SIGNATURE GENERATED SUCCESSFULLY")
print("-" * 60)

print("\nOriginal Message:")
print(message)

print("\nSHA-256 Hash:")
print(original_hash)

print("\nDigital Signature:")
print(signature)
# VERIFICATION

print("\n" + "=" * 60)
print("             SIGNATURE VERIFICATION")
print("=" * 60)

choice = input(
    "\nDo you want to modify the message before verification? (y/n): "
)

if choice.lower() == "y":

    modified_message = input(
        "\nEnter modified message: "
    )

else:

    modified_message = message


# Verify
valid, current_hash = verify_signature(
    modified_message,
    signature
)


print("\n" + "-" * 60)
print("VERIFICATION RESULT")
print("-" * 60)

print("\nCurrent Message:")
print(modified_message)

print("\nCurrent SHA-256 Hash:")
print(current_hash)


if valid:

    print("\n✓ DIGITAL SIGNATURE: VALID")
    print("✓ AUTHENTICITY: VERIFIED")
    print("✓ INTEGRITY: VERIFIED")

else:

    print("\n✗ DIGITAL SIGNATURE: INVALID")
    print("✗ AUTHENTICITY: NOT VERIFIED")
    print("✗ INTEGRITY: NOT VERIFIED")


print("\n" + "=" * 60)
print("                 END OF PROGRAM")
print("=" * 60)
