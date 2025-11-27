from ecc import PrivateKey

# Chapter 4 Exercise 1
# Find the uncompressed SEC format for the Public Key where the Private Key secrets are:
#   5000
#   2018**5
#   0xdeadbeef12345

secrets = [
    5000,
    2018**5,
    0xdeadbeef12345,
]

for secret in secrets:
    pk = PrivateKey(secret)
    # compressed=False で非圧縮 SEC 形式 (0x04 || x || y)
    sec = pk.point.sec(compressed=False)
    print(f"secret = {secret}")
    print(f"uncompressed SEC = {sec.hex()}")
    print()
