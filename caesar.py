"""
CAESAR CIPHER - THUẬT TOÁN MÃ HÓA CỔ ĐIỂN
=========================================

Caesar Cipher là một trong những thuật toán mã hóa cổ điển và đơn giản nhất,
được đặt tên theo hoàng đế La Mã Julius Caesar, người đã sử dụng nó để bảo mật
thông tin liên lạc quân sự.

NGUYÊN LÝ HOẠT ĐỘNG:
- Dịch chuyển mỗi ký tự trong bảng chữ cái một số vị trí cố định (shift/key)
- Ví dụ: với shift = 3, A → D, B → E, C → F, ..., X → A, Y → B, Z → C

CÔNG THỨC TOÁN HỌC:
- Mã hóa: E(x) = (x + k) mod 26
- Giải mã: D(x) = (x - k) mod 26
Trong đó: x = vị trí ký tự (A=0, B=1, ..., Z=25), k = shift value

VÍ DỤ:
Text: "HELLO"
Shift: 3
Mã hóa: H→K, E→H, L→O, L→O, O→R
Kết quả: "KHOOR"

ĐIỂM MẠNH:
- Đơn giản, dễ hiểu và thực hiện
- Phù hợp cho mục đích giáo dục

ĐIỂM YẾU:
- Rất dễ bị phá vỡ (chỉ có 25 khả năng shift)
- Dễ bị tấn công bằng frequency analysis
- Không an toàn cho mục đích thực tế
"""


def encrypt_caesar(msg, k):
    """
    Hàm mã hóa Caesar Cipher

    Args:
        msg (str): Văn bản cần mã hóa
        k (int): Số bước dịch chuyển (shift value)

    Returns:
        str: Văn bản đã được mã hóa

    Cách hoạt động:
        - Duyệt qua từng ký tự trong message
        - Dịch chuyển mỗi chữ cái đi k vị trí trong bảng chữ cái
        - Giữ nguyên ký tự không phải chữ cái (số, dấu câu, khoảng trắng)
    """
    arr = []  # Mảng chứa kết quả mã hóa

    # Chuẩn hóa k về phạm vi 0-25 (vì bảng chữ cái có 26 ký tự)
    # Ví dụ: k=29 -> k=3 (vì 29%26=3)
    if k > 26:
        k = k % 26

    # Duyệt qua từng ký tự trong message
    for char in msg:
        # Kiểm tra nếu ký tự không phải chữ cái (số, dấu câu, khoảng trắng...)
        if not char.isalpha():
            arr.append(char)  # Giữ nguyên ký tự đặc biệt
            continue

        # Xác định ký tự cơ sở (base character)
        # ord('A') = 65 cho chữ hoa, ord('a') = 97 cho chữ thường
        base = ord('A') if char.isupper() else ord('a')

        # CÔNG THỨC MÃ HÓA CAESAR:
        # 1. ord(char) - base: Chuyển ký tự về số từ 0-25 (A=0, B=1, ..., Z=25)
        # 2. + k: Dịch chuyển k vị trí
        # 3. % 26: Đảm bảo kết quả trong phạm vi 0-25 (wrap around)
        # 4. + base: Chuyển lại về ký tự ASCII
        # Ví dụ: H (72) với shift=3 -> (72-65+3)%26+65 = (7+3)%26+65 = 10+65 = 75 = K
        echar = chr((ord(char) + k - base) % 26 + base)
        arr.append(echar)

    return ''.join(arr)  # Nối tất cả ký tự thành chuỗi


def decrypt_caesar(msg, k):
    """
    Hàm giải mã Caesar Cipher

    Args:
        msg (str): Văn bản đã được mã hóa
        k (int): Số bước dịch chuyển (shift value) đã dùng để mã hóa

    Returns:
        str: Văn bản gốc đã được giải mã

    Cách hoạt động:
        - Tương tự như mã hóa nhưng dịch chuyển ngược lại (trừ k thay vì cộng k)
        - Cộng 26 để tránh số âm khi thực hiện phép trừ
    """
    arr = []  # Mảng chứa kết quả giải mã

    # Chuẩn hóa k về phạm vi 0-25
    if k > 26:
        k = k % 26

    # Duyệt qua từng ký tự trong message đã mã hóa
    for char in msg:
        # Kiểm tra nếu ký tự không phải chữ cái
        if not char.isalpha():
            arr.append(char)  # Giữ nguyên ký tự đặc biệt
            continue

        # Xác định ký tự cơ sở
        base = ord('A') if char.isupper() else ord('a')

        # CÔNG THỨC GIẢI MÃ CAESAR:
        # 1. ord(char) - base: Chuyển ký tự về số từ 0-25
        # 2. - k: Dịch chuyển ngược lại k vị trí
        # 3. + 26: Cộng 26 để tránh số âm (vì có thể có trường hợp char_value < k)
        # 4. % 26: Đảm bảo kết quả trong phạm vi 0-25
        # 5. + base: Chuyển lại về ký tự ASCII
        # Ví dụ: K (75) với shift=3 -> (75-65-3+26)%26+65 = (10-3+26)%26+65 = 33%26+65 = 7+65 = 72 = H
        dchar = chr((ord(char) - k - base + 26) % 26 + base)
        arr.append(dchar)

    return ''.join(arr)  # Nối tất cả ký tự thành chuỗi


# ================== DEMO CHƯƠNG TRÌNH ==================
# Ví dụ sử dụng Caesar Cipher

# Text cần mã hóa
text_to_encrypt = "Hello, World!"
# Số bước dịch chuyển (shift value)
shift = 3

print("=== CAESAR CIPHER DEMO ===")
print(f"Text gốc: {text_to_encrypt}")
print(f"Shift value: {shift}")

# Thực hiện mã hóa
encrypted_text = encrypt_caesar(text_to_encrypt, shift)
print(f"Text đã mã hóa: {encrypted_text}")

# Thực hiện giải mã
decrypted_text = decrypt_caesar(encrypted_text, shift)
print(f"Text đã giải mã: {decrypted_text}")

# Kiểm tra tính đúng đắn
print(f"Giải mã thành công: {text_to_encrypt == decrypted_text}")

print("\n=== GIẢI THÍCH CHI TIẾT ===")
print("Cách hoạt động của Caesar Cipher:")
print("1. Chuyển đổi ký tự thành số (A=0, B=1, ..., Z=25)")
print("2. Cộng/trừ shift value")
print("3. Sử dụng modulo 26 để wrap around (Z+1 = A)")
print("4. Chuyển số trở lại thành ký tự")

print("\n=== VÍ DỤ TỪNG BƯỚC ===")
# Demo chi tiết cho ký tự đầu tiên
first_char = text_to_encrypt[0]
print(f"Mã hóa ký tự '{first_char}':")
print(f"1. ord('{first_char}') = {ord(first_char)}")
print(f"2. {ord(first_char)} - {ord('A')} = {ord(first_char) - ord('A')} (chuyển về 0-25)")
print(f"3. ({ord(first_char) - ord('A')} + {shift}) % 26 = {(ord(first_char) - ord('A') + shift) % 26}")
print(f"4. {(ord(first_char) - ord('A') + shift) % 26} + {ord('A')} = {(ord(first_char) - ord('A') + shift) % 26 + ord('A')}")
print(f"5. chr({(ord(first_char) - ord('A') + shift) % 26 + ord('A')}) = '{chr((ord(first_char) - ord('A') + shift) % 26 + ord('A'))}'")

print("\n=== BẢO MẬT ===")
print("Caesar Cipher rất dễ bị phá vỡ vì:")
print("- Chỉ có 25 khả năng shift (brute force dễ dàng)")
print("- Frequency analysis có thể phá vỡ nhanh chóng")
print("- Không phù hợp cho mục đích bảo mật thực tế")
