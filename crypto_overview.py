"""
TỔNG QUAN CÁC THUẬT TOÁN MÃ HÓA
==============================

Đây là file tổng hợp và so sánh các thuật toán mã hóa đã implement,
từ cổ điển đến hiện đại, giúp hiểu rõ sự phát triển của cryptography.

CÁC THUẬT TOÁN ĐÃ IMPLEMENT:
1. Caesar Cipher - Mã hóa dịch chuyển
2. Vigenère Cipher - Mã hóa đa bảng cơ bản  
3. Playfair Cipher - Mã hóa digraph
4. Hill Cipher - Mã hóa ma trận
5. Polyalphabetic - Mã hóa thay thế đa bảng nâng cao
6. Permutation - Mã hóa hoán vị
7. DES - Mã hóa khối hiện đại

PHÂN LOẠI THEO PHƯƠNG PHÁP:
A. SUBSTITUTION CIPHERS (Thay thế):
   - Caesar: Single substitution với shift cố định
   - Vigenère: Polyalphabetic substitution
   - Playfair: Digraph substitution
   - Hill: Block substitution với ma trận
   
B. TRANSPOSITION CIPHERS (Hoán vị):
   - Columnar Transposition
   - Block Transposition
   - Rail Fence
   - Route Cipher
   
C. MODERN BLOCK CIPHERS (Mã hóa khối hiện đại):
   - DES: Feistel network với S-boxes

PHÂN LOẠI THEO THỜI ĐẠI:
• CỔ ĐIỂN (Classical): Caesar, Vigenère, Playfair
• HIỆN ĐẠI SỚM (Early Modern): Hill, Polyalphabetic advanced
• HIỆN ĐẠI (Modern): DES và các thuật toán block cipher

MỨC ĐỘ BẢO MẬT:
1. Rất yếu: Caesar (chỉ 25 khả năng)
2. Yếu: Playfair, simple Vigenère  
3. Trung bình: Hill, advanced Polyalphabetic
4. Mạnh (thời kỳ đó): DES
5. Không an toàn hiện tại: Tất cả trên đều đã lỗi thời!

PHƯƠNG PHÁP PHÂN TÍCH:
• Frequency Analysis: Hiệu quả với substitution đơn giản
• Index of Coincidence: Phát hiện polyalphabetic patterns
• Kasiski Examination: Tìm độ dài key của Vigenère
• Known Plaintext Attack: Hiệu quả với Hill cipher
• Brute Force: Khả thi với Caesar và DES (56-bit key)
"""

import importlib
import sys
import os

# Import các module đã tạo
try:
    from caesar import encrypt_caesar, decrypt_caesar
    from vigenere import encrypt_vigenere, decrypt_vigenere
    from playfair import encrypt_playfair, decrypt_playfair
    from hill import encrypt_hill, decrypt_hill
    from polyalphabetic import beaufort_encrypt, beaufort_decrypt, autokey_encrypt, autokey_decrypt
    from permutation import columnar_transposition_encrypt, columnar_transposition_decrypt
    from des import des_encrypt, des_decrypt
    import numpy as np
except ImportError as e:
    print(f"Warning: Could not import some modules: {e}")
    print("Make sure all cipher files are in the same directory.")


def demonstrate_all_ciphers():
    """
    Demo tất cả các thuật toán mã hóa
    """
    test_text = "HELLO WORLD"

    print("=" * 60)
    print("DEMO TẤT CẢ CÁC THUẬT TOÁN MÃ HÓA")
    print("=" * 60)
    print(f"Text gốc: {test_text}")
    print()

    # 1. CAESAR CIPHER
    print("1. CAESAR CIPHER")
    print("-" * 20)
    try:
        caesar_key = 3
        caesar_encrypted = encrypt_caesar(test_text, caesar_key)
        caesar_decrypted = decrypt_caesar(caesar_encrypted, caesar_key)
        print(f"Key: {caesar_key}")
        print(f"Encrypted: {caesar_encrypted}")
        print(f"Decrypted: {caesar_decrypted}")
        print(
            f"Success: {test_text.replace(' ', '') == caesar_decrypted.replace(' ', '')}")
    except Exception as e:
        print(f"Error: {e}")
    print()

    # 2. VIGENÈRE CIPHER
    print("2. VIGENÈRE CIPHER")
    print("-" * 20)
    try:
        vigenere_key = "SECRET"
        vigenere_encrypted = encrypt_vigenere(test_text, vigenere_key)
        vigenere_decrypted = decrypt_vigenere(vigenere_encrypted, vigenere_key)
        print(f"Key: {vigenere_key}")
        print(f"Encrypted: {vigenere_encrypted}")
        print(f"Decrypted: {vigenere_decrypted}")
    except Exception as e:
        print(f"Error: {e}")
    print()

    # 3. PLAYFAIR CIPHER
    print("3. PLAYFAIR CIPHER")
    print("-" * 20)
    try:
        playfair_key = "MONARCHY"
        playfair_encrypted = encrypt_playfair(test_text, playfair_key)
        playfair_decrypted = decrypt_playfair(playfair_encrypted, playfair_key)
        print(f"Key: {playfair_key}")
        print(f"Encrypted: {playfair_encrypted}")
        print(f"Decrypted: {playfair_decrypted}")
    except Exception as e:
        print(f"Error: {e}")
    print()

    # 4. HILL CIPHER
    print("4. HILL CIPHER")
    print("-" * 20)
    try:
        hill_key = np.array([[3, 2], [5, 7]])
        hill_encrypted = encrypt_hill(test_text, hill_key)
        hill_decrypted = decrypt_hill(hill_encrypted, hill_key)
        print(f"Key Matrix:\n{hill_key}")
        print(f"Encrypted: {hill_encrypted}")
        print(f"Decrypted: {hill_decrypted}")
    except Exception as e:
        print(f"Error: {e}")
    print()

    # 5. BEAUFORT CIPHER
    print("5. BEAUFORT CIPHER")
    print("-" * 20)
    try:
        beaufort_key = "CRYPTO"
        beaufort_encrypted = beaufort_encrypt(test_text, beaufort_key)
        beaufort_decrypted = beaufort_decrypt(beaufort_encrypted, beaufort_key)
        print(f"Key: {beaufort_key}")
        print(f"Encrypted: {beaufort_encrypted}")
        print(f"Decrypted: {beaufort_decrypted}")
    except Exception as e:
        print(f"Error: {e}")
    print()

    # 6. COLUMNAR TRANSPOSITION
    print("6. COLUMNAR TRANSPOSITION")
    print("-" * 30)
    try:
        col_key = "ZEBRA"
        col_encrypted = columnar_transposition_encrypt(test_text, col_key)
        col_decrypted = columnar_transposition_decrypt(col_encrypted, col_key)
        print(f"Key: {col_key}")
        print(f"Encrypted: {col_encrypted}")
        print(f"Decrypted: {col_decrypted}")
    except Exception as e:
        print(f"Error: {e}")
    print()

    # 7. DES CIPHER
    print("7. DES CIPHER")
    print("-" * 15)
    try:
        des_text = "HELLO123"  # DES cần 8 ký tự
        des_key = "MYKEY123"
        des_encrypted = des_encrypt(des_text, des_key)
        des_decrypted = des_decrypt(des_encrypted, des_key)
        print(f"Text: {des_text}")
        print(f"Key: {des_key}")
        print(f"Encrypted (hex): {des_encrypted.hex()}")
        print(f"Decrypted: {des_decrypted}")
        print(f"Success: {des_text == des_decrypted}")
    except Exception as e:
        print(f"Error: {e}")


def compare_security_levels():
    """
    So sánh mức độ bảo mật của các thuật toán
    """
    print("\n" + "=" * 60)
    print("SO SÁNH MỨC ĐỘ BẢO MẬT")
    print("=" * 60)

    security_comparison = [
        ("Caesar Cipher", "Rất thấp", "25 khả năng, frequency analysis"),
        ("Vigenère Cipher", "Thấp-Trung bình", "Kasiski examination, IC analysis"),
        ("Playfair Cipher", "Thấp-Trung bình", "Digraph frequency analysis"),
        ("Hill Cipher", "Trung bình", "Known plaintext attack"),
        ("Polyalphabetic", "Trung bình", "Phức tạp hơn nhưng vẫn có pattern"),
        ("Permutation", "Thấp-Trung bình", "Anagram analysis, pattern recognition"),
        ("DES", "Cao (thời kỳ đó)", "56-bit key đã không còn an toàn")
    ]

    print(f"{'Thuật toán':<20} {'Bảo mật':<15} {'Điểm yếu chính'}")
    print("-" * 70)
    for name, security, weakness in security_comparison:
        print(f"{name:<20} {security:<15} {weakness}")


def analyze_cipher_properties():
    """
    Phân tích đặc tính của các loại cipher
    """
    print("\n" + "=" * 60)
    print("PHÂN TÍCH ĐẶC TÍNH CÁC LOẠI CIPHER")
    print("=" * 60)

    print("SUBSTITUTION CIPHERS:")
    print("• Thay thế ký tự/nhóm ký tự")
    print("• Giữ nguyên vị trí, thay đổi giá trị")
    print("• Dễ bị frequency analysis nếu đơn giản")
    print("• Ví dụ: Caesar, Vigenère, Playfair, Hill")

    print("\nTRANSPOSITION CIPHERS:")
    print("• Thay đổi vị trí ký tự")
    print("• Giữ nguyên giá trị, thay đổi thứ tự")
    print("• Frequency analysis không hiệu quả")
    print("• Dễ bị anagram analysis")
    print("• Ví dụ: Columnar, Rail Fence, Route")

    print("\nMODERN BLOCK CIPHERS:")
    print("• Kết hợp substitution và permutation")
    print("• Mã hóa theo khối cố định")
    print("• Sử dụng nhiều rounds")
    print("• Cơ sở toán học vững chắc")
    print("• Ví dụ: DES, AES")


def historical_timeline():
    """
    Timeline lịch sử phát triển cryptography
    """
    print("\n" + "=" * 60)
    print("TIMELINE LỊCH SỬ CRYPTOGRAPHY")
    print("=" * 60)

    timeline = [
        ("~50 BC", "Caesar Cipher", "Julius Caesar sử dụng shift cipher"),
        ("1467", "Polyalphabetic", "Johannes Trithemius - tabula recta"),
        ("1553", "Vigenère Cipher", "Giovan Battista Bellaso, Blaise de Vigenère"),
        ("1854", "Playfair Cipher", "Charles Wheatstone phát minh"),
        ("1929", "Hill Cipher", "Lester S. Hill - mã hóa đại số tuyến tính"),
        ("1976", "DES", "IBM phát triển, NIST chấp nhận"),
        ("2001", "AES", "Thay thế DES (không implement ở đây)"),
        ("Hiện tại", "Post-quantum", "Chuẩn bị cho thời đại quantum computing")
    ]

    for year, cipher, description in timeline:
        print(f"{year:<12} {cipher:<20} {description}")


def practical_recommendations():
    """
    Khuyến nghị thực tế về sử dụng mã hóa
    """
    print("\n" + "=" * 60)
    print("KHUYẾN NGHỊ THỰC TẾ")
    print("=" * 60)

    print("❌ KHÔNG NÊN SỬ DỤNG CHO BẢO MẬT THỰC TẾ:")
    print("• Tất cả các thuật toán classical cipher")
    print("• DES (key quá ngắn)")
    print("• Bất kỳ thuật toán tự implement nào")

    print("\n✅ NÊN SỬ DỤNG HIỆN TẠI:")
    print("• AES (Advanced Encryption Standard)")
    print("• ChaCha20-Poly1305")
    print("• Các library crypto chuẩn (OpenSSL, NaCl, etc.)")

    print("\n🎓 GIÁ TRỊ GIÁO DỤC:")
    print("• Hiểu nguyên lý cơ bản của cryptography")
    print("• Học cách phân tích và tấn công cipher")
    print("• Nền tảng để hiểu các thuật toán hiện đại")
    print("• Training tư duy về bảo mật thông tin")

    print("\n⚠️  CẢNH BÁO BẢO MẬT:")
    print("• Không tự implement crypto cho production")
    print("• Luôn sử dụng library đã được kiểm tra")
    print("• Crypto chỉ là một phần của bảo mật tổng thể")
    print("• Key management quan trọng hơn thuật toán")


def main():
    """
    Hàm main chạy demo tổng hợp
    """
    print("CHƯƠNG TRÌNH DEMO TỔNG HỢP CÁC THUẬT TOÁN MÃ HÓA")
    print("Phát triển bởi: [Tên của bạn]")
    print("Mục đích: Giáo dục và nghiên cứu")
    print()

    # Demo tất cả các cipher
    demonstrate_all_ciphers()

    # So sánh bảo mật
    compare_security_levels()

    # Phân tích đặc tính
    analyze_cipher_properties()

    # Timeline lịch sử
    historical_timeline()

    # Khuyến nghị thực tế
    practical_recommendations()

    print("\n" + "=" * 60)
    print("KẾT LUẬN")
    print("=" * 60)
    print("Cryptography đã trải qua hành trình dài từ những phương pháp")
    print("đơn giản như Caesar Cipher đến các thuật toán phức tạp như AES.")
    print("Mỗi thuật toán đều có vai trò lịch sử và giá trị giáo dục riêng.")
    print()
    print("Hãy nhớ: Bảo mật không chỉ là mã hóa, mà là toàn bộ hệ thống!")
    print("Cảm ơn bạn đã tìm hiểu về thế giới fascinating của cryptography!")


if __name__ == "__main__":
    main()
