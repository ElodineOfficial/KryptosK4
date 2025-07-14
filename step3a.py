# Confirmation of new Stage 3 using the provided intermediate and tour

# 24‑letter constant from second‐layer Vigenère
PLAINTEXT = "DLOCITRCOOAEENTENTCLBOHL"

# Geometric tour index sequence (Tour‑1)
TOUR_SEQUENCE = [
    0, 9, 16, 21, 14, 19, 8, 3,
    10, 5, 12, 17, 22, 15, 20, 11,
    6, 1, 4, 13, 18, 23, 2, 7
]

# Layout into 4×6 grid (row-major)
rows, cols = 4, 6
grid = [PLAINTEXT[i*cols:(i+1)*cols] for i in range(rows)]

# Flatten and apply the tour
flat = ''.join(grid)
final = ''.join(flat[i] for i in TOUR_SEQUENCE)

print("4×6 Grid:")
for row in grid:
    print(' '.join(row))
print("\nFinal plaintext from tour:", final)

# Verify
expected = "DONOTLOCATETHEBERLINCLOC"
assert final == expected, f"Got {final}, expected {expected}"
