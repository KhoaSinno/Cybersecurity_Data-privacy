# HƯỚNG DẪN CHI TIẾT MD5 VÀ CÁC KIẾN THỨC LIÊN QUAN

## 1. Giới thiệu

Tài liệu này hướng dẫn chi tiết về thuật toán MD5 (Message Digest 5), các kiến thức liên quan (bit manipulation, padding, hash function), và cách thực hiện từng bước bằng Python. Phù hợp cho sinh viên, người tự học muốn hiểu bản chất và thực hành hash MD5.

---

## 1.1. Lý thuyết và luồng hoạt động của MD5

### Lý thuyết cơ bản

- MD5 là thuật toán hash mật mã, tạo ra digest 128-bit (32 ký tự hex) từ bất kỳ dữ liệu đầu vào nào.
- MD5 là hàm một chiều: dễ tính hash từ message, nhưng rất khó tìm ngược message từ hash.
- Độ an toàn của MD5 hiện tại không còn cao do khả năng tạo collision, nhưng vẫn dùng cho checksum.

### Luồng hoạt động tổng quát của MD5

1. **Padding (Đệm)**
   - Thêm bit '1' vào cuối message.
   - Thêm các bit '0' để độ dài ≡ 448 (mod 512).
   - Thêm 64-bit cuối cùng chứa độ dài message gốc.

2. **Chia thành blocks**
   - Chia message đã padding thành các block 512-bit.
   - Mỗi block được xử lý qua 64 rounds.

3. **Khởi tạo MD Buffer**
   - 4 thanh ghi 32-bit: A, B, C, D với giá trị khởi tạo cố định.

4. **Xử lý từng block**
   - 64 rounds với 4 hàm F, G, H, I.
   - Sử dụng các hằng số K và shift amounts cố định.

5. **Kết quả cuối cùng**
   - Ghép A, B, C, D thành hash 128-bit.

### Minh họa

- Message: "hello"
- Sau padding: "hello" + '1' + '0'*... + length
- Xử lý qua MD5: A₀B₀C₀D₀ → A₁B₁C₁D₁ → ... → Hash cuối cùng
- Kết quả: 5d41402abc4b2a76b9719d911017c592

> **Lưu ý:** MD5 không còn an toàn cho mục đích bảo mật, chỉ dùng cho checksum hoặc học tập.

---

## 2. Kiến thức nền tảng

### 2.1. Bit Manipulation

- Thao tác bit: AND (&), OR (|), XOR (^), NOT (~), LEFT SHIFT (<<), RIGHT SHIFT (>>).
- Ví dụ: `0b1010 & 0b1100 = 0b1000` (AND bit-wise).
- Trong Python: `10 & 12 = 8`.

### 2.2. Padding Message

- Mục đích: Đưa message về độ dài chuẩn cho MD5 (bội số của 512 bit).
- Quy tắc: Message + '1' + k×'0' + 64-bit length, sao cho tổng ≡ 0 (mod 512).

### 2.3. Hash Function Properties

- **Deterministic**: Cùng input cho cùng output.
- **Fixed output size**: Luôn ra 128-bit với MD5.
- **Avalanche effect**: Thay đổi 1 bit input → thay đổi ~50% bits output.
- **Pre-image resistance**: Khó tìm ngược input từ hash.

---

## 3. Các bước thực hiện MD5

### Bước 1: Padding Message

- Thêm bit '1' vào cuối message.
- Thêm k bits '0' sao cho (length + 1 + k) ≡ 448 (mod 512).
- Thêm 64-bit cuối là độ dài message gốc (little-endian).

### Bước 2: Khởi tạo MD Buffer

- A = 0x67452301
- B = 0xEFCDAB89  
- C = 0x98BADCFE
- D = 0x10325476

### Bước 3: Xử lý từng Block 512-bit

- Chia block thành 16 words 32-bit: X[0] đến X[15].
- Thực hiện 64 rounds với 4 hàm phụ trợ F, G, H, I.

### Bước 4: 4 Hàm phụ trợ

- F(X,Y,Z) = (X & Y) | (~X & Z)
- G(X,Y,Z) = (X & Z) | (Y & ~Z)  
- H(X,Y,Z) = X ^ Y ^ Z
- I(X,Y,Z) = Y ^ (X | ~Z)

### Bước 5: 64 Rounds

- Rounds 1-16: Dùng hàm F
- Rounds 17-32: Dùng hàm G
- Rounds 33-48: Dùng hàm H  
- Rounds 49-64: Dùng hàm I

### Bước 6: Kết quả cuối cùng

- Ghép A, B, C, D theo thứ tự little-endian thành hash 128-bit.

---

## 4. Ví dụ thực tế

### Ví dụ 1: Message "a"

- Message: "a" (ASCII: 0x61)
- Binary: 01100001
- Sau padding: 01100001 1 000...000 [length=8 in 64-bit]
- Hash MD5: 0cc175b9c0f1b6a831c399e269772661

### Ví dụ 2: Message "hello"

- Message: "hello"
- Binary: 0110100001100101011011000110110001101111
- Sau padding: [message] 1 000...000 [length=40 in 64-bit]  
- Hash MD5: 5d41402abc4b2a76b9719d911017c592

### Ví dụ 3: Message rỗng ""

- Message: "" (empty)
- Sau padding: 1 000...000 [length=0 in 64-bit]
- Hash MD5: d41d8cd98f00b204e9800998ecf8427e

---

## 5. Code Python mẫu

```python
import struct

def left_rotate(value, shift):
    """Left rotate a 32-bit integer by shift bits"""
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5_padding(message):
    """Add padding to message for MD5"""
    msg_len = len(message)
    message += b'\x80'  # Add '1' bit
    
    # Add '0' bits until length ≡ 448 (mod 512)
    while len(message) % 64 != 56:
        message += b'\x00'
    
    # Add original length as 64-bit little-endian
    message += struct.pack('<Q', msg_len * 8)
    return message

def md5_hash(message):
    """Compute MD5 hash of message"""
    # Initialize MD Buffer
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    
    # Constants for MD5
    K = [int(abs(math.sin(i + 1)) * (2**32)) & 0xFFFFFFFF for i in range(64)]
    
    # Shift amounts
    s = [7,12,17,22] * 4 + [5,9,14,20] * 4 + [4,11,16,23] * 4 + [6,10,15,21] * 4
    
    # Pad message
    message = md5_padding(message)
    
    # Process each 512-bit block
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        w = list(struct.unpack('<16I', block))
        
        a, b, c, d = h0, h1, h2, h3
        
        # 64 rounds
        for j in range(64):
            if j < 16:
                f = (b & c) | (~b & d)
                g = j
            elif j < 32:
                f = (d & b) | (~d & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * j) % 16
            
            f = (f + a + K[j] + w[g]) & 0xFFFFFFFF
            a, b, c, d = d, (b + left_rotate(f, s[j])) & 0xFFFFFFFF, b, c
        
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
    
    # Return final hash
    return struct.pack('<4I', h0, h1, h2, h3).hex()

def demo():
    messages = [b"", b"a", b"hello", b"The quick brown fox"]
    for msg in messages:
        hash_val = md5_hash(msg)
        print(f"MD5('{msg.decode()}') = {hash_val}")

if __name__ == "__main__":
    demo()
```

---

## 6. Lưu ý bảo mật

- MD5 không còn an toàn cho mục đích mật mã do vulnerability collision.
- Chỉ nên dùng MD5 cho checksum, không dùng cho password hashing.
- Thay thế bằng SHA-256, SHA-3, hoặc bcrypt cho security.
- MD5 vẫn hữu ích cho học tập và hiểu hash function.

---

## 7. Tham khảo

- RFC 1321: The MD5 Message-Digest Algorithm
- Wikipedia: <https://en.wikipedia.org/wiki/MD5>
- Sách giáo trình Cryptography and Network Security
- Slide bài giảng môn An toàn thông tin
