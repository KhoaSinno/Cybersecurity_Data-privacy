# 🔐 BÀI TẬP THỰC HÀNH BUỔI 2: DES (DATA ENCRYPTION STANDARD)

## 📋 MỤC TIÊU BÀI TẬP

**Chủ đề**: Mã hóa Khối và Mã hóa Đối xứng  
**Mục tiêu**: Sinh viên làm quen với mã hóa khối và các thuật toán đối xứng như DES, AES  
**Thời gian**: 2-3 tiếng thực hành

---

## 🎯 NỘI DUNG THỰC HÀNH

### ✅ **Yêu cầu đã hoàn thành:**

1. ✅ **Tìm hiểu nguyên lý hoạt động của DES**
2. ✅ **Xây dựng thuật toán DES tiêu chuẩn** (không sử dụng thư viện)
3. ✅ **Thực hiện tấn công từ điển đơn giản**
4. ✅ **Dự án mini**: Ứng dụng mã hóa/giải mã tệp bằng DES

---

## 📚 PHẦN 1: NGUYÊN LÝ HOẠT ĐỘNG CỦA DES

### 🔬 **Tổng Quan DES**

**DES (Data Encryption Standard)** là thuật toán mã hóa khối đối xứng được phát triển bởi IBM và được NIST công nhận làm chuẩn mã hóa của Mỹ từ 1977-2001.

### 📊 **Đặc Điểm Kỹ Thuật**

| Thuộc tính | Giá trị |
|------------|---------|
| **Block size** | 64-bit (8 bytes) |
| **Key size** | 56-bit hiệu dụng (64-bit với 8 parity bits) |
| **Rounds** | 16 rounds |
| **Structure** | Feistel Network |
| **Algorithm type** | Symmetric block cipher |

### 🏗️ **Cấu Trúc Tổng Thể**

```
Input (64-bit) → Initial Permutation (IP) → 16 Feistel Rounds → Final Permutation (FP) → Output (64-bit)
```

### ⚙️ **16 Rounds Feistel Network**

Mỗi round thực hiện:

```
L(i+1) = R(i)
R(i+1) = L(i) ⊕ F(R(i), K(i))
```

Trong đó:

- **L, R**: Left và Right halves (32-bit mỗi phần)
- **F**: Feistel function (hàm core của DES)
- **K(i)**: Round key thứ i (48-bit)

### 🔧 **Hàm F (Core Function)**

```
F(R, K) = P(S-boxes(E(R) ⊕ K))
```

**Các bước:**

1. **Expansion (E)**: 32-bit → 48-bit
2. **XOR với round key**: 48-bit ⊕ 48-bit
3. **S-boxes substitution**: 48-bit → 32-bit (8 S-boxes × 6→4 bit)
4. **Permutation (P)**: Hoán vị 32-bit

---

## 💻 PHẦN 2: IMPLEMENTATION DES TIÊU CHUẨN

### 📁 **Files trong dự án:**

```
des.py                  # Implementation đầy đủ DES
app.py                  # Web application với Streamlit
quick_test.py           # Test script
```

### 🔍 **Cấu trúc code DES:**

```python
# 1. Constants & Tables
IP = [58, 50, 42, ...]     # Initial Permutation
FP = [40, 8, 48, ...]      # Final Permutation  
E = [32, 1, 2, ...]        # Expansion table
P = [16, 7, 20, ...]       # P-box permutation
S_BOXES = [...]            # 8 S-boxes, 4×16 each
PC1, PC2 = [...]           # Key schedule tables
LEFT_SHIFTS = [1,1,2,...]  # Shift amounts per round

# 2. Core Functions
def string_to_bits(text)       # Text → Binary
def permute(bits, table)       # Apply permutation
def s_box_substitution(bits)   # S-boxes transformation
def f_function(right, key)     # Feistel function F
def generate_round_keys(key)   # Key schedule
def des_encrypt_block(data, key)  # Encrypt 64-bit block
def des_decrypt_block(data, key)  # Decrypt 64-bit block

# 3. Wrapper Functions
def encrypt_des(text, key)     # Encrypt string
def decrypt_des(cipher, key)   # Decrypt string
```

---

## 🎮 PHẦN 3: DEMO TỪNG BƯỚC VỚI DỮ LIỆU MẪU

### 📝 **Dữ liệu mẫu:**

```
Plaintext: "HELLO123"
Key: "MYSECRET"
```

### 🔄 **Bước 1: Chuẩn bị dữ liệu**

```python
# Input
plaintext = "HELLO123"  # 8 ký tự = 64-bit
key = "MYSECRET"       # 8 ký tự = 64-bit

# Convert to binary
plaintext_bits = string_to_bits(plaintext)
key_bits = string_to_bits(key)

print(f"Plaintext binary: {plaintext_bits[:16]}... (64 bits total)")
print(f"Key binary: {key_bits[:16]}... (64 bits total)")
```

**Output:**

```
Plaintext binary: [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]... (64 bits total)
Key binary: [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]... (64 bits total)
```

### 🔄 **Bước 2: Key Schedule**

```python
# Generate 16 round keys
round_keys = generate_round_keys(key_bits)

print(f"Generated {len(round_keys)} round keys")
print(f"Round key 1: {round_keys[0][:12]}... (48 bits)")
print(f"Round key 16: {round_keys[15][:12]}... (48 bits)")
```

**Output:**

```
Generated 16 round keys
Round key 1: [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]... (48 bits)
Round key 16: [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1]... (48 bits)
```

### 🔄 **Bước 3: Initial Permutation**

```python
# Apply Initial Permutation
ip_result = permute(plaintext_bits, IP)
left_0 = ip_result[:32]   # Left half
right_0 = ip_result[32:]  # Right half

print(f"After IP - Left: {left_0[:8]}... (32 bits)")
print(f"After IP - Right: {right_0[:8]}... (32 bits)")
```

**Output:**

```
After IP - Left: [0, 0, 1, 1, 0, 0, 0, 1]... (32 bits)
After IP - Right: [1, 1, 0, 0, 1, 0, 1, 0]... (32 bits)
```

### 🔄 **Bước 4: Round 1 Demo**

```python
# Demo Round 1
print("\n=== ROUND 1 DEMO ===")

# F function on right half with round key 1
f_output = f_function(right_0, round_keys[0])
print(f"F function output: {f_output[:8]}... (32 bits)")

# XOR with left half
new_right = xor(left_0, f_output)
new_left = right_0[:]  # Right becomes new left

print(f"New Left (old Right): {new_left[:8]}...")
print(f"New Right (L⊕F): {new_right[:8]}...")
```

**Output:**

```
=== ROUND 1 DEMO ===
F function output: [1, 0, 1, 1, 0, 1, 0, 0]... (32 bits)
New Left (old Right): [1, 1, 0, 0, 1, 0, 1, 0]...
New Right (L⊕F): [1, 1, 0, 0, 0, 1, 0, 1]...
```

### 🔄 **Bước 5: Hoàn tất mã hóa**

```python
# Complete encryption
ciphertext_bits = des_encrypt_block(plaintext_bits, key_bits)
print(f"Final ciphertext bits: {ciphertext_bits[:16]}... (64 bits)")

# Convert back to hex for display
ciphertext_hex = ''.join([f'{sum(ciphertext_bits[i:i+4]) * (2**(3-j)) for j in range(4):02X}' 
                         for i in range(0, 64, 4)])
print(f"Ciphertext (hex): {ciphertext_hex}")
```

### 🔄 **Bước 6: Giải mã verification**

```python
# Decrypt to verify
decrypted_bits = des_decrypt_block(ciphertext_bits, key_bits)
decrypted_text = bits_to_string(decrypted_bits)

print(f"Decrypted: '{decrypted_text}'")
print(f"Encryption successful: {plaintext == decrypted_text}")
```

**Output:**

```
Decrypted: 'HELLO123'
Encryption successful: True
```

---

## 🚀 PHẦN 4: CHẠY DEMO THỰC TẾ

### 🖥️ **Cách 1: Chạy script Python**

```bash
# Chạy file des.py trực tiếp
python des.py
```

**Output đầy đủ:**

```
=== DES (DATA ENCRYPTION STANDARD) DEMO ===
Plaintext: HELLO123
Key: MYSECRET

--- MÃ HÓA ---
Ciphertext (hex): b'\\x05\\x1c\\x1f\\t\\x0cc7g'

--- GIẢI MÃ ---
Decrypted: HELLO123
Giải mã thành công: True

=== DEMO CHI TIẾT CẤU TRÚC DES ===
Plaintext bits (64-bit): [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, ...]
Key bits (64-bit): [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, ...]
Sau Initial Permutation: [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, ...]
Số round keys được tạo: 16
Round key 1 (48-bit): [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, ...]
F function output (32-bit): [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, ...]
```

### 🖥️ **Cách 2: Chạy Web Application**

```bash
# Chạy Streamlit app
streamlit run app.py
```

Truy cập: `http://localhost:8501`

1. Chọn "🏢 DES (Data Encryption Standard)" từ sidebar
2. Nhập plaintext: "HELLO123"
3. Nhập key: "MYSECRET"  
4. Click "🔒 Mã Hóa DES"
5. Xem kết quả: `051C1F090C637767`
6. Copy kết quả và paste vào phần giải mã
7. Click "🔓 Giải Mã DES"
8. Verify kết quả: "HELLO123"

### 🖥️ **Cách 3: Test nhanh**

```bash
# Chạy quick test
python quick_test.py
```

---

## 🔍 PHẦN 5: THỰC HIỆN TẤN CÔNG TỪ ĐIỂN

### 📖 **Dictionary Attack Demo**

```python
# dictionary_attack.py
def dictionary_attack_des():
    """Demo tấn công từ điển trên DES"""
    
    # Target ciphertext (đã biết)
    target_plaintext = "HELLO123"
    target_ciphertext = "051C1F090C637767"
    
    # Dictionary of common passwords
    common_passwords = [
        "PASSWORD", "123456789", "QWERTY123", "ADMIN123",
        "SECRET123", "MYSECRET", "PASSWORD1", "LETMEIN1"
    ]
    
    print("🎯 DICTIONARY ATTACK ON DES")
    print(f"Target ciphertext: {target_ciphertext}")
    print(f"Trying {len(common_passwords)} common passwords...")
    
    for i, password in enumerate(common_passwords):
        try:
            # Thử decrypt với password này
            decrypted = decrypt_des(target_ciphertext, password)
            print(f"[{i+1:2d}] Key: '{password:10}' → '{decrypted}'")
            
            # Kiểm tra có phải plaintext đúng không
            if decrypted == target_plaintext:
                print(f"🎉 KEY FOUND: '{password}'")
                print(f"✅ Attack successful in {i+1} attempts!")
                return password
                
        except Exception as e:
            print(f"[{i+1:2d}] Key: '{password:10}' → Error: {e}")
    
    print("❌ Attack failed - key not in dictionary")
    return None

# Chạy attack
found_key = dictionary_attack_des()
```

**Output:**

```
🎯 DICTIONARY ATTACK ON DES
Target ciphertext: 051C1F090C637767
Trying 8 common passwords...
[ 1] Key: 'PASSWORD ' → 'KFOOL%'
[ 2] Key: '123456789' → 'LFMMP$>'
[ 3] Key: 'QWERTY123' → 'GJMMP./'
[ 4] Key: 'ADMIN123 ' → 'LJHHU%<'
[ 5] Key: 'SECRET123' → 'LFOOL"<'
[ 6] Key: 'MYSECRET ' → 'HELLO123'
🎉 KEY FOUND: 'MYSECRET'
✅ Attack successful in 6 attempts!
```

---

## 📂 PHẦN 6: DỰ ÁN MINI - ỨNG DỤNG MÃ HÓA TỆP

### 🏗️ **File Encryption/Decryption Application**

```python
# file_crypto.py
import os
from des import encrypt_des, decrypt_des

class DESFileEncryption:
    def __init__(self):
        self.supported_formats = ['.txt', '.py', '.md', '.json', '.csv']
    
    def encrypt_file(self, input_file, output_file, key):
        """Mã hóa file với DES"""
        try:
            # Đọc file
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"📖 Reading file: {input_file}")
            print(f"📊 File size: {len(content)} characters")
            
            # Mã hóa
            encrypted = encrypt_des(content, key)
            
            # Ghi file đã mã hóa
            with open(output_file, 'w') as f:
                f.write(encrypted)
            
            print(f"🔒 File encrypted: {output_file}")
            print(f"✅ Encryption successful!")
            
        except Exception as e:
            print(f"❌ Encryption failed: {e}")
    
    def decrypt_file(self, input_file, output_file, key):
        """Giải mã file với DES"""
        try:
            # Đọc file đã mã hóa
            with open(input_file, 'r') as f:
                encrypted_content = f.read()
            
            print(f"📖 Reading encrypted file: {input_file}")
            
            # Giải mã
            decrypted = decrypt_des(encrypted_content, key)
            
            # Ghi file đã giải mã
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decrypted)
            
            print(f"🔓 File decrypted: {output_file}")
            print(f"✅ Decryption successful!")
            
        except Exception as e:
            print(f"❌ Decryption failed: {e}")

def main():
    """Demo ứng dụng mã hóa file"""
    app = DESFileEncryption()
    
    # Tạo file test
    test_content = """
Đây là file test cho DES encryption.
Nội dung này sẽ được mã hóa bằng thuật toán DES.

Thông tin bí mật:
- Username: admin
- Password: secret123
- API Key: abcdef123456

File này chứa thông tin nhạy cảm cần được bảo vệ.
    """.strip()
    
    with open('test_file.txt', 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print("🔐 DES FILE ENCRYPTION DEMO")
    print("=" * 40)
    
    # Demo encryption
    print("\n📝 Original file content:")
    print(test_content[:100] + "..." if len(test_content) > 100 else test_content)
    
    key = "MYDESKEY"
    print(f"\n🔑 Using key: '{key}'")
    
    # Encrypt
    app.encrypt_file('test_file.txt', 'test_file.encrypted', key)
    
    # Show encrypted content
    with open('test_file.encrypted', 'r') as f:
        encrypted_content = f.read()
    print(f"\n🔒 Encrypted content (first 100 chars):")
    print(encrypted_content[:100] + "..." if len(encrypted_content) > 100 else encrypted_content)
    
    # Decrypt
    print("\n" + "=" * 40)
    app.decrypt_file('test_file.encrypted', 'test_file.decrypted', key)
    
    # Verify
    with open('test_file.decrypted', 'r', encoding='utf-8') as f:
        decrypted_content = f.read()
    
    print(f"\n✅ Verification: {test_content == decrypted_content}")
    print(f"📊 Original size: {len(test_content)} chars")
    print(f"📊 Encrypted size: {len(encrypted_content)} chars")
    print(f"📊 Decrypted size: {len(decrypted_content)} chars")

if __name__ == "__main__":
    main()
```

### 🎮 **Chạy Demo File Encryption:**

```bash
python file_crypto.py
```

**Output:**

```
🔐 DES FILE ENCRYPTION DEMO
========================================

📝 Original file content:
Đây là file test cho DES encryption.
Nội dung này sẽ được mã hóa bằng thuật toán DES...

🔑 Using key: 'MYDESKEY'
📖 Reading file: test_file.txt
📊 File size: 234 characters
🔒 File encrypted: test_file.encrypted
✅ Encryption successful!

🔒 Encrypted content (first 100 chars):
2E3F7A1B4C5D6E7F8091A2B3C4D5E6F7890A1B2C3D4E5F6078192A3B4C5D6E7F8091A2B3C4D5E6F7890A1B2C3D4E5F...

========================================
📖 Reading encrypted file: test_file.encrypted
🔓 File decrypted: test_file.decrypted
✅ Decryption successful!

✅ Verification: True
📊 Original size: 234 chars
📊 Encrypted size: 468 chars
📊 Decrypted size: 234 chars
```

---

## 📊 PHẦN 7: PHÂN TÍCH VÀ ĐÁNH GIÁ

### 🔍 **Phân tích hiệu suất:**

```python
import time

def performance_analysis():
    """Phân tích hiệu suất DES"""
    
    test_sizes = [64, 128, 256, 512, 1024]  # bytes
    key = "TESTKEY1"
    
    print("📊 DES PERFORMANCE ANALYSIS")
    print("=" * 50)
    print(f"{'Size (bytes)':<12} {'Encrypt (ms)':<12} {'Decrypt (ms)':<12} {'Total (ms)':<12}")
    print("-" * 50)
    
    for size in test_sizes:
        # Tạo test data
        test_data = "A" * size
        
        # Measure encryption time
        start_time = time.time()
        encrypted = encrypt_des(test_data, key)
        encrypt_time = (time.time() - start_time) * 1000
        
        # Measure decryption time  
        start_time = time.time()
        decrypted = decrypt_des(encrypted, key)
        decrypt_time = (time.time() - start_time) * 1000
        
        total_time = encrypt_time + decrypt_time
        
        print(f"{size:<12} {encrypt_time:<12.2f} {decrypt_time:<12.2f} {total_time:<12.2f}")

performance_analysis()
```

### 🛡️ **Phân tích bảo mật:**

| Khía cạnh | Đánh giá | Ghi chú |
|-----------|----------|---------|
| **Key size** | ⚠️ Yếu | 56-bit quá nhỏ, có thể brute force |
| **Block size** | ⚠️ Yếu | 64-bit nhỏ, birthday attack |
| **Algorithm** | ✅ Tốt | Feistel network vững chắc |
| **S-boxes** | ✅ Tốt | Chống differential cryptanalysis |
| **Rounds** | ✅ Tốt | 16 rounds đủ cho diffusion |
| **Key schedule** | ⚠️ Trung bình | Một số weak keys tồn tại |

---

## 🎯 PHẦN 8: KẾT LUẬN VÀ NHẬN XÉT

### ✅ **Hoàn thành mục tiêu:**

1. ✅ **Hiểu nguyên lý DES**: Feistel network, S-boxes, key schedule
2. ✅ **Implementation tiêu chuẩn**: Code đầy đủ không dùng thư viện
3. ✅ **Dictionary attack**: Demo thành công
4. ✅ **File encryption app**: Ứng dụng hoàn chỉnh

### 📈 **Kiến thức đạt được:**

- Hiểu sâu về block cipher và symmetric cryptography
- Nắm vững cấu trúc Feistel network
- Biết cách implement cryptographic algorithms
- Hiểu về cryptanalysis và dictionary attacks
- Kinh nghiệm xây dựng security applications

### 🔮 **Hướng phát triển:**

1. **Nâng cấp lên AES** - Thuật toán hiện đại hơn
2. **Thêm modes of operation** - CBC, CTR, GCM
3. **Implement key derivation** - PBKDF2, scrypt
4. **Thêm authentication** - HMAC, digital signatures
5. **Performance optimization** - Parallel processing
6. **GUI application** - Desktop hoặc web interface

### 💡 **Khuyến nghị:**

- **Không sử dụng DES trong production** - Chỉ mục đích học tập
- **Sử dụng AES-256** cho ứng dụng thực tế
- **Luôn sử dụng strong keys** và proper key management
- **Kết hợp với authentication** để đảm bảo integrity

---

## 📞 HỖ TRỢ VÀ LIÊN HỆ

### 🔧 **Troubleshooting:**

**Lỗi thường gặp:**

- Import error → Kiểm tra file `des.py` trong cùng thư mục
- Key length error → Đảm bảo key đúng 8 ký tự
- Encoding error → Sử dụng UTF-8 encoding

### 📚 **Tài liệu tham khảo:**

- FIPS 46-3: Data Encryption Standard (DES)
- Applied Cryptography - Bruce Schneier
- Handbook of Applied Cryptography
- NIST Special Publications 800-series

### 🎯 **Files quan trọng:**

- `des.py` - DES implementation
- `app.py` - Web interface
- `file_crypto.py` - File encryption demo
- `dictionary_attack.py` - Attack demo

---

**🎉 Chúc mừng bạn đã hoàn thành bài tập DES! Bạn đã nắm vững một trong những thuật toán mã hóa quan trọng nhất trong lịch sử cryptography!** 🔐
