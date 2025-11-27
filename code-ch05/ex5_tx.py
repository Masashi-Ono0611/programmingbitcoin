from io import BytesIO

from tx import Tx


hex_transaction = (
    "010000000456919960ac691763688d3d3bcea9ad6ecaf875df5339e148a1fc61c6ed7a069e0"
    "10000006a47304402204585bcdef85e6b1c6af5c2669d4830ff86e42dd205c0e089bc2a8216"
    "57e951c002201024a10366077f87d6bce1f7100ad8cfa8a064b39d4e8fe4ea13a7b71aa8180f"
    "012102f0da57e85eec2934a82a585ea337ce2f4998b50ae699dd79f5880e253dafafb7feffff"
    "ffeb8f51f4038dc17e6313cf831d4f02281c2a468bde0fafd37f1bf882729e7fd3000000006a"
    "47304402207899531a52d59a6de200179928ca900254a36b8dff8bb75f5f5d71b1cdc2612502"
    "2008b422690b8461cb52c3cc30330b23d574351872b7c361e9aae3649071c1a7160121035d5c"
    "93d9ac96881f19ba1f686f15f009ded7c62efe85a872e6a19b43c15a2937feffffff567bf405"
    "95119d1bb8a3037c356efd56170b64cbcc160fb028fa10704b45d775000000006a4730440220"
    "4c7c7818424c7f7911da6cddc59655a70af1cb5eaf17c69dadbfc74ffa0b662f02207599e08b"
    "c8023693ad4e9527dc42c34210f7a7d1d1ddfc8492b654a11e7620a0012102158b46fbdff65d"
    "0172b7989aec8850aa0dae49abfb84c81ae6e5b251a58ace5cfeffffffd63a5e6c16e620f86f"
    "375925b21cabaf736c779f88fd04dcad51d26690f7f345010000006a47304402200633ea0d33"
    "14bea0d95b3cd8dadb2ef79ea8331ffe1e61f762c0f6daea0fabde022029f23b3e9c30f08044"
    "6150b23852028751635dcee2be669c2a1686a4b5edf304012103ffd6f4a67e94aba353a00882"
    "e563ff2722eb4cff0ad6006e86ee20dfe7520d55feffffff0251430f00000000001976a914ab"
    "0c0b2e98b1ab6dbf67d4750b0a56244948a87988ac005a6202000000001976a9143c82d7df36"
    "4eb6c75be8c80df2b3eda8db57397088ac46430600"
)


def main() -> None:
    raw = bytes.fromhex(hex_transaction)
    stream = BytesIO(raw)
    tx = Tx.parse(stream)

    second_input_scriptsig = tx.tx_ins[1].script_sig.serialize().hex()
    first_output_scriptpubkey = tx.tx_outs[0].script_pubkey.serialize().hex()
    second_output_amount = tx.tx_outs[1].amount

    print("2nd input ScriptSig (hex):", second_input_scriptsig)
    print("1st output ScriptPubKey (hex):", first_output_scriptpubkey)
    print("2nd output amount (satoshi):", second_output_amount)


if __name__ == "__main__":
    main()
