from ecc import PrivateKey

# Chapter 4 Exercise 5
# Find the address corresponding to Public Keys whose Private Key secrets are:
#   5002        (use uncompressed SEC, on testnet)
#   2020**5     (use compressed SEC, on testnet)
#   0x12345deadbeef (use compressed SEC, on mainnet)

cases = [
    {"secret": 5002, "compressed": False, "testnet": True, "label": "5002, uncompressed, testnet"},
    {"secret": 2020**5, "compressed": True, "testnet": True, "label": "2020**5, compressed, testnet"},
    {"secret": 0x12345deadbeef, "compressed": True, "testnet": False, "label": "0x12345deadbeef, compressed, mainnet"},
]

for c in cases:
    pk = PrivateKey(c["secret"])
    addr = pk.point.address(compressed=c["compressed"], testnet=c["testnet"])
    print(f"case: {c['label']}")
    print(f"secret = {c['secret']}")
    print(f"address = {addr}")
    print()
