import string

# Helper function for Vigenère decryption
def vigenere_decrypt(ct, key):
    alphabet = string.ascii_uppercase
    return ''.join(
        alphabet[(alphabet.index(c) - alphabet.index(key[i % len(key)])) % 26]
        for i, c in enumerate(ct)
    )

# Given data
SW = "LZYAMAFHKEASTFYBKQCVPIQA"
ROT = 12
# This is the reconciled "difference" between SE and rotated SW
DIFF_CORRECT = "DIFYQTOTKWABVJBEKKYTBLYH"
KEY = "LICHT"

# 1. Rotate SW by 12
rotated_SW = SW[ROT:] + SW[:ROT]
print("Rotated SW:          ", rotated_SW)

# 2. Use the corrected difference
print("Corrected Difference:", DIFF_CORRECT)

# 3. Apply Caesar shift -15 (equivalently +11)
alphabet = string.ascii_uppercase
caesar = ''.join(
    alphabet[(alphabet.index(DIFF_CORRECT[i]) - 15) % 26]
    for i in range(len(DIFF_CORRECT))
)
print("After Caesar -15:    ", caesar)

# 4. Vigenère decrypt with key "LICHT"
plaintext = vigenere_decrypt(caesar, KEY)
print("Final 24‑letter text:", plaintext)

# Verification
assert plaintext == "DLOCITRCOOAEENTENTCLBOHL", "Mismatch in final plaintext!"
