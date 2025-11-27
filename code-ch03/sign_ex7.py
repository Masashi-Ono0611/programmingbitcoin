from ecc import S256Point, G, N
from helper import hash256

# secret (private key)
e = 12345

print("[1] 秘密鍵 e を決めます。これは署名者だけが知っている値です。")
print(f"e (secret) = {e}")

# message hash
z = int.from_bytes(hash256(b'Programming Bitcoin!'), 'big')
print("\n[2] メッセージ 'Programming Bitcoin!' を hash256 し、整数に変換したものを z とします。")
print(f"z (message hash) = {hex(z)}")

# choose a random k (nonce)
# NOTE: for real-world use, k must be random and never reused
k = 1234567890
print("\n[3] 署名ごとに一度だけ使う一時秘密 k を選びます (本番では高品質な乱数が必要)。")
print(f"k (nonce) = {k}")

# compute r = (kG).x
kG = k * G
r = kG.x.num
print("\n[4] 点 kG を計算し、その x 座標を r とします。")
print(f"kG = ({hex(kG.x.num)}, {hex(kG.y.num)})")
print(f"r = (kG).x = {hex(r)}")

# compute k inverse modulo N
k_inv = pow(k, N - 2, N)
print("\n[5] k の逆元 k_inv = k^{-1} (mod N) を計算します。これは 1/k に相当します。")
print(f"k_inv = {hex(k_inv)}")

# compute s = (z + r*e) / k (mod N)
s = (z + r * e) * k_inv % N
print("\n[6] s = (z + r*e) / k (mod N) を計算します。ここに秘密鍵 e が用いられ、署名の一部としてカバーされます。")
print(f"s = {hex(s)}")

# corresponding public key point
point = e * G
print("\n[7] 公開鍵 P = eG を計算します。これは他人に知られてよい値です。")
print(f"Public key P = {point}")

print("\n[8] これで署名 (r, s) が完成しました。検証側は (P, z, r, s) を使って verify できます。")
print(f"最終的な値: z = {hex(z)}")
print(f"最終的な値: r = {hex(r)}")
print(f"最終的な値: s = {hex(s)}")
