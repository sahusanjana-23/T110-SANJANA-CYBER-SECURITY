# ==========================================
# Practical : Message Authentication Code
# Student Name : Sanjana Sahu
# Class/Roll : TYCST110
# ==========================================

import hmac
import hashlib

print("=" * 50)
print(" MESSAGE AUTHENTICATION CODE (MAC)")
print(" Student : Sanjana Sahu")
print(" Roll No : TYCST110")
print("=" * 50)

secret_key = input("\nEnter Secret Key : ")

message = input("Enter Original Message : ")

generated_mac = hmac.new(
    secret_key.encode(),
    message.encode(),
    hashlib.sha256
).hexdigest()

print("\nGenerated MAC")
print(generated_mac)

print("\n------------- Verification -------------")

received_message = input("Enter Received Message : ")

received_mac = hmac.new(
    secret_key.encode(),
    received_message.encode(),
    hashlib.sha256
).hexdigest()

if hmac.compare_digest(generated_mac, received_mac):

    print("\nMessage Verified Successfully")
    print("Integrity Maintained")
    print("Sender is Authentic")

else:

    print("\nVerification Failed")
    print("Message Modified")