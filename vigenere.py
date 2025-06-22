"""
VIGENÈRE CIPHER - THUẬT TOÁN MÃ HÓA POLYALPHABETIC
==================================================

Vigenère Cipher là một thuật toán mã hóa cổ điển được phát triển bởi Blaise de Vigenère.
Đây là một dạng Caesar Cipher cải tiến, sử dụng nhiều Caesar Cipher khác nhau trong một message.

NGUYÊN LÝ HOẠT ĐỘNG:
- Sử dụng một từ khóa (key) để mã hóa
- Mỗi ký tự trong text được mã hóa bằng một ký tự khác nhau trong key
- Key được lặp lại cho đến khi có độ dài bằng text cần mã hóa

VÍ DỤ:
Text: "HELLO"
Key:  "KEY"
Key lặp lại: "KEYKE"
Mã hóa từng cặp: H+K, E+E, L+Y, L+K, O+E

CÔNG THỨC TOÁN HỌC:
- Mã hóa: E(i) = (M(i) + K(i)) mod 26
- Giải mã: D(i) = (E(i) - K(i) + 26) mod 26
Trong đó: M = message, K = key, E = encrypted text

ĐIỂM MẠNH:
- An toàn hơn Caesar Cipher đơn giản
- Khó phá vỡ bằng frequency analysis

ĐIỂM YẾU:
- Vẫn có thể bị phá vỡ bằng Kasiski examination
- Không an toàn với các thuật toán mã hóa hiện đại
"""


def generate_key(msg, key):
    """
    Hàm tạo khóa có độ dài bằng với message
    - Nếu khóa ngắn hơn message, sẽ lặp lại khóa để có độ dài bằng message
    - Ví dụ: msg="HELLO", key="KEY" -> key_generated="KEYKE"
    """
    key = list(key)  # Chuyển key thành list để dễ thao tác

    # Nếu độ dài message và key bằng nhau thì trả về key
    if len(msg) == len(key):
        return key
    else:
        # Lặp lại key cho đến khi đủ độ dài với message
        for i in range(len(msg) - len(key)):
            # Sử dụng phép chia lấy dư để lặp lại
            key.append(key[i % len(key)])
    return "".join(key)  # Chuyển list về string


def encrypt_vigenere(msg, key):
    """
    Hàm mã hóa text bằng thuật toán Vigenère Cipher
    - Thuật toán: (char + key_char) mod 26
    - Hỗ trợ cả chữ hoa, chữ thường và ký tự đặc biệt
    """
    encrypted_text = []
    key = generate_key(msg, key)  # Tạo key có độ dài bằng message

    for i in range(len(msg)):
        char = msg[i]

        # Xử lý chữ cái viết hoa (A-Z)
        if char.isupper():
            # Công thức mã hóa: (ord(char) - ord('A') + ord(key[i]) - ord('A')) % 26 + ord('A')
            # Đơn giản hóa: ord(char) + ord(key[i]) - 2*ord('A')
            encrypted_char = chr(
                (ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))

        # Xử lý chữ cái viết thường (a-z)
        elif char.islower():
            # Tương tự như chữ hoa nhưng dùng 'a' làm base
            encrypted_char = chr(
                (ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))

        # Giữ nguyên ký tự đặc biệt (khoảng trắng, dấu câu, số...)
        else:
            encrypted_char = char

        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)


def decrypt_vigenere(msg, key):
    """
    Hàm giải mã text đã được mã hóa bằng Vigenère Cipher
    - Thuật toán: (encrypted_char - key_char + 26) mod 26
    - Cộng 26 để tránh số âm khi thực hiện phép trừ
    """
    decrypted_text = []
    key = generate_key(msg, key)  # Tạo key có độ dài bằng message

    for i in range(len(msg)):
        char = msg[i]

        # Xử lý chữ cái viết hoa (A-Z)
        if char.isupper():
            # Công thức giải mã: (ord(char) - ord('A') - (ord(key[i]) - ord('A')) + 26) % 26 + ord('A')
            # Đơn giản hóa: (ord(char) - ord(key[i]) + 26) % 26 + ord('A')
            decrypted_char = chr(
                (ord(char) - ord(key[i]) + 26) % 26 + ord('A'))

        # Xử lý chữ cái viết thường (a-z)
        elif char.islower():
            # Tương tự như chữ hoa nhưng dùng 'a' làm base
            decrypted_char = chr(
                (ord(char) - ord(key[i]) + 26) % 26 + ord('a'))

        # Giữ nguyên ký tự đặc biệt (không thay đổi)
        else:
            decrypted_char = char

        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

# ================== DEMO CHƯƠNG TRÌNH ==================
# Ví dụ sử dụng Vigenère Cipher


# Text cần mã hóa
text_to_encrypt = "Hello, World!"
# Khóa mã hóa (sẽ được lặp lại để có độ dài bằng text)
key = "KEY"

print("=== VIGENÈRE CIPHER DEMO ===")
print(f"Text gốc: {text_to_encrypt}")
print(f"Khóa: {key}")
print(f"Khóa sau khi generate: {generate_key(text_to_encrypt, key)}")

# Thực hiện mã hóa
encrypted_text = encrypt_vigenere(text_to_encrypt, key)
print(f"Text đã mã hóa: {encrypted_text}")

# Thực hiện giải mã
decrypted_text = decrypt_vigenere(encrypted_text, key)
print(f"Text đã giải mã: {decrypted_text}")

# Kiểm tra tính đúng đắn
print(f"Giải mã thành công: {text_to_encrypt == decrypted_text}")

print("\n=== GIẢI THÍCH THUẬT TOÁN ===")
print("Vigenère Cipher là thuật toán mã hóa sử dụng nhiều Caesar Cipher")
print("- Mỗi ký tự trong text được mã hóa với một ký tự khác nhau trong key")
print("- Key được lặp lại cho đến khi có độ dài bằng text cần mã hóa")
print("- Công thức mã hóa: (char + key_char) mod 26")
print("- Công thức giải mã: (encrypted_char - key_char + 26) mod 26")
print("- Code này hỗ trợ cả chữ hoa, chữ thường và giữ nguyên ký tự đặc biệt")
