import string

def remove_center_w(text: str) -> str:
    # Remove the 49th character (index 48)
    return text[:48] + text[49:]

def chunk_quadrants(text: str) -> dict:
    # Split into four 24-character blocks
    names = ["NW", "NE", "SW", "SE"]
    return {name: text[i*24:(i+1)*24] for i, name in enumerate(names)}

def to_matrix(block: str, rows: int = 4, cols: int = 6) -> list:
    return [list(block[i*cols:(i+1)*cols]) for i in range(rows)]

def apply_permutation(matrix: list, perm: list) -> list:
    # Direct column permutation: new_col[j] = old_col[perm[j]]
    return [[row[perm[j]] for j in range(len(perm))] for row in matrix]

def caesar_shift(text: str, shift: int) -> str:
    alpha = string.ascii_uppercase
    return ''.join(alpha[(alpha.index(c) + shift) % 26] for c in text)

def vigenere_decrypt(text: str, key: str) -> str:
    alpha = string.ascii_uppercase
    # Repeat key to match text length
    full_key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return ''.join(
        alpha[(alpha.index(text[i]) - alpha.index(full_key[i])) % 26]
        for i in range(len(text))
    )

def decrypt_quadrant(ct: str, perm: list, shift: int, key: str) -> str:
    # 1) Put into 4×6 matrix
    matrix = to_matrix(ct)
    # 2) Apply column permutation
    permuted = apply_permutation(matrix, perm)
    # 3) Flatten and apply Caesar shift
    flat = ''.join(sum(permuted, []))
    shifted = caesar_shift(flat, shift)
    # 4) Vigenère decryption
    return vigenere_decrypt(shifted, key)

def verify_cipher(raw: str) -> dict:
    # 1) Clean raw text and remove center W
    raw = raw.replace(" ", "").strip()
    cleaned = remove_center_w(raw)
    # 2) Chunk into quadrants
    quads = chunk_quadrants(cleaned)
    # 3) Parameters per quadrant
    params = {
        "NW": {"perm": [1,3,4,0,2,5], "shift": 1,  "key": "KRYPTOS"},
        "NE": {"perm": [2,0,1,5,3,4], "shift": -7, "key": "ABSCISSA"},
        "SW": {"perm": [4,3,5,1,2,0], "shift": 15, "key": "PALIMPSEST"},
        "SE": {"perm": [3,1,2,4,0,5], "shift": 8,  "key": "PALIMPSEST"},
    }
    # 4) Decrypt each
    results = {}
    for name, ct in quads.items():
        p = params[name]["perm"]
        s = params[name]["shift"]
        k = params[name]["key"]
        pt = decrypt_quadrant(ct, p, s, k)
        results[name] = pt
    return results

if __name__ == "__main__":
    # Example raw ciphertext
    raw_input = (
        "OBKR UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO "
        "TWTQSJQSSEKZZWATJKLUDIAWINFBNYP "
        "VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
    )
    decrypted = verify_cipher(raw_input)
    for quad, text in decrypted.items():
        print(f"{quad}: {text}")
