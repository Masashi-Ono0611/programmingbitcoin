from ecc import PrivateKey

# Chapter 4 Exercise 6
# Find the WIF for Private Key whose secrets are:
#   5003             (compressed, testnet)
#   2021**5          (uncompressed, testnet)
#   0x54321deadbeef  (compressed, mainnet)

cases = [
    {"secret": 5003,            "compressed": True,  "testnet": True,  "label": "5003, compressed, testnet"},
    {"secret": 2021**5,         "compressed": False, "testnet": True,  "label": "2021**5, uncompressed, testnet"},
    {"secret": 0x54321deadbeef, "compressed": True,  "testnet": False, "label": "0x54321deadbeef, compressed, mainnet"},
]

for c in cases:
    pk = PrivateKey(c["secret"])
    wif = pk.wif(compressed=c["compressed"], testnet=c["testnet"])
    print(f"case   : {c['label']}")
    print(f"secret : {c['secret']}")
    print(f"WIF    : {wif}")
    print()
