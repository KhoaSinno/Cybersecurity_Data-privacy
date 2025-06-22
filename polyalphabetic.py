"""
POLYALPHABETIC SUBSTITUTION CIPHER - MÃ HÓA THAY THẾ ĐA BẢNG
===========================================================

Mã hóa thay thế đa bảng là một phương pháp sử dụng nhiều bảng chữ cái thay thế khác nhau
để mã hóa plaintext. Mỗi ký tự được mã hóa bằng một bảng khác nhau, làm cho frequency
analysis trở nên khó khăn hơn nhiều.

CÁC LOẠI MÃ HÓA ĐA BẢNG:
1. Vigenère Cipher (đã implement riêng)
2. Beaufort Cipher
3. Autokey Cipher
4. Running Key Cipher

NGUYÊN LÝ HOẠT ĐỘNG:
- Sử dụng nhiều Caesar Cipher với shift khác nhau
- Key xác định shift cho từng vị trí
- Key có thể được lặp lại, tự động tạo, hoặc từ text khác

VÍ DỤ:
Với key pattern [3, 7, 12]:
Position 0: Caesar shift 3
Position 1: Caesar shift 7  
Position 2: Caesar shift 12
Position 3: Caesar shift 3 (lặp lại)
...

ĐIỂM MẠNH:
- Phá vỡ pattern frequency của single substitution
- Khó phân tích hơn Caesar cipher
- Có thể sử dụng key rất dài

ĐIỂM YẾU:
- Vẫn có thể bị phá vỡ bằng Kasiski examination
- Index of Coincidence có thể xác định độ dài key
- Không an toàn với thuật toán hiện đại
"""

import random
from collections import Counter


def beaufort_encrypt(text, key):
    """
    Mã hóa Beaufort Cipher (biến thể của Vigenère)

    Công thức: C(i) = (K(i) - P(i)) mod 26

    Args:
        text (str): Text cần mã hóa
        key (str): Key mã hóa

    Returns:
        str: Text đã mã hóa
    """
    result = []
    key = key.upper()
    text = text.upper()

    key_len = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            # Beaufort: (key_char - plain_char) mod 26
            shift = (ord(key[key_index % key_len]) - ord(char)) % 26
            encrypted_char = chr(shift + ord('A'))
            result.append(encrypted_char)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def beaufort_decrypt(text, key):
    """
    Giải mã Beaufort Cipher

    Beaufort cipher là reciprocal (tự nghịch đảo): decrypt = encrypt

    Args:
        text (str): Text đã mã hóa
        key (str): Key đã dùng để mã hóa

    Returns:
        str: Text gốc
    """
    return beaufort_encrypt(text, key)  # Beaufort is reciprocal


def autokey_encrypt(text, key):
    """
    Mã hóa Autokey Cipher

    Key ban đầu + plaintext làm key mở rộng

    Args:
        text (str): Text cần mã hóa
        key (str): Key ban đầu

    Returns:
        str: Text đã mã hóa
    """
    result = []
    key = key.upper()
    text = text.upper()

    # Tạo extended key: key + plaintext
    extended_key = key
    for char in text:
        if char.isalpha():
            extended_key += char

    key_index = 0

    for char in text:
        if char.isalpha():
            # Vigenère encryption với extended key
            shift = ord(extended_key[key_index]) - ord('A')
            encrypted_char = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(encrypted_char)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def autokey_decrypt(text, key):
    """
    Giải mã Autokey Cipher

    Args:
        text (str): Text đã mã hóa
        key (str): Key ban đầu

    Returns:
        str: Text gốc
    """
    result = []
    key = key.upper()
    text = text.upper()

    # Tạo extended key từ key ban đầu + plaintext đã giải mã
    extended_key = key
    key_index = 0

    for char in text:
        if char.isalpha():
            # Giải mã bằng key hiện tại
            shift = ord(extended_key[key_index]) - ord('A')
            decrypted_char = chr(
                (ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            result.append(decrypted_char)

            # Thêm ký tự đã giải mã vào extended key
            extended_key += decrypted_char
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def running_key_encrypt(text, running_key):
    """
    Mã hóa Running Key Cipher

    Sử dụng một text dài (sách, bài thơ) làm key

    Args:
        text (str): Text cần mã hóa
        running_key (str): Text dài làm key

    Returns:
        str: Text đã mã hóa
    """
    result = []
    text = text.upper()
    running_key = running_key.upper()

    # Loại bỏ ký tự không phải chữ cái từ running key
    clean_key = ''.join(char for char in running_key if char.isalpha())

    key_index = 0

    for char in text:
        if char.isalpha():
            if key_index >= len(clean_key):
                # Nếu key hết, có thể lặp lại hoặc báo lỗi
                key_index = key_index % len(clean_key)

            # Vigenère encryption
            shift = ord(clean_key[key_index]) - ord('A')
            encrypted_char = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(encrypted_char)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def running_key_decrypt(text, running_key):
    """
    Giải mã Running Key Cipher

    Args:
        text (str): Text đã mã hóa
        running_key (str): Text dài đã dùng làm key

    Returns:
        str: Text gốc
    """
    result = []
    text = text.upper()
    running_key = running_key.upper()

    # Loại bỏ ký tự không phải chữ cái từ running key
    clean_key = ''.join(char for char in running_key if char.isalpha())

    key_index = 0

    for char in text:
        if char.isalpha():
            if key_index >= len(clean_key):
                key_index = key_index % len(clean_key)

            # Vigenère decryption
            shift = ord(clean_key[key_index]) - ord('A')
            decrypted_char = chr(
                (ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def periodic_key_encrypt(text, key_pattern):
    """
    Mã hóa với key pattern tuần hoàn

    Args:
        text (str): Text cần mã hóa
        key_pattern (list): List các shift values

    Returns:
        str: Text đã mã hóa
    """
    result = []
    text = text.upper()

    pattern_index = 0

    for char in text:
        if char.isalpha():
            # Caesar shift với pattern hiện tại
            shift = key_pattern[pattern_index % len(key_pattern)]
            encrypted_char = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(encrypted_char)
            pattern_index += 1
        else:
            result.append(char)

    return ''.join(result)


def periodic_key_decrypt(text, key_pattern):
    """
    Giải mã với key pattern tuần hoàn

    Args:
        text (str): Text đã mã hóa
        key_pattern (list): List các shift values đã dùng

    Returns:
        str: Text gốc
    """
    result = []
    text = text.upper()

    pattern_index = 0

    for char in text:
        if char.isalpha():
            # Caesar decrypt với pattern hiện tại
            shift = key_pattern[pattern_index % len(key_pattern)]
            decrypted_char = chr(
                (ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            result.append(decrypted_char)
            pattern_index += 1
        else:
            result.append(char)

    return ''.join(result)


def analyze_frequency(text):
    """
    Phân tích tần suất ký tự

    Args:
        text (str): Text cần phân tích

    Returns:
        dict: Dictionary tần suất ký tự
    """
    text = ''.join(char.upper() for char in text if char.isalpha())
    total_chars = len(text)

    if total_chars == 0:
        return {}

    counter = Counter(text)
    frequency = {char: (count / total_chars) * 100 for char,
                 count in counter.items()}

    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))


def index_of_coincidence(text):
    """
    Tính Index of Coincidence để ước lượng độ dài key

    IC = Σ(fi(fi-1)) / (n(n-1))

    Args:
        text (str): Text cần phân tích

    Returns:
        float: Index of Coincidence
    """
    text = ''.join(char.upper() for char in text if char.isalpha())
    n = len(text)

    if n <= 1:
        return 0

    counter = Counter(text)
    ic = sum(f * (f - 1) for f in counter.values()) / (n * (n - 1))

    return ic


# ================== DEMO CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    plaintext = "HELLO WORLD FROM POLYALPHABETIC CIPHER"

    print("=== POLYALPHABETIC SUBSTITUTION CIPHER DEMO ===")
    print(f"Text gốc: {plaintext}")

    # 1. BEAUFORT CIPHER
    print("\n--- BEAUFORT CIPHER ---")
    beaufort_key = "SECRET"
    beaufort_encrypted = beaufort_encrypt(plaintext, beaufort_key)
    beaufort_decrypted = beaufort_decrypt(beaufort_encrypted, beaufort_key)

    print(f"Key: {beaufort_key}")
    print(f"Mã hóa: {beaufort_encrypted}")
    print(f"Giải mã: {beaufort_decrypted}")

    # 2. AUTOKEY CIPHER
    print("\n--- AUTOKEY CIPHER ---")
    autokey_key = "CRYPTO"
    autokey_encrypted = autokey_encrypt(plaintext, autokey_key)
    autokey_decrypted = autokey_decrypt(autokey_encrypted, autokey_key)

    print(f"Key ban đầu: {autokey_key}")
    print(f"Mã hóa: {autokey_encrypted}")
    print(f"Giải mã: {autokey_decrypted}")

    # 3. RUNNING KEY CIPHER
    print("\n--- RUNNING KEY CIPHER ---")
    running_key = "TO BE OR NOT TO BE THAT IS THE QUESTION WHETHER TIS NOBLER"
    running_encrypted = running_key_encrypt(plaintext, running_key)
    running_decrypted = running_key_decrypt(running_encrypted, running_key)

    print(f"Running key: {running_key[:30]}...")
    print(f"Mã hóa: {running_encrypted}")
    print(f"Giải mã: {running_decrypted}")

    # 4. PERIODIC KEY CIPHER
    print("\n--- PERIODIC KEY CIPHER ---")
    key_pattern = [3, 7, 12, 1, 19]
    periodic_encrypted = periodic_key_encrypt(plaintext, key_pattern)
    periodic_decrypted = periodic_key_decrypt(periodic_encrypted, key_pattern)

    print(f"Key pattern: {key_pattern}")
    print(f"Mã hóa: {periodic_encrypted}")
    print(f"Giải mã: {periodic_decrypted}")

    # 5. FREQUENCY ANALYSIS
    print("\n--- PHÂN TÍCH TẦN SUẤT ---")
    print("Tần suất ký tự trong text gốc:")
    original_freq = analyze_frequency(plaintext)
    for char, freq in list(original_freq.items())[:5]:
        print(f"{char}: {freq:.2f}%")

    print("\nTần suất ký tự trong text đã mã hóa (Beaufort):")
    encrypted_freq = analyze_frequency(beaufort_encrypted)
    for char, freq in list(encrypted_freq.items())[:5]:
        print(f"{char}: {freq:.2f}%")

    # 6. INDEX OF COINCIDENCE
    print("\n--- INDEX OF COINCIDENCE ---")
    ic_original = index_of_coincidence(plaintext)
    ic_encrypted = index_of_coincidence(beaufort_encrypted)

    print(f"IC text gốc: {ic_original:.4f}")
    print(f"IC text mã hóa: {ic_encrypted:.4f}")
    print("IC ≈ 0.065: Tiếng Anh")
    print("IC ≈ 0.038: Text ngẫu nhiên")

    print("\n=== GIẢI THÍCH CHI TIẾT ===")
    print("Polyalphabetic Substitution sử dụng nhiều bảng thay thế:")
    print("1. Beaufort: C = (K - P) mod 26 (tự nghịch đảo)")
    print("2. Autokey: Key mở rộng = key ban đầu + plaintext")
    print("3. Running Key: Sử dụng text dài làm key")
    print("4. Periodic Key: Lặp lại pattern shift values")
    print("\nPhá vỡ frequency analysis của single substitution!")
    print("Nhưng vẫn có thể bị phá bằng Kasiski examination và IC analysis.")
