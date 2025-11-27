from helper import encode_base58

# Chapter 4 Exercise 4
# Convert the following hex to binary and then to Base58:
#   7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
#   eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
#   c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6

hex_values = [
    "7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d",
    "eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c",
    "c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6",
]

for h in hex_values:
    raw = bytes.fromhex(h)
    b58 = encode_base58(raw)
    print(f"hex     = {h}")
    print(f"base58 = {b58}")
    print()
