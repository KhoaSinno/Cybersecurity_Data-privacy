"""
HILL CIPHER - THUẬT TOÁN MÃ HÓA TUYẾN TÍNH
=========================================

Hill Cipher được phát minh bởi Lester S. Hill năm 1929. Đây là thuật toán mã hóa
dựa trên đại số tuyến tính, sử dụng phép nhân ma trận trong modulo 26.

NGUYÊN LÝ HOẠT ĐỘNG:
- Chia plaintext thành các khối có kích thước bằng kích thước ma trận key
- Chuyển đổi ký tự thành số (A=0, B=1, ..., Z=25)
- Nhân vector plaintext với ma trận key trong modulo 26
- Chuyển đổi kết quả về ký tự

CÔNG THỨC TOÁN HỌC:
- Mã hóa: C = (K × P) mod 26
- Giải mã: P = (K⁻¹ × C) mod 26
Trong đó: K = ma trận key, P = vector plaintext, C = vector ciphertext

VÍ DỤ MA TRẬN KEY 2x2:
[3  2]
[5  7]

ĐIỂM MẠNH:
- Dựa trên toán học vững chắc
- Mã hóa theo khối, an toàn hơn substitution đơn giản
- Tần suất ký tự đơn lẻ không còn ý nghĩa

ĐIỂM YẾU:
- Ma trận key phải khả nghịch trong modulo 26
- Dễ bị tấn công known-plaintext
- Cần biết kích thước ma trận để giải mã
"""

import numpy as np
from math import gcd


def mod_inverse(a, m):
    """
    Tìm nghịch đảo modular của a trong modulo m

    Args:
        a (int): Số cần tìm nghịch đảo
        m (int): Modulo

    Returns:
        int: Nghịch đảo của a mod m, hoặc None nếu không tồn tại
    """
    # Kiểm tra gcd(a, m) = 1
    if gcd(a, m) != 1:
        return None

    # Sử dụng Extended Euclidean Algorithm
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y

    _, x, _ = extended_gcd(a % m, m)
    return (x % m + m) % m


def matrix_mod_inverse(matrix, mod):
    """
    Tìm nghịch đảo của ma trận trong modulo

    Args:
        matrix (numpy.ndarray): Ma trận cần tìm nghịch đảo
        mod (int): Modulo

    Returns:
        numpy.ndarray: Ma trận nghịch đảo, hoặc None nếu không tồn tại
    """
    n = matrix.shape[0]
    det = int(np.round(np.linalg.det(matrix))) % mod

    # Tìm nghịch đảo của determinant
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        return None

    # Tính ma trận adjugate (adjoint)
    if n == 2:
        # Với ma trận 2x2: adj = [[d, -b], [-c, a]]
        adj = np.array([[matrix[1, 1], -matrix[0, 1]],
                       [-matrix[1, 0], matrix[0, 0]]])
    else:
        # Với ma trận lớn hơn, sử dụng công thức cofactor
        adj = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                # Tính minor
                minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                cofactor = ((-1) ** (i + j)) * \
                    int(np.round(np.linalg.det(minor)))
                adj[j, i] = cofactor % mod  # Chú ý: transpose

    # Ma trận nghịch đảo = (det⁻¹ × adj) mod m
    inv_matrix = (det_inv * adj) % mod
    return inv_matrix


def text_to_numbers(text):
    """
    Chuyển đổi text thành list các số (A=0, B=1, ..., Z=25)

    Args:
        text (str): Text cần chuyển đổi

    Returns:
        list: List các số tương ứng
    """
    # Loại bỏ ký tự không phải chữ cái và chuyển về chữ hoa
    text = ''.join(char.upper() for char in text if char.isalpha())
    return [ord(char) - ord('A') for char in text]


def numbers_to_text(numbers):
    """
    Chuyển đổi list số thành text

    Args:
        numbers (list): List các số

    Returns:
        str: Text tương ứng
    """
    return ''.join(chr(num + ord('A')) for num in numbers)


def encrypt_hill(text, key_matrix):
    """
    Mã hóa text bằng Hill Cipher

    Args:
        text (str): Text cần mã hóa
        key_matrix (numpy.ndarray): Ma trận key

    Returns:
        str: Text đã mã hóa
    """
    n = key_matrix.shape[0]  # Kích thước ma trận (n x n)
    numbers = text_to_numbers(text)

    # Thêm padding nếu cần thiết
    while len(numbers) % n != 0:
        numbers.append(ord('X') - ord('A'))  # Thêm 'X' làm padding

    encrypted_numbers = []

    # Mã hóa từng khối
    for i in range(0, len(numbers), n):
        # Lấy khối n ký tự
        block = np.array(numbers[i:i+n])

        # Nhân ma trận: C = K × P mod 26
        encrypted_block = (key_matrix @ block) % 26
        encrypted_numbers.extend(encrypted_block.tolist())

    return numbers_to_text(encrypted_numbers)


def decrypt_hill(text, key_matrix):
    """
    Giải mã text đã được mã hóa bằng Hill Cipher

    Args:
        text (str): Text đã mã hóa
        key_matrix (numpy.ndarray): Ma trận key đã dùng để mã hóa

    Returns:
        str: Text gốc đã giải mã, hoặc None nếu ma trận không khả nghịch
    """
    # Tìm ma trận nghịch đảo của key
    inv_key_matrix = matrix_mod_inverse(key_matrix, 26)
    if inv_key_matrix is None:
        print("Ma trận key không khả nghịch trong modulo 26!")
        return None

    n = key_matrix.shape[0]
    numbers = text_to_numbers(text)

    decrypted_numbers = []

    # Giải mã từng khối
    for i in range(0, len(numbers), n):
        # Lấy khối n ký tự
        block = np.array(numbers[i:i+n])

        # Nhân ma trận nghịch đảo: P = K⁻¹ × C mod 26
        decrypted_block = (inv_key_matrix @ block) % 26
        decrypted_numbers.extend(decrypted_block.tolist())

    return numbers_to_text(decrypted_numbers)


def is_matrix_invertible(matrix, mod=26):
    """
    Kiểm tra ma trận có khả nghịch trong modulo hay không

    Args:
        matrix (numpy.ndarray): Ma trận cần kiểm tra
        mod (int): Modulo (mặc định 26)

    Returns:
        bool: True nếu khả nghịch, False nếu không
    """
    det = int(np.round(np.linalg.det(matrix))) % mod
    return gcd(det, mod) == 1


# ================== DEMO CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    # Text và ma trận key demo
    plaintext = "HELLO WORLD"

    # Ma trận key 2x2 (khả nghịch trong mod 26)
    key_matrix = np.array([[3, 2],
                          [5, 7]], dtype=int)

    print("=== HILL CIPHER DEMO ===")
    print(f"Text gốc: {plaintext}")
    print(f"Ma trận key:")
    print(key_matrix)

    # Kiểm tra ma trận có khả nghịch không
    if not is_matrix_invertible(key_matrix):
        print("CẢNH BÁO: Ma trận key không khả nghịch trong modulo 26!")
    else:
        print("Ma trận key khả nghịch trong modulo 26 ✓")

    # Mã hóa
    encrypted = encrypt_hill(plaintext, key_matrix)
    print(f"Text đã mã hóa: {encrypted}")

    # Giải mã
    decrypted = decrypt_hill(encrypted, key_matrix)
    print(f"Text đã giải mã: {decrypted}")

    # Tính ma trận nghịch đảo để demo
    inv_matrix = matrix_mod_inverse(key_matrix, 26)
    print(f"\nMa trận nghịch đảo:")
    print(inv_matrix)

    print("\n=== GIẢI THÍCH CHI TIẾT ===")
    print("Hill Cipher sử dụng phép nhân ma trận:")
    print("1. Chuyển text thành vector số (A=0, B=1, ..., Z=25)")
    print("2. Chia thành các khối có kích thước = kích thước ma trận")
    print("3. Mã hóa: C = (K × P) mod 26")
    print("4. Giải mã: P = (K⁻¹ × C) mod 26")
    print("\nĐây là thuật toán mã hóa khối đầu tiên trong lịch sử!")

    print("\n=== VÍ DỤ TÍNH TOÁN ===")
    # Demo tính toán cho 2 ký tự đầu
    demo_text = "HE"
    demo_numbers = text_to_numbers(demo_text)
    print(f"'{demo_text}' -> {demo_numbers}")

    # Nhân ma trận
    block = np.array(demo_numbers)
    result = (key_matrix @ block) % 26
    print(f"Ma trận × vector = {key_matrix} × {block} = {result} (mod 26)")
    print(f"Kết quả: {numbers_to_text(result)}")
