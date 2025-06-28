"""
Dictionary Attack trên DES
========================

Mô phỏng tấn công từ điển đơn giản trên hệ thống DES
Bài tập thực hành Cybersecurity - Data Privacy
"""

from des import encrypt_des, decrypt_des
import time
import string


def create_simple_dictionary():
    """Tạo từ điển đơn giản với các key phổ biến"""
    dictionary = [
        "PASSWORD", "12345678", "ABCDEFGH", "MYKEY123",
        "SECRETKEY", "TESTKEY1", "WELCOME1", "ADMIN123",
        "USER1234", "HELLO123", "COMPUTER", "SECURITY",
        "QWERTYUI", "ASDFGHJK", "ZXCVBNM1", "FOOTBALL"
    ]

    # Thêm một số pattern đơn giản
    for i in range(1, 101):
        dictionary.append(f"KEY{i:05d}")

    # Thêm các từ phổ biến
    common_words = ["LOVE", "HATE", "GOOD", "BEST", "HOME", "WORK"]
    for word in common_words:
        dictionary.append(word + "1234")
        dictionary.append(word + "PASS")

    return dictionary


def is_valid_plaintext(text):
    """Kiểm tra xem plaintext có hợp lý không"""
    if not text or len(text) == 0:
        return False

    # Kiểm tra có ít nhất 50% ký tự printable
    try:
        printable_count = sum(1 for c in text if c in string.printable)
        if printable_count / len(text) < 0.5:
            return False
    except:
        return False

    # Kiểm tra không có quá nhiều ký tự null
    null_count = text.count('\x00')
    if null_count > len(text) // 2:
        return False

    # Kiểm tra không có quá nhiều ký tự điều khiển
    control_count = sum(1 for c in text if ord(c) < 32 and c not in '\n\r\t')
    if control_count > len(text) // 4:
        return False

    return True


def dictionary_attack(ciphertext, max_attempts=None):
    """
    Thực hiện dictionary attack

    Args:
        ciphertext (str): Hex string cần crack
        max_attempts (int): Số lần thử tối đa

    Returns:
        tuple: (found_key, plaintext, attempts)
    """
    dictionary = create_simple_dictionary()

    if max_attempts:
        dictionary = dictionary[:max_attempts]

    print(f"🔍 Bắt đầu dictionary attack với {len(dictionary)} keys...")
    print(
        f"📝 Ciphertext: {ciphertext[:50]}{'...' if len(ciphertext) > 50 else ''}")
    print(f"⏱️  Thời gian bắt đầu: {time.strftime('%H:%M:%S')}")

    start_time = time.time()

    for i, key in enumerate(dictionary):
        try:
            # Thử giải mã với key hiện tại
            plaintext = decrypt_des(ciphertext, key)

            # Kiểm tra tính hợp lý của plaintext
            if is_valid_plaintext(plaintext):
                end_time = time.time()
                print(f"\n✅ THÀNH CÔNG!")
                print(f"🔑 Key tìm được: '{key}'")
                print(f"📄 Plaintext: '{plaintext}'")
                print(f"🔢 Số lần thử: {i + 1}")
                print(f"⏱️  Thời gian: {end_time - start_time:.2f} giây")
                return key, plaintext, i + 1

            # In progress mỗi 20 lần thử
            if (i + 1) % 20 == 0:
                elapsed = time.time() - start_time
                rate = (i + 1) / elapsed if elapsed > 0 else 0
                print(f"⏳ Đã thử {i + 1} keys ({rate:.1f} keys/sec)...")

        except Exception as e:
            # Bỏ qua lỗi và tiếp tục
            continue

    end_time = time.time()
    print(f"\n❌ THẤT BẠI!")
    print(f"🔢 Đã thử {len(dictionary)} keys")
    print(f"⏱️  Thời gian: {end_time - start_time:.2f} giây")
    return None, None, len(dictionary)


def demonstrate_attack_scenarios():
    """Demo các tình huống tấn công khác nhau"""

    scenarios = [
        {
            "name": "Weak Password",
            "plaintext": "SECRET MESSAGE",
            "key": "PASSWORD",
            "description": "Key dễ đoán trong từ điển"
        },
        {
            "name": "Numeric Pattern",
            "plaintext": "CONFIDENTIAL DATA",
            "key": "12345678",
            "description": "Key số tuần tự"
        },
        {
            "name": "Common Word",
            "plaintext": "TOP SECRET INFO",
            "key": "COMPUTER",
            "description": "Key từ phổ biến"
        }
    ]

    print("🎯 DEMO CÁC TÌNH HUỐNG TẤN CÔNG")
    print("="*60)

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n🔍 SCENARIO {i}: {scenario['name']}")
        print(f"📝 Description: {scenario['description']}")
        print(f"🎯 Target plaintext: '{scenario['plaintext']}'")
        print(f"🔑 Actual key: '{scenario['key']}'")

        # Mã hóa
        ciphertext = encrypt_des(scenario['plaintext'], scenario['key'])
        print(f"🔒 Ciphertext: {ciphertext[:50]}...")

        print(f"\n🚀 Bắt đầu attack...")
        print("-" * 40)

        # Thực hiện tấn công với giới hạn
        found_key, found_plaintext, attempts = dictionary_attack(
            ciphertext, max_attempts=50)

        if found_key:
            print(f"🎉 Attack thành công cho scenario {i}!")
            print(f"✅ Key dự đoán: '{found_key}'")
            print(f"✅ Key thực tế: '{scenario['key']}'")
            print(f"✅ Khớp: {scenario['key'] == found_key}")
        else:
            print(f"💔 Attack thất bại cho scenario {i}")
            print(f"ℹ️  Key có thể không có trong từ điển hiện tại")

        print("="*60)


# ================== MAIN DEMO ==================
if __name__ == "__main__":
    print("="*70)
    print("🔐 DEMO TẤN CÔNG TỪ ĐIỂN TRÊN DES")
    print("📚 Bài tập thực hành Cybersecurity - Data Privacy")
    print("="*70)

    # Demo cơ bản
    print("\n🎬 DEMO CƠ BẢN")
    print("="*40)

    original_plaintext = "HELLO WORLD MESSAGE"
    correct_key = "MYKEY123"

    print(f"🎯 Target plaintext: '{original_plaintext}'")
    print(f"🔑 Correct key: '{correct_key}'")

    # Mã hóa
    ciphertext = encrypt_des(original_plaintext, correct_key)
    print(f"🔒 Ciphertext: {ciphertext}")

    print("\n" + "="*50)

    # Thực hiện tấn công
    found_key, found_plaintext, attempts = dictionary_attack(
        ciphertext, max_attempts=30)

    if found_key:
        print(f"\n🎉 BASIC ATTACK THÀNH CÔNG!")
        print(f"✅ Key ban đầu: '{correct_key}'")
        print(f"✅ Key tìm được: '{found_key}'")
        print(f"✅ Khớp: {correct_key == found_key}")
    else:
        print(f"\n💔 BASIC ATTACK THẤT BẠI!")
        print(
            f"ℹ️  Key '{correct_key}' có thể không có trong 30 keys đầu của từ điển")

    # Demo nhiều tình huống
    print("\n\n")
    demonstrate_attack_scenarios()

    # Kết luận
    print(f"\n📋 KẾT LUẬN:")
    print(f"⚠️  DES với weak keys rất dễ bị tấn công từ điển")
    print(f"🔒 Luôn sử dụng strong, random keys")
    print(f"🚫 Không sử dụng DES trong production (chỉ học tập)")
    print(f"✅ Sử dụng AES-256 cho ứng dụng thực tế")

    print(f"\n💡 TIPS:")
    print(f"   • Key nên dài, random và không có trong từ điển")
    print(f"   • Sử dụng key derivation functions (PBKDF2, scrypt)")
    print(f"   • Kết hợp với salt để chống rainbow tables")
    print(f"   • Luôn dùng authenticated encryption (AES-GCM)")
