# des_demo.py - DES Implementation Demo
def string_to_bits(text):
    """Chuyển string thành binary"""
    return ''.join(format(ord(char), '08b') for char in text)


def permute(bits, table):
    """Áp dụng permutation table"""
    return ''.join(bits[i-1] for i in table)


def left_shift(bits, shifts):
    """Dịch trái vòng tròn"""
    return bits[shifts:] + bits[:shifts]


def xor(bits1, bits2):
    """XOR hai chuỗi bit"""
    return ''.join('0' if a == b else '1' for a, b in zip(bits1, bits2))


# Bảng permutation chính
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,  59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# S-Box 1 (mẫu - đúng theo chuẩn DES)
S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

# S-Box 2 (thêm để demo đầy đủ)
S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


def s_box_substitute(group, s_box):
    """Thực hiện S-Box substitution cho 1 group 6-bit"""
    row = int(group[0] + group[5], 2)  # bit đầu + cuối
    col = int(group[1:5], 2)  # 4 bit giữa
    return format(s_box[row][col], '04b')


def des_demo():
    """Demo DES với HELLO123 và MYSECRET"""

    print("=" * 60)
    print("            DES STEP-BY-STEP DEMO")
    print("=" * 60)
    print()

    # Input
    plaintext = "HELLO123"
    key = "MYSECRET"
    print(f"📝 INPUT:")
    print(f"Plaintext: {plaintext}")
    print(f"Key:       {key}")
    print()

    # Chuyển đổi sang binary
    plaintext_bits = string_to_bits(plaintext)
    key_bits = string_to_bits(key)
    print(f"🔢 BINARY CONVERSION:")
    print(f"Plaintext: {plaintext_bits}")
    print(f"Key:       {key_bits}")
    print(
        f"Length:    {len(plaintext_bits)} bits (plaintext), {len(key_bits)} bits (key)")
    print()

    # Initial Permutation
    ip_result = permute(plaintext_bits, IP)
    L0 = ip_result[:32]
    R0 = ip_result[32:]
    print(f"🔄 INITIAL PERMUTATION:")
    print(f"After IP: {ip_result}")
    print(f"L0: {L0}")
    print(f"R0: {R0}")
    print()

    # Key Schedule (PC-1)
    pc1_result = permute(key_bits, PC1)
    C0 = pc1_result[:28]
    D0 = pc1_result[28:]
    print(f"🔑 KEY SCHEDULE:")
    print(f"After PC-1: {pc1_result} ({len(pc1_result)} bits)")
    print(f"C0: {C0} ({len(C0)} bits)")
    print(f"D0: {D0} ({len(D0)} bits)")
    print()

    # Tạo Round Key 1
    C1 = left_shift(C0, 1)
    D1 = left_shift(D0, 1)
    CD1 = C1 + D1
    K1 = permute(CD1, PC2)
    print(f"🔗 ROUND KEY 1 GENERATION:")
    print(f"C1 (shifted): {C1}")
    print(f"D1 (shifted): {D1}")
    print(f"CD1:          {CD1} ({len(CD1)} bits)")
    print(f"K1 (PC-2):    {K1} ({len(K1)} bits)")
    print()

    # Demo F Function
    print(f"⚙️ F FUNCTION DEMO:")
    expanded_R0 = permute(R0, E)
    print(f"R0 original:     {R0} ({len(R0)} bits)")
    print(f"R0 expanded:     {expanded_R0} ({len(expanded_R0)} bits)")

    xor_result = xor(expanded_R0, K1)
    print(f"K1:              {K1}")
    print(f"XOR result:      {xor_result}")
    print()

    # S-Box demo chi tiết
    print(f"📦 S-BOX SUBSTITUTION:")
    groups = [xor_result[i:i+6] for i in range(0, 48, 6)]
    s_outputs = []

    for i, group in enumerate(groups[:2]):  # Demo 2 groups đầu
        if i == 0:
            s_out = s_box_substitute(group, S1)
            print(f"Group {i+1}: {group}")
            print(
                f"  Row: {int(group[0] + group[5], 2)}, Col: {int(group[1:5], 2)}")
            print(f"  S{i+1} output: {s_out}")
            s_outputs.append(s_out)
        elif i == 1:
            s_out = s_box_substitute(group, S2)
            print(f"Group {i+1}: {group}")
            print(
                f"  Row: {int(group[0] + group[5], 2)}, Col: {int(group[1:5], 2)}")
            print(f"  S{i+1} output: {s_out}")
            s_outputs.append(s_out)

    print(f"... (6 groups còn lại tương tự)")
    print()

    # P-Box demo
    print(f"🔀 P-BOX PERMUTATION DEMO:")
    # Giả sử có kết quả đầy đủ từ 8 S-Boxes
    s_box_output = "01011001000111011011111001001101"  # Kết quả từ guide
    print(f"S-Box output: {s_box_output}")

    p_result = permute(s_box_output, P)
    print(f"P-Box result: {p_result}")
    print()

    # Feistel Round demo
    print(f"🔄 FEISTEL ROUND 1 DEMO:")
    f_output = p_result  # Kết quả từ F function
    print(f"F(R0, K1):    {f_output}")
    print(f"L0:           {L0}")

    R1 = xor(L0, f_output)
    L1 = R0
    print(f"L1 = R0:      {L1}")
    print(f"R1 = L0⊕F:    {R1}")
    print()

    print("✅ DEMO HOÀN THÀNH!")
    print("📚 Tài liệu này minh họa các bước chính của DES.")
    print("🔒 Lưu ý: DES chỉ dùng cho mục đích học tập, không an toàn cho thực tế.")


def verify_calculations():
    """Xác minh các tính toán với dữ liệu từ guide"""
    print("\n" + "=" * 60)
    print("            VERIFICATION WITH GUIDE DATA")
    print("=" * 60)

    # Verify binary conversion
    expected_plaintext = "0100100001000101010011000100110001001111001100010011001000110011"
    expected_key = "0100110101011001010100110100010101000011010100100100010101010100"

    actual_plaintext = string_to_bits("HELLO123")
    actual_key = string_to_bits("MYSECRET")

    print("🔍 VERIFICATION:")
    print(
        f"✅ Plaintext binary: {'MATCH' if actual_plaintext == expected_plaintext else 'MISMATCH'}")
    print(
        f"✅ Key binary:       {'MATCH' if actual_key == expected_key else 'MISMATCH'}")

    # Debug prints
    print(f"\nDEBUG INFO:")
    print(f"Expected plaintext: {expected_plaintext}")
    print(f"Actual plaintext:   {actual_plaintext}")
    print(f"Expected key:       {expected_key}")
    print(f"Actual key:         {actual_key}")

    # Verify IP
    expected_ip = "1100110000000000110000001111111111110000101010101100110000001111"
    actual_ip = permute(actual_plaintext, IP)
    print(f"\nExpected IP:        {expected_ip}")
    print(f"Actual IP:          {actual_ip}")
    print(
        f"✅ Initial Perm:     {'MATCH' if actual_ip == expected_ip else 'MISMATCH'}")

    # Verify PC-1
    expected_pc1 = "00000000111111110000000010100011010011001001000000110110"
    actual_pc1 = permute(actual_key, PC1)
    print(f"\nExpected PC-1:      {expected_pc1}")
    print(f"Actual PC-1:        {actual_pc1}")
    print(
        f"✅ PC-1:             {'MATCH' if actual_pc1 == expected_pc1 else 'MISMATCH'}")

    # Verify K1
    C0 = actual_pc1[:28]
    D0 = actual_pc1[28:]
    C1 = left_shift(C0, 1)
    D1 = left_shift(D0, 1)
    CD1 = C1 + D1
    actual_k1 = permute(CD1, PC2)
    expected_k1 = "000110110000001011101111111111000111000001110010"
    print(f"\nExpected K1:        {expected_k1}")
    print(f"Actual K1:          {actual_k1}")
    print(
        f"✅ Round Key K1:     {'MATCH' if actual_k1 == expected_k1 else 'MISMATCH'}")

    if actual_plaintext == expected_plaintext and actual_key == expected_key:
        print("\n🎉 BINARY CONVERSION ĐÚNG!")
        if actual_pc1 == expected_pc1:
            print("🎉 PC-1 CALCULATION ĐÚNG!")
        else:
            print("⚠️  PC-1 có khác biệt - cần kiểm tra bảng PC1")
    else:
        print("\n⚠️  Có sự khác biệt trong binary conversion.")


if __name__ == "__main__":
    des_demo()
    verify_calculations()
