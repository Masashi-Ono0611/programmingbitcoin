from __future__ import annotations

from ecc import PrivateKey
from helper import decode_base58
from script import p2pkh_script
from tx import Tx, TxIn, TxOut


def prompt_int(message: str) -> int:
    value = input(message).strip()
    if value.lower().startswith("0x"):
        return int(value, 16)
    return int(value)


def build_tx() -> Tx:
    """Build a 1-input 2-output testnet transaction for Chapter 7 Exercise 4.

    - 60% of a single UTXO goes to the target address
    - The remaining amount minus fees goes back to your change address

    NOTE:
      - UTXO 情報 (prev_tx, prev_index, input_amount, change_address) は
        あなたの環境に合わせて下の定数を書き換えてください。
      - 秘密鍵だけは CLI から入力します。
    """

    print("=== Chapter 7 Exercise 4: build 1-in, 2-out testnet transaction ===")

    # --- TODO: ここを自分の UTXO / アドレスに合わせて編集してください ---
    # https://mempool.space/signet/tx/d1dd114e6d27fbf963f5a5fb1e435a709b0e6ddacbafcba6adcaed5d6d3e356e
    PREV_TX_HEX = "d1dd114e6d27fbf963f5a5fb1e435a709b0e6ddacbafcba6adcaed5d6d3e356e"
    # そのトランザクションの何番目の出力か
    PREV_INDEX = 0
    # その出力の金額 (satoshi)。例: 0.43 BTC = 43000000 satoshi
    INPUT_AMOUNT = int(0.00010000* 100_000_000)

    # 問題文で指定されている送金先アドレス (60%)
    TARGET_ADDRESS = "mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv"
    # あなたのチェンジアドレス (自分の signet アドレス)
    CHANGE_ADDRESS = "mpa7S8q48je9FKzdv31fmn8dRv2VQF4wu5"

    # 手数料 (satoshi)。トランザクションサイズに対して十分な fee を設定
    # 例: signet ノードの min relay fee (約 226 sat) を超えるよう 300 sat にする。
    FEE = 300
    # --- TODO ここまで ---

    # PREV_TX_HEX is the human-readable txid (big-endian) as shown on explorers.
    # TxIn expects prev_tx in this big-endian form and will reverse it only when
    # serializing to the wire format, so we should NOT reverse it here.
    prev_tx = bytes.fromhex(PREV_TX_HEX)
    prev_index = PREV_INDEX
    input_amount = INPUT_AMOUNT

    # 金額計算 (固定 1000 sat を target, 残り - fee を change)
    target_amount = 1000
    change_amount = input_amount - target_amount - FEE

    if change_amount <= 0:
        raise ValueError(f"Change amount is not positive ({change_amount}satoshi); adjust FEE or INPUT_AMOUNT.")

    # ScriptPubKey for target and change
    target_h160 = decode_base58(TARGET_ADDRESS)
    change_h160 = decode_base58(CHANGE_ADDRESS)
    target_script = p2pkh_script(target_h160)
    change_script = p2pkh_script(change_h160)

    tx_in = TxIn(prev_tx, prev_index)
    tx_out_target = TxOut(target_amount, target_script)
    tx_out_change = TxOut(change_amount, change_script)

    tx_obj = Tx(1, [tx_in], [tx_out_change, tx_out_target], 0, testnet=True)

    # 秘密鍵（数値）を CLI から受け取る
    secret = prompt_int("Private key secret (integer, DO NOT COMMIT THIS): ")
    private_key = PrivateKey(secret=secret)

    # 署名
    if not tx_obj.sign_input(0, private_key):
        raise RuntimeError("Signing or verification failed for input 0")

    return tx_obj


def main() -> None:
    tx_obj = build_tx()
    raw = tx_obj.serialize().hex()
    print("\n=== Raw transaction (hex) ===")
    print(raw)
    print("\nPaste this hex into a testnet pushtx service (e.g. blockstream testnet) to broadcast.")


if __name__ == "__main__":
    main()
