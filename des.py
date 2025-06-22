"""
DES (DATA ENCRYPTION STANDARD) - MÃ HÓA KHỐI HIỆN ĐẠI
===================================================

DES là thuật toán mã hóa khối được IBM phát triển vào thập niên 1970 và được
NIST chấp nhận làm chuẩn mã hóa của Mỹ từ 1977-2001. Đây là nền tảng của
mã hóa hiện đại.

ĐẶC ĐIỂM CỦA DES:
- Mã hóa khối 64-bit với key 56-bit (thực tế 64-bit nhưng 8 bit parity)
- Sử dụng mạng Feistel với 16 rounds
- Kết hợp substitution và permutation
- Symmetric cipher (cùng key cho encrypt/decrypt)

CẤU TRÚC DES:
1. Initial Permutation (IP)
2. 16 rounds Feistel Network
3. Final Permutation (IP⁻¹)

MỖI ROUND FEISTEL:
- Chia 64-bit thành 2 nửa: L và R (mỗi nửa 32-bit)
- L(i+1) = R(i)
- R(i+1) = L(i) ⊕ F(R(i), K(i))

HÀM F (CORE FUNCTION):
1. Expansion (32-bit -> 48-bit)
2. XOR với round key (48-bit)
3. S-boxes substitution (48-bit -> 32-bit)
4. Permutation (32-bit -> 32-bit)

KEY SCHEDULE:
- 64-bit key -> 56-bit (loại bỏ parity bits)
- Tạo 16 round keys mỗi 48-bit

ĐIỂM MẠNH:
- Cơ sở toán học vững chắc
- Kết hợp substitution và permutation hiệu quả
- Đã được kiểm tra kỹ lưỡng

ĐIỂM YẾU:
- Key size 56-bit quá nhỏ (có thể brute force)
- Block size 64-bit nhỏ (birthday attack)
- Đã bị thay thế bởi AES
"""

# DES Constants và Tables

# Initial Permutation Table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Final Permutation Table (IP inverse)
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Expansion Table (32-bit -> 48-bit)
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Permutation Table for F function
P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# S-boxes (8 boxes, each 4x16)
S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# Key Schedule Tables
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Left shift amounts for each round
LEFT_SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def string_to_bits(text):
    """
    Chuyển đổi string thành binary representation

    Args:
        text (str): Text cần chuyển đổi

    Returns:
        list: List các bit (0 hoặc 1)
    """
    bits = []
    for char in text:
        byte = ord(char)
        for i in range(8):
            bits.append((byte >> (7 - i)) & 1)
    return bits


def bits_to_string(bits):
    """
    Chuyển đổi binary representation thành string

    Args:
        bits (list): List các bit

    Returns:
        str: String tương ứng
    """
    chars = []
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(bits):
                byte = (byte << 1) | bits[i + j]
        chars.append(chr(byte))
    return ''.join(chars)


def permute(bits, table):
    """
    Thực hiện permutation theo table

    Args:
        bits (list): Input bits
        table (list): Permutation table

    Returns:
        list: Permuted bits
    """
    return [bits[i - 1] for i in table]


def left_shift(bits, n):
    """
    Left shift circular

    Args:
        bits (list): Input bits
        n (int): Số vị trí shift

    Returns:
        list: Shifted bits
    """
    return bits[n:] + bits[:n]


def xor(bits1, bits2):
    """
    XOR hai list bits

    Args:
        bits1, bits2 (list): Hai list bits

    Returns:
        list: Kết quả XOR
    """
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]


def s_box_substitution(bits):
    """
    Thực hiện S-box substitution

    Args:
        bits (list): 48-bit input

    Returns:
        list: 32-bit output
    """
    result = []

    # Chia 48-bit thành 8 nhóm 6-bit
    for i in range(8):
        # Lấy 6-bit cho S-box thứ i
        group = bits[i * 6:(i + 1) * 6]

        # Bit đầu và cuối tạo row (2-bit)
        row = (group[0] << 1) | group[5]

        # 4 bit giữa tạo column (4-bit)
        col = (group[1] << 3) | (group[2] << 2) | (group[3] << 1) | group[4]

        # Lấy giá trị từ S-box
        val = S_BOXES[i][row][col]

        # Chuyển thành 4-bit binary
        for j in range(4):
            result.append((val >> (3 - j)) & 1)

    return result


def f_function(right, round_key):
    """
    Hàm F của DES (core function)

    Args:
        right (list): 32-bit right half
        round_key (list): 48-bit round key

    Returns:
        list: 32-bit output
    """
    # 1. Expansion (32-bit -> 48-bit)
    expanded = permute(right, E)

    # 2. XOR với round key
    xored = xor(expanded, round_key)

    # 3. S-box substitution (48-bit -> 32-bit)
    substituted = s_box_substitution(xored)

    # 4. Permutation
    result = permute(substituted, P)

    return result


def generate_round_keys(key):
    """
    Tạo 16 round keys từ master key

    Args:
        key (list): 64-bit master key

    Returns:
        list: 16 round keys, mỗi key 48-bit
    """
    # PC1: Loại bỏ parity bits (64-bit -> 56-bit)
    key_56 = permute(key, PC1)

    # Chia thành 2 nửa 28-bit
    left = key_56[:28]
    right = key_56[28:]

    round_keys = []

    for i in range(16):
        # Left shift
        left = left_shift(left, LEFT_SHIFTS[i])
        right = left_shift(right, LEFT_SHIFTS[i])

        # Kết hợp lại
        combined = left + right

        # PC2: Tạo 48-bit round key
        round_key = permute(combined, PC2)
        round_keys.append(round_key)

    return round_keys


def des_encrypt_block(plaintext_block, key):
    """
    Mã hóa một block 64-bit bằng DES

    Args:
        plaintext_block (list): 64-bit plaintext
        key (list): 64-bit key

    Returns:
        list: 64-bit ciphertext
    """
    # Tạo round keys
    round_keys = generate_round_keys(key)

    # Initial Permutation
    current = permute(plaintext_block, IP)

    # Chia thành 2 nửa
    left = current[:32]
    right = current[32:]

    # 16 rounds Feistel
    for i in range(16):
        new_left = right[:]
        new_right = xor(left, f_function(right, round_keys[i]))

        left = new_left
        right = new_right

    # Swap cuối cùng (32-bit swap)
    final = right + left

    # Final Permutation
    ciphertext = permute(final, FP)

    return ciphertext


def des_decrypt_block(ciphertext_block, key):
    """
    Giải mã một block 64-bit bằng DES

    Args:
        ciphertext_block (list): 64-bit ciphertext
        key (list): 64-bit key

    Returns:
        list: 64-bit plaintext
    """
    # Tạo round keys (reverse order cho decryption)
    round_keys = generate_round_keys(key)
    round_keys.reverse()

    # Initial Permutation
    current = permute(ciphertext_block, IP)

    # Chia thành 2 nửa
    left = current[:32]
    right = current[32:]

    # 16 rounds Feistel với round keys đảo ngược
    for i in range(16):
        new_left = right[:]
        new_right = xor(left, f_function(right, round_keys[i]))

        left = new_left
        right = new_right

    # Swap cuối cùng
    final = right + left

    # Final Permutation
    plaintext = permute(final, FP)

    return plaintext


def des_encrypt(plaintext, key):
    """
    Mã hóa text bằng DES

    Args:
        plaintext (str): Text cần mã hóa
        key (str): Key (8 ký tự)

    Returns:
        bytes: Ciphertext
    """
    # Padding plaintext đến bội số của 8
    while len(plaintext) % 8 != 0:
        plaintext += '\0'

    # Chuyển key thành bits
    key_bits = string_to_bits(key[:8])  # Chỉ lấy 8 ký tự đầu

    ciphertext_bits = []

    # Mã hóa từng block 64-bit
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        block_bits = string_to_bits(block)

        encrypted_block = des_encrypt_block(block_bits, key_bits)
        ciphertext_bits.extend(encrypted_block)

    return bits_to_string(ciphertext_bits).encode('latin-1')


def des_decrypt(ciphertext, key):
    """
    Giải mã ciphertext bằng DES

    Args:
        ciphertext (bytes): Ciphertext
        key (str): Key (8 ký tự)

    Returns:
        str: Plaintext đã giải mã
    """
    ciphertext_str = ciphertext.decode('latin-1')
    ciphertext_bits = string_to_bits(ciphertext_str)

    # Chuyển key thành bits
    key_bits = string_to_bits(key[:8])

    plaintext_bits = []

    # Giải mã từng block 64-bit
    for i in range(0, len(ciphertext_bits), 64):
        block_bits = ciphertext_bits[i:i+64]

        decrypted_block = des_decrypt_block(block_bits, key_bits)
        plaintext_bits.extend(decrypted_block)

    plaintext = bits_to_string(plaintext_bits)
    return plaintext.rstrip('\0')  # Loại bỏ padding


# Wrapper functions for Streamlit compatibility
def encrypt_des(text, key):
    """
    Wrapper function for DES encryption
    
    Args:
        text (str): Text to encrypt
        key (str): 8-character key
        
    Returns:
        str: Encrypted text in hex format
    """
    try:
        # Ensure key is 8 characters
        if len(key) < 8:
            key = key.ljust(8, '0')
        elif len(key) > 8:
            key = key[:8]
        
        encrypted_bytes = des_encrypt(text.encode('utf-8'), key)
        return encrypted_bytes.hex().upper()
    except Exception as e:
        return f"Error: {str(e)}"

def decrypt_des(ciphertext, key):
    """
    Wrapper function for DES decryption
    
    Args:
        ciphertext (str): Hex string to decrypt
        key (str): 8-character key
        
    Returns:
        str: Decrypted text
    """
    try:
        # Ensure key is 8 characters
        if len(key) < 8:
            key = key.ljust(8, '0')
        elif len(key) > 8:
            key = key[:8]
        
        # Convert hex to bytes
        cipher_bytes = bytes.fromhex(ciphertext)
        decrypted_bytes = des_decrypt(cipher_bytes, key)
        return decrypted_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {str(e)}"


# ================== DEMO CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    print("=== DES (DATA ENCRYPTION STANDARD) DEMO ===")

    # Test data
    plaintext = "HELLO123"  # 8 ký tự (64-bit)
    key = "MYKEY123"       # 8 ký tự (64-bit)

    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")

    # Mã hóa
    print("\n--- MÃ HÓA ---")
    ciphertext = des_encrypt(plaintext, key)
    print(f"Ciphertext (hex): {ciphertext.hex()}")

    # Giải mã
    print("\n--- GIẢI MÃ ---")
    decrypted = des_decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted}")
    print(f"Giải mã thành công: {plaintext == decrypted}")

    print("\n=== DEMO CHI TIẾT CẤU TRÚC DES ===")

    # Convert plaintext và key thành bits để demo
    plaintext_bits = string_to_bits(plaintext)
    key_bits = string_to_bits(key)

    print(f"Plaintext bits (64-bit): {plaintext_bits}")
    print(f"Key bits (64-bit): {key_bits}")

    # Demo Initial Permutation
    ip_result = permute(plaintext_bits, IP)
    print(
        f"Sau Initial Permutation: {ip_result[:16]}... (hiển thị 16 bit đầu)")

    # Demo key schedule
    round_keys = generate_round_keys(key_bits)
    print(f"Số round keys được tạo: {len(round_keys)}")
    print(
        f"Round key 1 (48-bit): {round_keys[0][:16]}... (hiển thị 16 bit đầu)")

    # Demo F function
    left_half = ip_result[:32]
    right_half = ip_result[32:]
    f_result = f_function(right_half, round_keys[0])
    print(
        f"F function output (32-bit): {f_result[:16]}... (hiển thị 16 bit đầu)")

    print("\n=== GIẢI THÍCH CẤU TRÚC DES ===")
    print("DES là mã hóa khối 64-bit với key 56-bit:")
    print("1. Initial Permutation: Trộn lẫn vị trí bit")
    print("2. 16 Feistel rounds: Mỗi round sử dụng hàm F")
    print("3. Final Permutation: Hoán vị cuối cùng")
    print("\nHàm F kết hợp:")
    print("- Expansion: 32→48 bit")
    print("- XOR với round key")
    print("- S-boxes: 48→32 bit (substitution)")
    print("- Permutation: Trộn lẫn bit")
    print("\nKey Schedule tạo 16 round keys từ master key")
    print("\n*** DES hiện tại KHÔNG AN TOÀN do key size nhỏ! ***")
    print("*** Chỉ sử dụng cho mục đích giáo dục ***")
