from __future__ import annotations

from ecc import PrivateKey
from helper import hash256, little_endian_to_int


def main() -> None:
    print("=== Generate P2PKH testnet wallet (for Chapter 7 Ex4) ===")
    print("このスクリプトは、パスフレーズからテストネット用の P2PKH アドレスを生成します。\n")

    phrase = input("任意のパスフレーズ（英数字など／絶対に他所で使い回さない）: ").encode("utf-8")

    # パスフレーズから疑似乱数的に秘密鍵を導出
    # ※学習用。実運用ではもっと安全なウォレットを使うこと。
    secret = little_endian_to_int(hash256(phrase))
    private_key = PrivateKey(secret)

    # testnet 用 P2PKH アドレスを生成
    address = private_key.point.address(testnet=True)

    print("\n[Wallet Information]")
    print(f"secret (integer)        : {secret}")
    print(f"secret (hex)            : {hex(secret)}")
    print(f"testnet P2PKH address   : {address}")
    print("\n※ この secret は `ex4_build_tx.py` の入力に使えます。")
    print("※ この情報は絶対に Git にコミットしたり、他人と共有しないでください。")


if __name__ == "__main__":
    main()
