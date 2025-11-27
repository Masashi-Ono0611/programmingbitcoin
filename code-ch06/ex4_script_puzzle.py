from script import Script

# Chapter 6 Exercise 4
# Figure out what this Script is doing:
#   6e879169a77ca787
#
# Opcodes:
#   6e = OP_2DUP   (duplicate the top two stack items)
#   87 = OP_EQUAL  (compare top two items for equality)
#   91 = OP_NOT    (logical NOT: 0 -> 1, non-zero -> 0)
#   69 = OP_VERIFY (fail if top of stack is 0)
#   a7 = OP_SHA1   (replace top element by its SHA1 hash)
#   7c = OP_SWAP   (swap top two stack items)
#
# ScriptPubKey used in the notebook:
#   Script([0x6e, 0x87, 0x91, 0x69, 0xa7, 0x7c, 0xa7, 0x87])
#
# Intuition:
#   If ScriptSig pushes two values x, y, then this Script:
#     - First enforces x != y
#     - Then checks whether SHA1(x) == SHA1(y)
#   つまり、「中身は違うのに SHA1 ハッシュが同じ 2 つの値」を要求する、
#   事実上ほぼ不可能なロック条件になっています。


def build_scripts() -> tuple[Script, Script]:
    # ScriptPubKey is fixed by the exercise
    script_pubkey = Script([0x6e, 0x87, 0x91, 0x69, 0xa7, 0x7c, 0xa7, 0x87])

    # ScriptSig: push two different data values x, y onto the stack.
    # ここでは単に例として b"foo" と b"bar" を使います。
    # x != y なので、前半の条件 (x != y) は満たしますが、
    # SHA1(x) == SHA1(y) にはならないので、最終結果は False になります。
    x = b"foo"
    y = b"bar"
    script_sig = Script([x, y])

    return script_sig, script_pubkey


def main() -> None:
    script_sig, script_pubkey = build_scripts()
    combined_script = script_sig + script_pubkey
    # z はこの Script では使われないので 0 でよい
    result = combined_script.evaluate(0)
    print("ScriptSig      :", script_sig)
    print("ScriptPubKey   :", script_pubkey)
    print("Evaluation z   :", 0)
    print("Result (True?):", result)


if __name__ == "__main__":
    main()
