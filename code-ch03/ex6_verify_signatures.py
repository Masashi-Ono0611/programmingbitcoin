from ecc import S256Point, Signature, G, N

# 公開鍵 P
point = S256Point(
    0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c,
    0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34,
)


def debug_verify(label, z, r, s):
    print(f"\n=== {label} ===")
    print("この署名が有効かどうかを、ECDSA の検証手順で確かめます。")
    print("ゴール: uG + vP の x 座標が r と一致するか? かつ verify(z, (r,s)) が True か?")

    print("\n[1] 入力になっている値")
    print(f"z (メッセージハッシュ)       = {hex(z)}")
    print(f"r (署名のx座標由来の値) = {hex(r)}")
    print(f"s (署名のもう一つの値)   = {hex(s)}")

    # s_inv, u, v を計算
    s_inv = pow(s, N - 2, N)
    print("\n[2] s_inv = s^{-1} (mod N) を計算します。これは 1/s に相当する値です。")
    print(f"s_inv (sの逆元) = {hex(s_inv)}")

    u = z * s_inv % N
    v = r * s_inv % N
    print("\n[3] u, v を計算します。これは公開値だけから作る係数です。")
    print("    u = z * s^{-1} (mod N), v = r * s^{-1} (mod N)")
    print(f"u (G に掛ける係数) = {hex(u)}")
    print(f"v (公開鍵 P に掛ける係数) = {hex(v)}")

    # uG, vP, R=uG+vP を計算
    uG = u * G
    vP = v * point
    R = uG + vP

    print("\n[4] 楕円曲線上で点を計算します。")
    print("    uG = u * G (生成点Gをu倍した点)")
    print("    vP = v * P (公開鍵Pをv倍した点)")
    print("    R  = uG + vP")
    print(f"u*G = ({hex(uG.x.num)}, {hex(uG.y.num)})")
    print(f"v*P = ({hex(vP.x.num)}, {hex(vP.y.num)})")

    if R.x is None:
        print("R = u*G + v*P = infinity (無限遠点)")
    else:
        print(f"R = u*G + v*P = ({hex(R.x.num)}, {hex(R.y.num)})")
        print("[5] R の x 座標が署名の r と一致しているかを確認します。")
        print(f"R.x == r ? {R.x.num == r}")

    sig = Signature(r, s)
    print("\n[6] point.verify(z, sig) でも同じ条件を内部でチェックしています。")
    print(f"verify() result: {point.verify(z, sig)}")


# Signature 1
z1 = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
r1 = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
s1 = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4

debug_verify("Signature 1", z1, r1, s1)

# Signature 2
z2 = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
r2 = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
s2 = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6

debug_verify("Signature 2", z2, r2, s2)
