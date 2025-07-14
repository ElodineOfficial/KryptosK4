# underink_decrypt.py
# Python script to decrypt the 48‑letter under‑ink Vigenère ciphertext

# Constant ciphertext (48 letters)
CONST_UNDERINK = "ROJMLESLXESLXWSEPUFWIRHTWSUESCCMMCCLRIFXXEWGHEYKIEK"
# Repeating key
KEY = "EAST"


def repeat_key(key: str, length: int) -> str:
    """
    Repeat the key until it matches the desired length.
    """
    return (key * ((length // len(key)) + 1))[:length]


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts the ciphertext using Vigenère cipher (A=0, B=1, ..., Z=25).
    """
    plaintext_chars = []
    key_stream = repeat_key(key, len(ciphertext))
    for c_char, k_char in zip(ciphertext, key_stream):
        # Convert letters to 0-25
        c_val = ord(c_char) - ord('A')
        k_val = ord(k_char) - ord('A')
        # Decrypt: (cipher_val - key_val) mod 26
        p_val = (c_val - k_val) % 26
        plaintext_chars.append(chr(p_val + ord('A')))
    return ''.join(plaintext_chars)


def main():
    decrypted = vigenere_decrypt(CONST_UNDERINK, KEY)
    print("Decrypted under-ink text:", decrypted)
    # Optionally, remove the duplicate 'EAST' from 'NORTHEASTEAST...'
    cleaned = decrypted.replace("EASTEAST", "EAST")
    print("Cleaned directive:        ", cleaned)


if __name__ == "__main__":
    main()
