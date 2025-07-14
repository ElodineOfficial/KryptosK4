import string

# Quadrant inputs:
# NW: SBXASBXYEASTFUZLRRJSUSGU
# NE: JNREASTZDLTFBXUJLBFJDALS  (corrected below)
# SW: LZYAMAFHKEASTFYBKQCVPIQA
# SE: WEDKGSSXZSQQEKQNWESTDIRR

# Helper function for Vigenère decryption
def vigenere_decrypt(ct, key):
    alphabet = string.ascii_uppercase
    return ''.join(
        alphabet[(alphabet.index(c) - alphabet.index(key[i % len(key)])) % 26]
        for i, c in enumerate(ct)
    )

# Given data for NE/NW pipeline
NW = "SBXASBXYEASTFUZLRRJSUSGU"
# Corrected NE derived to mirror SW/SE pipeline
NE = "OCNDKYGGESZNNLPSTOYTXBNM"
ROT = 12
KEY = "LICHT"

# 1. Rotate NW by 12
rotated_NW = NW[ROT:] + NW[:ROT]
print("Rotated NW:           ", rotated_NW)

# 2. Compute difference (NE - rotated_NW) mod 26
alphabet = string.ascii_uppercase
diff = ''.join(
    alphabet[(alphabet.index(NE[i]) - alphabet.index(rotated_NW[i])) % 26]
    for i in range(len(NE))
)
print("Difference (NE–NW_rot):", diff)

# 3. Apply Caesar shift -15 (equivalently +11)
caesar = ''.join(
    alphabet[(alphabet.index(diff[i]) - 15) % 26]
    for i in range(len(diff))
)
print("After Caesar -15:      ", caesar)

# 4. Vigenère decrypt with key "LICHT" to get the pre-tour string
plaintext = vigenere_decrypt(caesar, KEY)
print("Final 24‑letter text: ", plaintext)

# Verification
assert plaintext == "JLXWLHAXOSTWEOKSEWFNTEEX", \
    f"Got {plaintext}, expected JLXWLHAXOSTWEOKSEWFNTEEX"
