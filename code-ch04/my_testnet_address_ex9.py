from ecc import PrivateKey
from helper import hash256, little_endian_to_int


def main() -> None:
    # パスフレーズを CLI から入力（平文入力 / 実運用なら getpass などを検討）
    phrase_str = input("Enter your secret passphrase (will be hashed): ")
    passphrase = phrase_str.encode("utf-8")

    # パスフレーズ → ハッシュ → little-endian 整数
    secret = little_endian_to_int(hash256(passphrase))

    # 秘密鍵と testnet アドレス生成（圧縮 SEC を使用）
    pk = PrivateKey(secret)
    address = pk.point.address(compressed=True, testnet=True)

    print("=== Your Testnet Address (Ex9) ===")
    print(f"secret (int)       : {secret}")
    print(f"testnet address    : {address}")


if __name__ == "__main__":
    main()
