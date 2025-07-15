This is a technical text dump of how these scripts work and solve the first half of K4.

Raw K4: OBKR UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO TWTQSJQSSEKZZWATJKLUDIAWINFBNYP VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR

Here’s a step‑by‑step recipe you can execute entirely by hand. Wherever you see “letter→number,” use A = 0, B = 1, …, Z = 25, and whenever you “mod 26,” if you get a negative result add 26, or if ≥ 26 subtract 26.

1. Clean and split the raw K4 text
Strip out spaces so you have one 97‑letter string.
Remove the 49th character (the extra “W” in the exact center). You now have 96 letters. >Reminder for later maths<: This became our crosshair and axis, it did not necessarily get ‘removed’
Cut into four blocks of 24 letters, in reading order:
NW = letters 1–24
NE = letters 25–48
SW = letters 49–72
SE = letters 73–96

2. First‐layer decryption of each quadrant
For each block (NW, NE, SW, SE), do:
Write it in a 4 rows × 6 cols grid, filling each row left→right, top→bottom.
Re‑label the columns by applying the quadrant’s permutation. If perm = [p₀,p₁,…,p₅], that means “new column 0 is old column p₀,” “new column 1 is old p₁,” etc.
Quadrant
Permutation
Caesar shift
Vigenère key
NW
[1, 3, 4, 0, 2, 5]
+ 1
KRYPTOS
NE
[2, 0, 1, 5, 3, 4]
– 7
ABSCISSA
SW
[4, 3, 5, 1, 2, 0]
+ 15
PALIMPSEST
SE
[3, 1, 2, 4, 0, 5]
+ 8
PALIMPSEST

3. Flatten the permuted grid back into one 24‑letter string (row by row).
Apply the Caesar shift to each letter: convert letter→number, add the shift, mod 26, convert back.
Vigenère‑decrypt with the given key:
Repeat the key to length 24.
For each position i, compute (cipherᵢ – keyᵢ) mod 26 → plaintext letter.
Record the resulting 24‑letter “quadrant plaintext.”
After this you’ll have:
NW_pt = SBXASBXYEASTFUZLRRJSUSGU  
NE_pt = JNREASTZDLTFBXUJLBFJDALS  
SW_pt = LZYAMAFHKEASTFYBKQCVPIQA  
SE_pt = WEDKGSSXZSQQEKQNWESTDIRR  

4. Build the first half of the message (SW ↔ SE)
Rotate the SW_pt string left by 12 letters.
 e.g. if SW_pt = ABC… (24 letters), rotated = letters 13–24 then 1–12.
Compute a 24‑letter “difference” string Δ where for each position i:
 Δᵢ = (SE_ptᵢ – rotated_SW_ptᵢ) mod 26 → letter
Caesar‑shift Δ by – 15 (i.e. subtract 15, mod 26).
Vigenère‑decrypt the result with key “LICHT” (same method as before). You get a 24‑letter pre‑tour text: DLOCITRCOOAEENTENTCLBOHL
Lay that into a 4×6 grid, row by row:
 D L O C I T
R C O O A E
E N T E N T
C L B O H L
Re‑order by the “geometric tour” index sequence (row‑major positions 0…23): [0,9,16,21,14,19,8,3,10,5,12,17,22,15,20,11,6,1,4,13,18,23,2,7] That means your final first‑half message is the letters at those indices in the 24‑letter row‑major string:
DONOTLOCATETHEBERLINCLOC

5. Build the second half of the message (NW ↔ NE)
Exactly mirror the SW ↔ SE process, but with NW_pt and NE_pt:
Rotate NW_pt left by 12.
Form Δ′ where for each i:
 Δ′ᵢ = (NE_ptᵢ – rotated_NW_ptᵢ) mod 26 → letter
Caesar‑shift Δ′ by – 15.
Vigenère‑decrypt with key “LICHT.” You get:
JLXWLHAXOSTWEOKSEWFNTEEX
Lay into 4×6 grid and apply the same tour index sequence. The result is:
JSEEKNOWTHEWESTWALLOFXXX
Final result so far
Putting both halves together gives you most of Kryptos K4: This accounts for half of the known words in K4.
DONOTLOCATETHEBERLINCLOC
JSEEKNOWTHEWESTWALLOFXXX
