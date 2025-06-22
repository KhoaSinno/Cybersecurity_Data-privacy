"""
PLAYFAIR CIPHER - THUẬT TOÁN MÃ HÓA CỔ ĐIỂN
==========================================

Playfair Cipher được phát minh bởi Charles Wheatstone năm 1854 và được Lord Playfair
quảng bá. Đây là thuật toán mã hóa digraph (mã hóa cặp ký tự) đầu tiên.

NGUYÊN LÝ HOẠT ĐỘNG:
- Sử dụng ma trận 5x5 chứa 25 chữ cái (I và J được coi là một)
- Mã hóa theo cặp ký tự (digraph)
- Áp dụng 3 quy tắc mã hóa dựa trên vị trí cặp ký tự trong ma trận

QUY TẮC MÃ HÓA:
1. Cùng hàng: Dịch chuyển sang phải (wrap around)
2. Cùng cột: Dịch chuyển xuống dưới (wrap around)  
3. Khác hàng khác cột: Tạo hình chữ nhật, hoán đổi cột

VÍ DỤ MA TRẬN (key="MONARCHY"):
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z

ĐIỂM MẠNH:
- An toàn hơn Caesar và substitution cipher đơn giản
- Frequency analysis khó khăn hơn do mã hóa theo cặp

ĐIỂM YẾU:
- Vẫn có thể bị phá vỡ bằng frequency analysis của digraph
- Ma trận 5x5 giới hạn độ phức tạp
"""


def create_playfair_matrix(key):
    """
    Tạo ma trận 5x5 Playfair từ key

    Args:
        key (str): Từ khóa để tạo ma trận

    Returns:
        list: Ma trận 5x5 dạng list of lists
        dict: Dictionary mapping ký tự -> (row, col)
    """
    # Loại bỏ ký tự trùng lặp và chuyển về chữ hoa
    key = key.upper().replace('J', 'I')  # J được thay bằng I
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Không có J

    # Tạo chuỗi không trùng lặp từ key + alphabet
    used_chars = set()
    matrix_string = ""

    # Thêm ký tự từ key trước
    for char in key:
        if char.isalpha() and char not in used_chars:
            matrix_string += char
            used_chars.add(char)

    # Thêm các ký tự còn lại từ alphabet
    for char in alphabet:
        if char not in used_chars:
            matrix_string += char
            used_chars.add(char)

    # Tạo ma trận 5x5
    matrix = []
    char_positions = {}

    for i in range(5):
        row = []
        for j in range(5):
            char = matrix_string[i * 5 + j]
            row.append(char)
            char_positions[char] = (i, j)
        matrix.append(row)

    return matrix, char_positions


def prepare_text(text):
    """
    Chuẩn bị text cho mã hóa Playfair

    Args:
        text (str): Text gốc

    Returns:
        str: Text đã được chuẩn bị (digraph)

    Quy tắc chuẩn bị:
    1. Chuyển về chữ hoa, loại bỏ ký tự không phải chữ cái
    2. Thay J bằng I
    3. Thêm 'X' giữa các cặp ký tự giống nhau
    4. Thêm 'X' ở cuối nếu độ dài lẻ
    """
    # Loại bỏ ký tự không phải chữ cái và chuyển về chữ hoa
    text = ''.join(char.upper() for char in text if char.isalpha())
    text = text.replace('J', 'I')

    # Xử lý các cặp ký tự giống nhau
    processed = ""
    i = 0
    while i < len(text):
        processed += text[i]

        # Nếu không phải ký tự cuối và ký tự tiếp theo giống nhau
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed += 'X'  # Thêm X để tách
            i += 1
        elif i + 1 < len(text):
            processed += text[i + 1]
            i += 2
        else:
            i += 1

    # Thêm X nếu độ dài lẻ
    if len(processed) % 2 == 1:
        processed += 'X'

    return processed


def encrypt_playfair(text, key):
    """
    Mã hóa text bằng Playfair Cipher

    Args:
        text (str): Text cần mã hóa
        key (str): Key để tạo ma trận

    Returns:
        str: Text đã mã hóa
    """
    matrix, positions = create_playfair_matrix(key)
    text = prepare_text(text)

    encrypted = ""

    # Mã hóa từng cặp ký tự
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = positions[char1]
        row2, col2 = positions[char2]

        # QUY TẮC 1: Cùng hàng - dịch chuyển sang phải
        if row1 == row2:
            new_col1 = (col1 + 1) % 5
            new_col2 = (col2 + 1) % 5
            encrypted += matrix[row1][new_col1] + matrix[row2][new_col2]

        # QUY TẮC 2: Cùng cột - dịch chuyển xuống dưới
        elif col1 == col2:
            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5
            encrypted += matrix[new_row1][col1] + matrix[new_row2][col2]

        # QUY TẮC 3: Khác hàng khác cột - tạo hình chữ nhật
        else:
            encrypted += matrix[row1][col2] + matrix[row2][col1]

    return encrypted


def decrypt_playfair(text, key):
    """
    Giải mã text đã được mã hóa bằng Playfair Cipher

    Args:
        text (str): Text đã mã hóa
        key (str): Key đã dùng để mã hóa

    Returns:
        str: Text gốc đã giải mã
    """
    matrix, positions = create_playfair_matrix(key)

    decrypted = ""

    # Giải mã từng cặp ký tự
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = positions[char1]
        row2, col2 = positions[char2]

        # QUY TẮC 1: Cùng hàng - dịch chuyển sang trái
        if row1 == row2:
            new_col1 = (col1 - 1) % 5
            new_col2 = (col2 - 1) % 5
            decrypted += matrix[row1][new_col1] + matrix[row2][new_col2]

        # QUY TẮC 2: Cùng cột - dịch chuyển lên trên
        elif col1 == col2:
            new_row1 = (row1 - 1) % 5
            new_row2 = (row2 - 1) % 5
            decrypted += matrix[new_row1][col1] + matrix[new_row2][col2]

        # QUY TẮC 3: Khác hàng khác cột - tạo hình chữ nhật
        else:
            decrypted += matrix[row1][col2] + matrix[row2][col1]

    return decrypted


def print_matrix(matrix):
    """In ma trận Playfair"""
    print("Ma trận Playfair 5x5:")
    for row in matrix:
        print(" ".join(row))


# ================== DEMO CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    # Text và key demo
    plaintext = "HELLO WORLD"
    key = "MONARCHY"

    print("=== PLAYFAIR CIPHER DEMO ===")
    print(f"Text gốc: {plaintext}")
    print(f"Key: {key}")

    # Tạo và hiển thị ma trận
    matrix, positions = create_playfair_matrix(key)
    print_matrix(matrix)

    # Chuẩn bị text
    prepared_text = prepare_text(plaintext)
    print(f"Text đã chuẩn bị: {prepared_text}")

    # Mã hóa
    encrypted = encrypt_playfair(plaintext, key)
    print(f"Text đã mã hóa: {encrypted}")

    # Giải mã
    decrypted = decrypt_playfair(encrypted, key)
    print(f"Text đã giải mã: {decrypted}")

    print("\n=== GIẢI THÍCH CHI TIẾT ===")
    print("Playfair Cipher hoạt động theo 3 quy tắc:")
    print("1. Cùng hàng: Dịch chuyển sang phải")
    print("2. Cùng cột: Dịch chuyển xuống dưới")
    print("3. Khác hàng khác cột: Hoán đổi cột (tạo hình chữ nhật)")
    print("\nĐây là thuật toán mã hóa theo cặp ký tự (digraph)")
    print("An toàn hơn Caesar nhưng vẫn có thể bị phá vỡ bằng phân tích tần suất digraph")
