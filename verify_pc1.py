# Verify PC-1 permutation for DES

def apply_pc1(key_64bit):
    # PC-1 table
    pc1_table = [
        57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
    ]

    # Apply PC-1 permutation
    key_56bit = ''.join([key_64bit[i - 1] for i in pc1_table])
    return key_56bit


# Key 'MYSECRET' in binary
key_64bit = (
    "01001101"  # M
    "01011001"  # Y
    "01010011"  # S
    "01000101"  # E
    "01000011"  # C
    "01010010"  # R
    "01000101"  # E
    "01010100"  # T
)

# Apply PC-1
result_56bit = apply_pc1(key_64bit)

# Split into C0 and D0
C0 = result_56bit[:28]
D0 = result_56bit[28:]

# Print results
print("After PC-1:", result_56bit)
print("C0:", C0)
print("D0:", D0)
