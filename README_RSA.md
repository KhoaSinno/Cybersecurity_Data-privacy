# HƯỚNG DẪN CHI TIẾT RSA VÀ CÁC KIẾN THỨC LIÊN QUAN

## 1. Giới thiệu

Tài liệu này hướng dẫn chi tiết về giải thuật RSA, các kiến thức số học liên quan (modulo, nguyên tố cùng nhau, UCLN, BCNN), và cách thực hiện từng bước bằng Python. Phù hợp cho sinh viên, người tự học muốn hiểu bản chất và thực hành mã hóa RSA.

---

## 1.1. Lý thuyết và luồng hoạt động của RSA

### Lý thuyết cơ bản

- RSA là thuật toán mã hóa bất đối xứng, sử dụng một cặp khóa: khóa công khai (public key) để mã hóa và khóa bí mật (private key) để giải mã.
- Độ an toàn của RSA dựa trên bài toán phân tích một số lớn thành thừa số nguyên tố (rất khó khi n đủ lớn).
- Khóa công khai có thể chia sẻ rộng rãi, còn khóa bí mật phải giữ an toàn tuyệt đối.

### Luồng hoạt động tổng quát của RSA

1. **Sinh khóa**
   - Chọn hai số nguyên tố lớn p, q.
   - Tính n = p *q và φ(n) = (p-1)*(q-1).
   - Chọn số e sao cho 1 < e < φ(n) và UCLN(e, φ(n)) = 1.
   - Tìm d là nghịch đảo modular của e theo φ(n).
   - Công khai (n, e), giữ bí mật d.
2. **Mã hóa**
   - Bên gửi chuyển bản rõ m thành bản mã c bằng công thức: c = m^e mod n.
   - Gửi c cho bên nhận.
3. **Giải mã**
   - Bên nhận dùng khóa bí mật d để tính lại bản rõ: m = c^d mod n.

### Minh họa

- Người A muốn gửi tin nhắn cho B:
  - B công khai (n, e), giữ bí mật d.
  - A mã hóa tin nhắn bằng (n, e) rồi gửi cho B.
  - B nhận được bản mã, dùng d để giải mã lấy lại bản rõ.

> **Lưu ý:** Trong thực tế, RSA thường chỉ dùng để mã hóa khóa đối xứng (ví dụ AES), không dùng để mã hóa dữ liệu lớn vì tốc độ chậm.

---

## 2. Kiến thức nền tảng

### 2.1. Phép chia lấy dư (Modulo)

- Ký hiệu: `a mod n` là phần dư khi chia a cho n.
- Ví dụ: `17 mod 5 = 2` (vì 17 = 3*5 + 2).
- Trong Python: `17 % 5 = 2`.

### 2.2. Số nguyên tố cùng nhau

- Hai số a, b gọi là nguyên tố cùng nhau nếu `gcd(a, b) = 1`.
- Ví dụ: 8 và 15 là nguyên tố cùng nhau (gcd(8, 15) = 1).

### 2.3. UCLN (GCD) và BCNN (LCM)

- UCLN (gcd): Số lớn nhất chia hết cả a và b.
  - Ví dụ: UCLN(12, 18) = 6 (vì 6 là số lớn nhất chia hết cả 12 và 18)
  - UCLN(15, 28) = 1 (vì 1 là số lớn nhất chia hết cả 15 và 28)
- BCNN (lcm): Số nhỏ nhất chia hết cả a và b.
  - Ví dụ: BCNN(12, 18) = 36 (vì 36 là số nhỏ nhất chia hết cả 12 và 18)
  - BCNN(15, 28) = 420 (vì 420 là số nhỏ nhất chia hết cả 15 và 28)
- Công thức: `lcm(a, b) = (a * b) // gcd(a, b)`.
- Thuật toán Euclid tìm UCLN:

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

---

## 3. Các bước thực hiện RSA

### Bước 1: Chọn hai số nguyên tố lớn p, q

- Ví dụ: p = 61, q = 53

### Bước 2: Tính n = p * q

- n là modulus dùng cho cả khóa công khai và bí mật.
- Ví dụ: n = 61 * 53 = 3233

### Bước 3: Tính φ(n) = (p-1)*(q-1)

- φ(n) là số lượng số nguyên tố cùng nhau với n nhỏ hơn n.
- Ví dụ: φ(n) = 60 * 52 = 3120

### Bước 4: Chọn số e sao cho 1 < e < φ(n) và gcd(e, φ(n)) = 1

- e là số nguyên tố cùng nhau với φ(n), thường chọn 3, 17, 65537.
- Ví dụ: e = 17

### Bước 5: Tìm d sao cho e*d ≡ 1 (mod φ(n))

- d là nghịch đảo modular của e theo φ(n).
- Dùng thuật toán Euclid mở rộng:

```python
def modinv(e, phi):
    t, newt = 0, 1
    r, newr = phi, e
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise Exception('e không có nghịch đảo')
    if t < 0:
        t += phi
    return t
```

- Ví dụ: d = 2753

### Bước 6: Công khai (n, e), giữ bí mật d

- Khóa công khai: (n, e)
- Khóa bí mật: d

### Bước 7: Mã hóa và giải mã

- Mã hóa: `c = m^e mod n` (m là bản rõ, c là bản mã)
- Giải mã: `m = c^d mod n`
- Trong Python: `pow(m, e, n)` và `pow(c, d, n)`

---

## 4. Ví dụ thực tế

### Ví dụ 1

- p = 61, q = 53
- n = 3233
- φ(n) = 3120
- e = 17
- d = 2753
- Mã hóa m = 65: c = pow(65, 17, 3233) = 2790
- Giải mã: m = pow(2790, 2753, 3233) = 65

### Ví dụ 2

- p = 47, q = 71
- n = 3337
- φ(n) = 3220
- e = 79
- d = 1019
- Mã hóa m = 688: c = pow(688, 79, 3337) = 1570
- Giải mã: m = pow(1570, 1019, 3337) = 688

### Ví dụ 3: Nhỏ, dễ tính tay

- p = 3, q = 5
- n = 3 × 5 = 15
- φ(n) = (3-1) × (5-1) = 2 × 4 = 8
- Chọn e = 3 (UCLN(3,8) = 1)
- Tìm d sao cho 3 × d ≡ 1 (mod 8)
- `Nghĩa là d x e – 1 chia hết cho φ(n)`
- Nhẩm mồm: d x 3 - 1 chia hết cho 8

Vậy d = 3

**Kiểm tra:**
3 × 3 = 9 ≡ 1 (mod 8)

- Khóa công khai: (n=15, e=3)
- Khóa bí mật: d=3
- Mã hóa m = 7: c = 7^3 mod 15 = 343 mod 15 = 13
- Giải mã: m = 13^3 mod 15 = 2197 mod 15 = 7
- Mã hóa m = 69: c = 69^3 mod 15 = 328509 mod 15 = 9
- Giải mã: m = 9^3 mod 15 = 729 mod 15 = 9

**Nhận xét:**

- Khi m = 69 (lớn hơn n = 15), mã hóa và giải mã không ra đúng m ban đầu mà ra 9.
- Lý do: Trong RSA, m phải là số nguyên nhỏ hơn n (0 ≤ m < n). Nếu m ≥ n, kết quả sẽ không đúng.
- Vì vậy, với n = 15, chỉ nên mã hóa các số m = 0, 1, ..., 14.

---

## 5. Code Python mẫu

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def modinv(e, phi):
    t, newt = 0, 1
    r, newr = phi, e
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise Exception('e không có nghịch đảo')
    if t < 0:
        t += phi
    return t

def is_coprime(a, b):
    return gcd(a, b) == 1

def rsa_keygen(p, q, e):
    n = p * q
    phi = (p-1)*(q-1)
    if not is_coprime(e, phi):
        raise Exception('e không nguyên tố cùng phi(n)')
    d = modinv(e, phi)
    return (n, e, d)

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

def demo():
    p, q = 61, 53
    e = 17
    n, e, d = rsa_keygen(p, q, e)
    m = 65
    c = rsa_encrypt(m, e, n)
    m2 = rsa_decrypt(c, d, n)
    print(f"Plaintext: {m}, Ciphertext: {c}, Decrypted: {m2}")

if __name__ == "__main__":
    demo()
```

---

## 6. Lưu ý bảo mật

- Không dùng RSA với key nhỏ (nên >= 2048 bit)
- Không dùng RSA để mã hóa dữ liệu lớn, chỉ nên mã hóa key đối xứng
- e phổ biến: 3, 17, 65537

---

## 7. Tham khảo

- Wikipedia: <https://vi.wikipedia.org/wiki/RSA>
- Sách giáo trình An toàn thông tin
- Slide bài giảng môn Mật mã học
