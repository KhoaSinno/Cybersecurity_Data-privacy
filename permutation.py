"""
PERMUTATION CIPHER - MÃ HÓA HOÁN VỊ
==================================

Permutation Cipher (còn gọi là Transposition Cipher) là thuật toán mã hóa dựa trên
việc sắp xếp lại vị trí các ký tự trong plaintext thay vì thay thế chúng.

CÁC LOẠI MÃ HÓA HOÁN VỊ:
1. Columnar Transposition - Hoán vị theo cột
2. Block Transposition - Hoán vị theo khối
3. Route Cipher - Mã hóa theo đường đi
4. Rail Fence Cipher - Mã hóa hàng rào

NGUYÊN LÝ HOẠT ĐỘNG:
- Sắp xếp text vào ma trận theo quy tắc
- Đọc text theo thứ tự khác để tạo ciphertext
- Key xác định cách sắp xếp và đọc

VÍ DỤ COLUMNAR TRANSPOSITION:
Key: "ZEBRA" (thứ tự: 5,2,1,4,3)
HELLO WORLD -> H E L L O
                W O R L D
Đọc theo thứ tự cột: ELRLO HLOWD

ĐIỂM MẠNH:
- Giữ nguyên tần suất ký tự (frequency analysis không hiệu quả)
- Đơn giản để thực hiện
- Có thể kết hợp với substitution cipher

ĐIỂM YẾU:
- Anagram analysis có thể phá vỡ
- Pattern recognition trong short keys
- Cần biết kích thước ma trận để giải mã
"""

import math
import numpy as np


def columnar_transposition_encrypt(text, key):
    """
    Mã hóa Columnar Transposition

    Args:
        text (str): Text cần mã hóa
        key (str): Key xác định thứ tự cột

    Returns:
        str: Text đã mã hóa
    """
    # Loại bỏ khoảng trắng và chuyển về chữ hoa
    text = ''.join(char.upper() for char in text if char.isalpha())
    key = key.upper()

    # Tính thứ tự các cột dựa trên key
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    # Tính số hàng cần thiết
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)

    # Thêm padding nếu cần
    padding_needed = num_rows * num_cols - len(text)
    text += 'X' * padding_needed

    # Tạo ma trận
    matrix = []
    for i in range(num_rows):
        row = text[i * num_cols:(i + 1) * num_cols]
        matrix.append(list(row))

    # Đọc theo thứ tự cột được sắp xếp
    encrypted = ""
    for col_index in key_order:
        for row in matrix:
            if col_index < len(row):
                encrypted += row[col_index]

    return encrypted


def columnar_transposition_decrypt(text, key):
    """
    Giải mã Columnar Transposition

    Args:
        text (str): Text đã mã hóa
        key (str): Key đã dùng để mã hóa

    Returns:
        str: Text gốc
    """
    key = key.upper()

    # Tính thứ tự các cột
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    num_cols = len(key)
    num_rows = len(text) // num_cols

    # Tạo ma trận rỗng
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    # Điền vào ma trận theo thứ tự cột đã sắp xếp
    text_index = 0
    for col_index in key_order:
        for row in range(num_rows):
            if text_index < len(text):
                matrix[row][col_index] = text[text_index]
                text_index += 1

    # Đọc theo hàng để lấy plaintext
    decrypted = ""
    for row in matrix:
        decrypted += ''.join(row)

    return decrypted.rstrip('X')  # Loại bỏ padding


def block_transposition_encrypt(text, key_matrix):
    """
    Mã hóa Block Transposition với ma trận key

    Args:
        text (str): Text cần mã hóa
        key_matrix (list): Ma trận hoán vị (permutation matrix)

    Returns:
        str: Text đã mã hóa
    """
    text = ''.join(char.upper() for char in text if char.isalpha())
    block_size = len(key_matrix)

    # Thêm padding nếu cần
    padding_needed = (block_size - len(text) % block_size) % block_size
    text += 'X' * padding_needed

    encrypted = ""

    # Xử lý từng khối
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]

        # Áp dụng hoán vị theo key_matrix
        permuted_block = ""
        for pos in key_matrix:
            if pos < len(block):
                permuted_block += block[pos]

        encrypted += permuted_block

    return encrypted


def block_transposition_decrypt(text, key_matrix):
    """
    Giải mã Block Transposition

    Args:
        text (str): Text đã mã hóa
        key_matrix (list): Ma trận hoán vị đã dùng

    Returns:
        str: Text gốc
    """
    block_size = len(key_matrix)

    # Tạo reverse permutation
    reverse_key = [0] * block_size
    for i, pos in enumerate(key_matrix):
        reverse_key[pos] = i

    decrypted = ""

    # Xử lý từng khối
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]

        # Áp dụng reverse permutation
        original_block = [''] * block_size
        for i, char in enumerate(block):
            if reverse_key[i] < len(original_block):
                original_block[reverse_key[i]] = char

        decrypted += ''.join(original_block)

    return decrypted.rstrip('X')


def rail_fence_encrypt(text, num_rails):
    """
    Mã hóa Rail Fence Cipher

    Args:
        text (str): Text cần mã hóa
        num_rails (int): Số hàng rào

    Returns:
        str: Text đã mã hóa
    """
    if num_rails <= 1:
        return text

    text = ''.join(char.upper() for char in text if char.isalpha())

    # Tạo các hàng rào
    rails = [[] for _ in range(num_rails)]

    # Xác định direction (lên/xuống)
    rail = 0
    direction = 1  # 1: xuống, -1: lên

    # Phân phối ký tự vào các hàng rào
    for char in text:
        rails[rail].append(char)

        # Thay đổi hướng khi đến biên
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1

        rail += direction

    # Nối các hàng rào lại
    encrypted = ""
    for rail in rails:
        encrypted += ''.join(rail)

    return encrypted


def rail_fence_decrypt(text, num_rails):
    """
    Giải mã Rail Fence Cipher

    Args:
        text (str): Text đã mã hóa
        num_rails (int): Số hàng rào đã dùng

    Returns:
        str: Text gốc
    """
    if num_rails <= 1:
        return text

    # Tính số ký tự trên mỗi hàng rào
    rail_lengths = [0] * num_rails
    rail = 0
    direction = 1

    for _ in text:
        rail_lengths[rail] += 1

        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1

        rail += direction

    # Phân phối text vào các hàng rào
    rails = []
    text_index = 0
    for length in rail_lengths:
        rails.append(list(text[text_index:text_index + length]))
        text_index += length

    # Đọc lại theo pattern zigzag
    decrypted = ""
    rail = 0
    direction = 1
    rail_indices = [0] * num_rails

    for _ in text:
        decrypted += rails[rail][rail_indices[rail]]
        rail_indices[rail] += 1

        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1

        rail += direction

    return decrypted


def route_cipher_encrypt(text, rows, cols, route):
    """
    Mã hóa Route Cipher

    Args:
        text (str): Text cần mã hóa
        rows (int): Số hàng ma trận
        cols (int): Số cột ma trận
        route (str): Đường đi đọc ('row', 'col', 'diagonal', 'spiral')

    Returns:
        str: Text đã mã hóa
    """
    text = ''.join(char.upper() for char in text if char.isalpha())

    # Thêm padding
    total_cells = rows * cols
    padding_needed = total_cells - len(text)
    text += 'X' * padding_needed

    # Tạo ma trận
    matrix = []
    for i in range(rows):
        row = text[i * cols:(i + 1) * cols]
        matrix.append(list(row))

    encrypted = ""

    if route == 'row':
        # Đọc theo hàng
        for row in matrix:
            encrypted += ''.join(row)

    elif route == 'col':
        # Đọc theo cột
        for col in range(cols):
            for row in range(rows):
                encrypted += matrix[row][col]

    elif route == 'diagonal':
        # Đọc theo đường chéo
        # Đường chéo chính
        for i in range(min(rows, cols)):
            encrypted += matrix[i][i]
        # Đường chéo phụ
        for i in range(min(rows, cols)):
            if i != cols - 1 - i:  # Tránh trùng lặp
                encrypted += matrix[i][cols - 1 - i]
        # Các phần tử còn lại
        for i in range(rows):
            for j in range(cols):
                if i != j and i != cols - 1 - j:
                    encrypted += matrix[i][j]

    elif route == 'spiral':
        # Đọc theo hình xoắn ốc
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            # Đọc hàng trên từ trái sang phải
            for col in range(left, right + 1):
                encrypted += matrix[top][col]
            top += 1

            # Đọc cột phải từ trên xuống dưới
            for row in range(top, bottom + 1):
                encrypted += matrix[row][right]
            right -= 1

            # Đọc hàng dưới từ phải sang trái
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    encrypted += matrix[bottom][col]
                bottom -= 1

            # Đọc cột trái từ dưới lên trên
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    encrypted += matrix[row][left]
                left += 1

    return encrypted


def print_matrix(matrix, title="Matrix"):
    """In ma trận một cách đẹp mắt"""
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{cell:2}" for cell in row))


# ================== DEMO CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    plaintext = "HELLO WORLD FROM PERMUTATION CIPHER"

    print("=== PERMUTATION CIPHER DEMO ===")
    print(f"Text gốc: {plaintext}")

    # 1. COLUMNAR TRANSPOSITION
    print("\n--- COLUMNAR TRANSPOSITION ---")
    col_key = "ZEBRA"
    col_encrypted = columnar_transposition_encrypt(plaintext, col_key)
    col_decrypted = columnar_transposition_decrypt(col_encrypted, col_key)

    print(f"Key: {col_key}")
    print(
        f"Thứ tự cột: {sorted(range(len(col_key)), key=lambda k: col_key[k])}")
    print(f"Mã hóa: {col_encrypted}")
    print(f"Giải mã: {col_decrypted}")

    # 2. BLOCK TRANSPOSITION
    print("\n--- BLOCK TRANSPOSITION ---")
    # Key matrix: hoán vị [0,1,2,3,4] -> [2,4,1,0,3]
    block_key = [2, 4, 1, 0, 3]
    block_encrypted = block_transposition_encrypt(plaintext, block_key)
    block_decrypted = block_transposition_decrypt(block_encrypted, block_key)

    print(f"Key matrix (permutation): {block_key}")
    print(f"Mã hóa: {block_encrypted}")
    print(f"Giải mã: {block_decrypted}")

    # 3. RAIL FENCE CIPHER
    print("\n--- RAIL FENCE CIPHER ---")
    rails = 4
    rail_encrypted = rail_fence_encrypt(plaintext, rails)
    rail_decrypted = rail_fence_decrypt(rail_encrypted, rails)

    print(f"Số hàng rào: {rails}")
    print(f"Mã hóa: {rail_encrypted}")
    print(f"Giải mã: {rail_decrypted}")

    # 4. ROUTE CIPHER
    print("\n--- ROUTE CIPHER ---")
    rows, cols = 6, 6

    # Route spiral
    route_encrypted = route_cipher_encrypt(plaintext, rows, cols, 'spiral')
    print(f"Ma trận {rows}x{cols}, route spiral:")
    print(f"Mã hóa: {route_encrypted}")

    # Route column
    route_col_encrypted = route_cipher_encrypt(plaintext, rows, cols, 'col')
    print(f"Route column: {route_col_encrypted}")

    print("\n=== VISUALIZATION ===")
    # Hiển thị ma trận cho columnar transposition
    clean_text = ''.join(char.upper() for char in plaintext if char.isalpha())
    padding_needed = math.ceil(
        len(clean_text) / len(col_key)) * len(col_key) - len(clean_text)
    padded_text = clean_text + 'X' * padding_needed

    num_rows = len(padded_text) // len(col_key)
    matrix = []
    for i in range(num_rows):
        row = list(padded_text[i * len(col_key):(i + 1) * len(col_key)])
        matrix.append(row)

    print(f"\nColumnar Transposition Matrix (key: {col_key}):")
    print("   " + "  ".join(col_key))
    print("   " + "  ".join(str(i) for i in range(len(col_key))))
    for i, row in enumerate(matrix):
        print(f"{i}: " + "  ".join(row))

    print("\n=== GIẢI THÍCH CHI TIẾT ===")
    print("Permutation Cipher thay đổi VỊ TRÍ thay vì GIÁ TRỊ của ký tự:")
    print("1. Columnar: Sắp xếp vào ma trận, đọc theo thứ tự cột")
    print("2. Block: Hoán vị từng khối theo pattern cố định")
    print("3. Rail Fence: Viết zigzag trên nhiều hàng, đọc theo hàng")
    print("4. Route: Viết vào ma trận, đọc theo route đặc biệt")
    print("\nBảo mật: Frequency analysis không hiệu quả!")
    print("Nhược điểm: Anagram analysis và pattern recognition có thể phá vỡ.")

# Wrapper functions for Streamlit compatibility
def encrypt_permutation(text, key):
    """
    Wrapper function for permutation encryption
    
    Args:
        text (str): Text to encrypt
        key (str): Key for permutation (will be converted to columnar key)
        
    Returns:
        str: Encrypted text
    """
    try:
        # Convert string key to columnar key
        if key.isdigit():
            # If key is numeric, use it as-is
            return columnar_transposition_encrypt(text, key)
        else:
            # If key is alphabetic, use it for columnar transposition
            return columnar_transposition_encrypt(text, key)
    except:
        # Fallback to simple columnar transposition
        return columnar_transposition_encrypt(text, str(key))

def decrypt_permutation(text, key):
    """
    Wrapper function for permutation decryption
    
    Args:
        text (str): Text to decrypt
        key (str): Key for permutation
        
    Returns:
        str: Decrypted text
    """
    try:
        # Convert string key to columnar key
        if key.isdigit():
            # If key is numeric, use it as-is
            return columnar_transposition_decrypt(text, key)
        else:
            # If key is alphabetic, use it for columnar transposition
            return columnar_transposition_decrypt(text, key)
    except:
        # Fallback to simple columnar transposition
        return columnar_transposition_decrypt(text, str(key))
