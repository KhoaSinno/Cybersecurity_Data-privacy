# HƯỚNG DẪN CHI TIẾT SHA-1 VÀ CÁC KIẾN THỨC LIÊN QUAN

## 1. Giới thiệu

Tài liệu này hướng dẫn chi tiết về thuật toán SHA-1 (Secure Hash Algorithm 1), các kiến thức liên quan (bit manipulation, padding, hash function), và cách thực hiện từng bước bằng Python. Phù hợp cho sinh viên, người tự học muốn hiểu bản chất và thực hành hash SHA-1.

---

## 1.1. Lý thuyết và luồng hoạt động của SHA-1

### Lý thuyết cơ bản

- SHA-1 là thuật toán hash mật mã, tạo ra digest 160-bit (40 ký tự hex) từ bất kỳ dữ liệu đầu vào nào.
- SHA-1 là hàm một chiều: dễ tính hash từ message, nhưng rất khó tìm ngược message từ hash.
- Độ an toàn của SHA-1 hiện tại không còn cao do khả năng tạo collision, nhưng vẫn được dùng rộng rãi.

### Luồng hoạt động tổng quát của SHA-1

1. **Padding (Đệm)**
   - Thêm bit '1' vào cuối message.
   - Thêm các bit '0' để độ dài ≡ 448 (mod 512).
   - Thêm 64-bit cuối cùng chứa độ dài message gốc.

2. **Chia thành blocks**
   - Chia message đã padding thành các block 512-bit.
   - Mỗi block được xử lý qua 80 rounds.

3. **Khởi tạo Hash Values**
   - 5 thanh ghi 32-bit: H0, H1, H2, H3, H4 với giá trị khởi tạo cố định.

4. **Xử lý từng block**
   - 80 rounds với 4 hàm logic f0, f1, f2, f3.
   - Sử dụng các hằng số K và message schedule.

5. **Kết quả cuối cùng**
   - Ghép H0, H1, H2, H3, H4 thành hash 160-bit.

### Minh họa

- Message: "hello"
- Sau padding: "hello" + '1' + '0'*... + length
- Xử lý qua SHA-1: H₀H₁H₂H₃H₄ → Hash cuối cùng
- Kết quả: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d

> **Lưu ý:** SHA-1 không còn an toàn cho mục đích bảo mật quan trọng, nên chuyển sang SHA-256 hoặc SHA-3.

---

## 2. Kiến thức nền tảng

### 2.1. Bit Manipulation

- Thao tác bit: AND (&), OR (|), XOR (^), NOT (~), LEFT SHIFT (<<), RIGHT SHIFT (>>).
- Left Rotate: Xoay trái k bit, bit ngoài cùng trái chuyển về phải.
- Ví dụ: `ROTL(1010, 2) = 1010` (32-bit context).

### 2.2. Padding Message

- Mục đích: Đưa message về độ dài chuẩn cho SHA-1 (bội số của 512 bit).
- Quy tắc: Message + '1' + k×'0' + 64-bit length, sao cho tổng ≡ 0 (mod 512).

### 2.3. Message Schedule

- Mở rộng 16 words 32-bit thành 80 words cho 80 rounds.
- W[i] = ROTL(W[i-3] ⊕ W[i-8] ⊕ W[i-14] ⊕ W[i-16], 1) với i ≥ 16.

---

## 3. Các bước thực hiện SHA-1

### Bước 1: Padding Message

- Thêm bit '1' vào cuối message.
- Thêm k bits '0' sao cho (length + 1 + k) ≡ 448 (mod 512).
- Thêm 64-bit cuối là độ dài message gốc (big-endian).

### Bước 2: Khởi tạo Hash Values

- H0 = 0x67452301
- H1 = 0xEFCDAB89
- H2 = 0x98BADCFE
- H3 = 0x10325476
- H4 = 0xC3D2E1F0

### Bước 3: Xử lý từng Block 512-bit

- Chia block thành 16 words 32-bit: W[0] đến W[15].
- Mở rộng thành 80 words: W[16] đến W[79].
- Thực hiện 80 rounds với 4 hàm logic.

### Bước 4: 4 Hàm logic

- f0(B,C,D) = (B & C) | (~B & D) (rounds 0-19)
- f1(B,C,D) = B ⊕ C ⊕ D (rounds 20-39)
- f2(B,C,D) = (B & C) | (B & D) | (C & D) (rounds 40-59)
- f3(B,C,D) = B ⊕ C ⊕ D (rounds 60-79)

### Bước 5: 80 Rounds

- Rounds 0-19: Dùng hàm f0, K = 0x5A827999
- Rounds 20-39: Dùng hàm f1, K = 0x6ED9EBA1
- Rounds 40-59: Dùng hàm f2, K = 0x8F1BBCDC
- Rounds 60-79: Dùng hàm f3, K = 0xCA62C1D6

### Bước 6: Kết quả cuối cùng

- Ghép H0, H1, H2, H3, H4 theo thứ tự big-endian thành hash 160-bit.

---

## 4. Ví dụ thực tế

### Ví dụ 1: Message "a"

- Message: "a" (ASCII: 0x61)
- Binary: 01100001
- Sau padding: 01100001 1 000...000 [length=8 in 64-bit]
- Hash SHA-1: 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8

### Ví dụ 2: Message "hello"

- Message: "hello"
- Binary: 0110100001100101011011000110110001101111
- Sau padding: [message] 1 000...000 [length=40 in 64-bit]
- Hash SHA-1: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d

### Ví dụ 3: Message rỗng ""

- Message: "" (empty)
- Sau padding: 1 000...000 [length=0 in 64-bit]
- Hash SHA-1: da39a3ee5e6b4b0d3255bfef95601890afd80709

---

## 5. Code Python mẫu

```python
import struct

def left_rotate(value, shift):
    """Left rotate a 32-bit integer by shift bits"""
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def sha1_padding(message):
    """Add padding to message for SHA-1"""
    msg_len = len(message)
    message += b'\x80'  # Add '1' bit
    
    # Add '0' bits until length ≡ 448 (mod 512)
    while len(message) % 64 != 56:
        message += b'\x00'
    
    # Add original length as 64-bit big-endian
    message += struct.pack('>Q', msg_len * 8)
    return message

def sha1_hash(message):
    """Compute SHA-1 hash of message"""
    # Initialize Hash Values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    
    # Constants for SHA-1
    K = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]
    
    # Pad message
    message = sha1_padding(message)
    
    # Process each 512-bit block
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        w = list(struct.unpack('>16I', block))
        
        # Extend to 80 words
        for j in range(16, 80):
            w.append(left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1))
        
        a, b, c, d, e = h0, h1, h2, h3, h4
        
        # 80 rounds
        for j in range(80):
            if j < 20:
                f = (b & c) | (~b & d)
                k = K[0]
            elif j < 40:
                f = b ^ c ^ d
                k = K[1]
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = K[2]
            else:
                f = b ^ c ^ d
                k = K[3]
            
            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
    
    # Return final hash
    return struct.pack('>5I', h0, h1, h2, h3, h4).hex()

def demo():
    messages = [b"", b"a", b"hello", b"The quick brown fox"]
    for msg in messages:
        hash_val = sha1_hash(msg)
        print(f"SHA-1('{msg.decode()}') = {hash_val}")

if __name__ == "__main__":
    demo()
```

---

## 6. Lưu ý bảo mật

- SHA-1 không còn an toàn cho mục đích mật mã do vulnerability collision.
- Google đã tạo thành công collision SHA-1 năm 2017 (SHAttered attack).
- Thay thế bằng SHA-256, SHA-3 cho các ứng dụng bảo mật quan trọng.
- SHA-1 vẫn có thể dùng cho checksum không quan trọng hoặc học tập.

---

## 7. Tham khảo

- RFC 3174: US Secure Hash Algorithm 1 (SHA1)
- Wikipedia: <https://en.wikipedia.org/wiki/SHA-1>
- NIST FIPS PUB 180-4: Secure Hash Standard
- SHAttered: <https://shattered.io/>
- Sách giáo trình Cryptography and Network Security
