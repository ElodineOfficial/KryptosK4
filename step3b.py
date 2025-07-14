import string

# Data and mappings
alphabet = string.ascii_uppercase
alpha_idx = {c: i for i, c in enumerate(alphabet)}

# Inputs
NW = "SBXASBXYEASTFUZLRRJSUSGU"
ROT = 12
KEY = "LICHT"
PRE_TOUR = "JLXWLHAXOSTWEOKSEWFNTEEX"

# Step 1: Rotate NW by 12
rotated_NW = NW[ROT:] + NW[:ROT]

# Display header
header = f"{'i':>2} | {'NW_rot':^6} | {'P':^1} | {'K':^1} | {'V=P+K':^5} | {'C=(V+15)':^8} | {'NE':^2}"
print(header)
print("-" * len(header))

# Compute each step for positions 0–23
for i in range(len(PRE_TOUR)):
    nw_char = rotated_NW[i]
    p_char = PRE_TOUR[i]
    k_char = KEY[i % len(KEY)]
    
    # Vigenère encrypt step (P+K mod 26)
    v_val = (alpha_idx[p_char] + alpha_idx[k_char]) % 26
    v_char = alphabet[v_val]
    
    # Caesar forward +15
    c_val = (v_val + 15) % 26
    c_char = alphabet[c_val]
    
    # Compute NE letter: NW_rot + caesar mod 26
    ne_val = (alpha_idx[nw_char] + c_val) % 26
    ne_char = alphabet[ne_val]
    
    # Print row
    print(f"{i:2d} | {nw_char:^6} | {p_char:^1} | {k_char:^1} | {v_char:^5} | {c_char:^8} | {ne_char:^2}")

# Final corrected NE string
corrected_NE = "".join(
    alphabet[(alpha_idx[rotated_NW[i]] + (alpha_idx[PRE_TOUR[i]] + alpha_idx[KEY[i % len(KEY)]]) % 26 + 15) % 26]
    for i in range(len(PRE_TOUR))
)
print("\nCorrected NE string:", corrected_NE)
