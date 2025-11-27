from __future__ import annotations

from ecc import PrivateKey
from helper import decode_base58
from script import p2pkh_script
from tx import Tx, TxIn, TxOut


def prompt_int(message: str) -> int:
    s = input(message).strip()
    if s.lower().startswith("0x"):
        return int(s, 16)
    return int(s)


def build_tx() -> Tx:
    """Build a 2-input 1-output signet transaction for Chapter 7 Exercise 5.

    Input 1: faucet (signet) UTXO (TODO: fill txid/index/amount)
    Input 2: change UTXO from Exercise 4 (TODO: fill txid/index/amount)

    Both inputs are assumed to be P2PKH to the same private key
    (the one you used in Chapter 4 / Exercise 4).
    """

    print("=== Chapter 7 Exercise 5: build 2-in, 1-out signet transaction ===")

    # --- TODO: ここを自分の UTXO / アドレスに合わせて編集してください ---
    # Input 1: https://mempool.space/signet/tx/f3fd483a090d5bdbc721d9d7fa98e343b132f2fdae9ef5fbae5b0a7b4b3a64e5
    PREV_TX1_HEX = "f3fd483a090d5bdbc721d9d7fa98e343b132f2fdae9ef5fbae5b0a7b4b3a64e5"  # big-endian txid
    PREV_INDEX1 = 0  # vout index
    INPUT_AMOUNT1 = 8700  # satoshi amount of output 1

    # Input 2: https://mempool.space/signet/tx/7b17f489b742ed8e20f37258e772433b02a9d095619a1ec5c68c2bcce4b77992
    PREV_TX2_HEX = "7b17f489b742ed8e20f37258e772433b02a9d095619a1ec5c68c2bcce4b77992"  # big-endian txid from Ex4
    PREV_INDEX2 = 0  # vout index of the chosen output from Ex4
    INPUT_AMOUNT2 = 100000  # satoshi amount of that output

    # 送金先アドレス（1本の出力にまとめる先）
    TARGET_ADDRESS = "mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv"  # P2PKH (m.../n...)

    # 手数料 (satoshi)。入力合計とバイトサイズを見て十分な値に調整すること。
    FEE = 500
    # --- TODO ここまで ---

    prev_tx1 = bytes.fromhex(PREV_TX1_HEX)
    prev_tx2 = bytes.fromhex(PREV_TX2_HEX)
    input_amount1 = INPUT_AMOUNT1
    input_amount2 = INPUT_AMOUNT2

    input_total = input_amount1 + input_amount2
    target_amount = input_total - FEE

    if target_amount <= 0:
        raise ValueError(
            f"Target amount is not positive ({target_amount} sat); adjust FEE or INPUT amounts."
        )

    target_h160 = decode_base58(TARGET_ADDRESS)
    target_script = p2pkh_script(target_h160)

    tx_in1 = TxIn(prev_tx1, PREV_INDEX1)
    tx_in2 = TxIn(prev_tx2, PREV_INDEX2)
    tx_out = TxOut(target_amount, target_script)

    tx_obj = Tx(1, [tx_in1, tx_in2], [tx_out], 0, testnet=True)

    # 秘密鍵（数値）を CLI から受け取る
    secret = prompt_int("Private key secret (integer, DO NOT COMMIT THIS): ")
    private_key = PrivateKey(secret=secret)

    # 2つの入力両方に署名する
    if not tx_obj.sign_input(0, private_key):
        raise RuntimeError("Signing or verification failed for input 0")
    if not tx_obj.sign_input(1, private_key):
        raise RuntimeError("Signing or verification failed for input 1")

    return tx_obj


def main() -> None:
    tx_obj = build_tx()
    raw = tx_obj.serialize().hex()
    print("\n=== Raw transaction (hex) ===")
    print(raw)
    print("\nPaste this hex into a signet pushtx service (e.g. mempool.space signet) to broadcast.")


if __name__ == "__main__":
    main()
