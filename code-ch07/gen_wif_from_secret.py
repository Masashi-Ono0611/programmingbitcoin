from __future__ import annotations

from helper import encode_base58_checksum


def prompt_int(message: str) -> int:
    s = input(message).strip()
    if s.lower().startswith("0x"):
        return int(s, 16)
    return int(s)


def secret_to_wif(secret: int, testnet: bool = True, compressed: bool = True) -> str:
    """Convert a raw secret integer to WIF.

    - For testnet/signet P2PKH, prefix is 0xEF.
    - For mainnet P2PKH, prefix would be 0x80 (ここでは使わない)。
    - Compressed keyの場合は末尾に 0x01 を付ける。
    """
    if not (1 <= secret < 2 ** 256):
        raise ValueError("secret must be in range [1, 2^256-1]")

    # 32-byte big-endian representation of the secret
    secret_bytes = secret.to_bytes(32, "big")

    if testnet:
        prefix = b"\xef"  # testnet/signet prefix
    else:
        prefix = b"\x80"  # mainnet prefix (not used in this chapter)

    if compressed:
        payload = prefix + secret_bytes + b"\x01"
    else:
        payload = prefix + secret_bytes

    return encode_base58_checksum(payload)


def main() -> None:
    print("=== Convert secret integer to testnet/signet WIF ===")
    print("このスクリプトは、gen_p2pkh_wallet.py などで得た secret (整数) を、")
    print("testnet/signet 用の WIF 形式に変換します。\n")

    secret = prompt_int("secret (integer or 0x...): ")
    wif = secret_to_wif(secret, testnet=True, compressed=True)

    print("\n[WIF Information]")
    print(f"secret (integer) : {secret}")
    print(f"secret (hex)     : {hex(secret)}")
    print(f"WIF (testnet)    : {wif}")
    print("\n※ この WIF を、Sparrow Wallet や Bitcoin Core (signet/testnet) などにインポートできます。")
    print("※ 本番用の mainnet 資産には絶対に使わないでください。学習用の鍵に限定してください。")


if __name__ == "__main__":
    main()
