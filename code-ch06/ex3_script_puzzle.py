from script import Script

# Chapter 6 Exercise 3
# Create a ScriptSig that can unlock the following ScriptPubKey:
#   script_pubkey = Script([0x76, 0x76, 0x95, 0x93, 0x56, 0x87])
#
# Opcodes (from the book / notebook):
#   56 = OP_6
#   76 = OP_DUP
#   87 = OP_EQUAL
#   93 = OP_ADD
#   95 = OP_MUL
#
# Goal:
#   Find some initial numbers to put on the stack (ScriptSig) so that
#   the combined script (ScriptSig + ScriptPubKey) evaluates to True.
#
# This file demonstrates one possible solution and prints the stack
# evaluation result. It is meant as a standalone runner similar to
# the Chapter 3 exercise scripts.


def build_scripts() -> tuple[Script, Script]:
    # ScriptPubKey is fixed by the exercise
    script_pubkey = Script([0x76, 0x76, 0x95, 0x93, 0x56, 0x87])

    # ScriptSig must push some initial numbers onto the stack.
    # One valid solution (not shown here to preserve the exercise
    # challenge) is to choose integers a, b such that after the
    # sequence of DUP, MUL, ADD, DUP, EQUAL, the final result is True.
    #
    # Replace the two placeholder zeros below with your chosen values
    # once you have solved the puzzle in the notebook.
    #
    # IMPORTANT:
    #   Script expects data pushes as *bytes*, not small integers.
    #   If we pass ints like 0 or 2 directly, they are treated as
    #   opcodes, which causes KeyError in OP_CODE_FUNCTIONS.
    #   To push the numbers 0 and 2 as data, we use b"\x00" and b"\x02".
    a = 0  # numeric value (not used by the script)
    b = 2  # numeric value satisfying b^2 + b = 6
    script_sig = Script([b"\x00", b"\x02"])

    return script_sig, script_pubkey


def main() -> None:
    script_sig, script_pubkey = build_scripts()
    combined_script = script_sig + script_pubkey
    # z is not used by these arithmetic opcodes, so we can pass 0.
    result = combined_script.evaluate(0)
    print("ScriptSig      :", script_sig)
    print("ScriptPubKey   :", script_pubkey)
    print("Evaluation z   :", 0)
    print("Result (True?):", result)


if __name__ == "__main__":
    main()
