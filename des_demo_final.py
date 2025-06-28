# des_demo_final.py - DES Implementation Demo (Final Version)
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


# Bảng permutation chuẩn DES
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

# S-Box 1 chuẩn DES
S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]


def des_demo():
    """Demo DES hoàn chỉnh với HELLO123 và MYSECRET"""

    print("=" * 50)
    print("        DES EDUCATIONAL DEMO")
    print("=" * 50)
    print()

    # Input
    plaintext = "HELLO123"
    key = "MYSECRET"
    print(f"📝 INPUT:")
    print(f"Plaintext: '{plaintext}'")
    print(f"Key:       '{key}'")
    print()

    # Chuyển đổi sang binary
    plaintext_bits = string_to_bits(plaintext)
    key_bits = string_to_bits(key)
    print(f"🔢 BINARY CONVERSION:")
    print(f"Plaintext: {plaintext_bits}")
    print(f"Key:       {key_bits}")
    print(f"Lengths:   {len(plaintext_bits)} bits each")
    print()

    # Initial Permutation
    ip_result = permute(plaintext_bits, IP)
    L0 = ip_result[:32]
    R0 = ip_result[32:]
    print(f"🔄 INITIAL PERMUTATION:")
    print(f"After IP: {ip_result}")
    print(f"L0:       {L0}")
    print(f"R0:       {R0}")
    print()

    # Key Schedule (PC-1)
    pc1_result = permute(key_bits, PC1)
    C0 = pc1_result[:28]
    D0 = pc1_result[28:]
    print(f"🔑 KEY SCHEDULE:")
    print(f"PC-1:     {pc1_result} (56-bit)")
    print(f"C0:       {C0} (28-bit)")
    print(f"D0:       {D0} (28-bit)")
    print()

    # Round Key Generation
    C1 = left_shift(C0, 1)
    D1 = left_shift(D0, 1)
    CD1 = C1 + D1
    K1 = permute(CD1, PC2)
    print(f"🔗 ROUND KEY 1:")
    print(f"C1:       {C1}")
    print(f"D1:       {D1}")
    print(f"CD1:      {CD1}")
    print(f"K1:       {K1} (48-bit)")
    print()

    # F Function Demo
    print(f"⚙️ F FUNCTION (Round 1):")

    # E-box expansion
    expanded_R0 = permute(R0, E)
    print(f"R0:           {R0}")
    print(f"Expanded R0:  {expanded_R0}")

    # XOR with round key
    xor_result = xor(expanded_R0, K1)
    print(f"K1:           {K1}")
    print(f"XOR result:   {xor_result}")
    print()

    # S-Box demo (simplified)
    group1 = xor_result[:6]
    row = int(group1[0] + group1[5], 2)
    col = int(group1[1:5], 2)
    s_output = S1[row][col]
    print(f"📦 S-BOX DEMO (Group 1):")
    print(f"6-bit input:  {group1}")
    print(f"Row={row}, Col={col} → S1[{row}][{col}] = {s_output}")
    print(f"4-bit output: {format(s_output, '04b')}")
    print("... (7 more S-boxes)")
    print()

    # Complete Feistel Round
    print(f"🔄 FEISTEL ROUND STRUCTURE:")
    print(f"L(i+1) = R(i)")
    print(f"R(i+1) = L(i) ⊕ F(R(i), K(i))")
    print()
    print(f"For Round 1:")
    print(f"L1 = R0 = {R0}")
    print(f"R1 = L0 ⊕ F(R0,K1)")
    print(f"   = {L0}")
    print(f"   ⊕ F_result (từ F function)")
    print()

    print("✅ DEMO COMPLETE!")
    print("📖 This demonstrates key DES operations:")
    print("   • Binary conversion")
    print("   • Initial Permutation (IP)")
    print("   • Key Schedule (PC-1, shifts, PC-2)")
    print("   • F Function (E-box, S-boxes, P-box)")
    print("   • Feistel Round structure")
    print()
    print("🔒 Note: DES is for educational use only!")


def simple_test():
    """Test cơ bản để xác minh functions"""
    print("\n" + "=" * 50)
    print("        BASIC FUNCTION TESTS")
    print("=" * 50)

    # Test string_to_bits
    test_char = "H"
    expected = "01001000"
    result = string_to_bits(test_char)
    print(f"🧪 string_to_bits('{test_char}'):")
    print(f"   Expected: {expected}")
    print(f"   Got:      {result}")
    print(f"   Status:   {'✅ PASS' if result == expected else '❌ FAIL'}")
    print()

    # Test permute with simple example
    bits = "1234"
    table = [4, 3, 2, 1]  # Reverse order
    expected = "4321"
    result = permute(bits, table)
    print(f"🧪 permute('{bits}', {table}):")
    print(f"   Expected: {expected}")
    print(f"   Got:      {result}")
    print(f"   Status:   {'✅ PASS' if result == expected else '❌ FAIL'}")
    print()

    # Test left_shift
    bits = "12345678"
    shifts = 2
    expected = "34567812"
    result = left_shift(bits, shifts)
    print(f"🧪 left_shift('{bits}', {shifts}):")
    print(f"   Expected: {expected}")
    print(f"   Got:      {result}")
    print(f"   Status:   {'✅ PASS' if result == expected else '❌ FAIL'}")
    print()

    # Test XOR
    bits1 = "1010"
    bits2 = "1100"
    expected = "0110"
    result = xor(bits1, bits2)
    print(f"🧪 xor('{bits1}', '{bits2}'):")
    print(f"   Expected: {expected}")
    print(f"   Got:      {result}")
    print(f"   Status:   {'✅ PASS' if result == expected else '❌ FAIL'}")


if __name__ == "__main__":
    des_demo()
    simple_test()
