"""
CRYPTOGRAPHY EDUCATION WEB APP
==============================
Ứng dụng web giáo dục về các thuật toán mã hóa
Sử dụng Streamlit để tạo giao diện tương tác
"""

import streamlit as st
import numpy as np
from caesar import encrypt_caesar, decrypt_caesar
from vigenere import encrypt_vigenere, decrypt_vigenere
from playfair import encrypt_playfair, decrypt_playfair
from hill import encrypt_hill, decrypt_hill
from des import encrypt_des, decrypt_des
from permutation import encrypt_permutation, decrypt_permutation
from polyalphabetic import encrypt_polyalphabetic, decrypt_polyalphabetic

# Cấu hình trang
st.set_page_config(
    page_title="Cryptography Education Platform",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh để làm đẹp giao diện
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.algorithm-header {
    font-size: 2rem;
    color: #ff7f0e;
    margin-top: 2rem;
    margin-bottom: 1rem;
    border-left: 5px solid #ff7f0e;
    padding-left: 15px;
}
.info-box {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #1f77b4;
    margin: 1rem 0;
}
.success-box {
    background-color: #d4edda;
    color: #155724;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #28a745;
    margin: 1rem 0;
}
.warning-box {
    background-color: #fff3cd;
    color: #856404;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #ffc107;
    margin: 1rem 0;
}
.example-box {
    background-color: #e7f3ff;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    border: 1px solid #b3d9ff;
}
</style>
""", unsafe_allow_html=True)

def main():
    # Header chính
    st.markdown('<h1 class="main-header">🔐 Nền Tảng Giáo Dục Mã Hóa</h1>', unsafe_allow_html=True)
    
    # Sidebar để chọn thuật toán
    st.sidebar.markdown("## 📚 Chọn Thuật Toán")
    algorithm = st.sidebar.selectbox(
        "Thuật toán mã hóa:",
        [
            "🏠 Trang Chủ",
            "🔤 Caesar Cipher", 
            "🗝️ Vigenère Cipher",
            "🎭 Playfair Cipher", 
            "🧮 Hill Cipher",
            "🔀 Polyalphabetic Cipher",
            "🔄 Permutation Cipher",
            "🏢 DES (Data Encryption Standard)"
        ]
    )

    if algorithm == "🏠 Trang Chủ":
        show_homepage()
    elif algorithm == "🔤 Caesar Cipher":
        show_caesar_cipher()
    elif algorithm == "🗝️ Vigenère Cipher":
        show_vigenere_cipher()
    elif algorithm == "🎭 Playfair Cipher":
        show_playfair_cipher()
    elif algorithm == "🧮 Hill Cipher":
        show_hill_cipher()
    elif algorithm == "🔀 Polyalphabetic Cipher":
        show_polyalphabetic_cipher()
    elif algorithm == "🔄 Permutation Cipher":
        show_permutation_cipher()
    elif algorithm == "🏢 DES (Data Encryption Standard)":
        show_des_cipher()

def show_homepage():
    """Hiển thị trang chủ với tổng quan về mã hóa"""
    
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 👋 Chào mừng đến với Nền Tảng Giáo Dục Mã Hóa!
    
    Đây là ứng dụng web tương tác giúp bạn học và thực hành các thuật toán mã hóa từ cổ điển đến hiện đại.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Thống kê thuật toán
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Thuật Toán Cổ Điển", "4", "Caesar, Vigenère, Playfair, Hill")
    
    with col2:
        st.metric("Thuật Toán Hiện Đại", "3", "Polyalphabetic, Permutation, DES")
    
    with col3:
        st.metric("Độ Bảo Mật", "Từ Yếu → Mạnh", "Học từ cơ bản đến nâng cao")
    
    with col4:
        st.metric("Tính Năng", "100%", "Demo trực tiếp + Giải thích")

    # Phân loại thuật toán
    st.markdown('<h2 class="algorithm-header">📊 Phân Loại Thuật Toán</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🔄 Theo Phương Pháp", "📅 Theo Thời Đại", "🔒 Theo Độ Bảo Mật"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="example-box">', unsafe_allow_html=True)
            st.markdown("""
            **🔄 SUBSTITUTION (Thay Thế)**
            - **Caesar**: Thay thế đơn giản với dịch chuyển cố định
            - **Vigenère**: Thay thế đa bảng cơ bản  
            - **Playfair**: Thay thế cặp ký tự (digraph)
            - **Hill**: Thay thế khối với ma trận
            """)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="example-box">', unsafe_allow_html=True)
            st.markdown("""
            **🔀 TRANSPOSITION (Hoán Vị)**
            - **Permutation**: Sắp xếp lại vị trí ký tự
            - **Columnar**: Hoán vị theo cột
            - **Block**: Hoán vị theo khối
            
            **🏢 MODERN (Hiện Đại)**
            - **DES**: Mã hóa khối với Feistel network
            """)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        timeline_data = {
            "🏛️ Cổ Điển (Trước 1900)": ["Caesar Cipher", "Vigenère Cipher", "Playfair Cipher"],
            "🔬 Hiện Đại Sớm (1900-1970)": ["Hill Cipher", "Advanced Polyalphabetic"],
            "💻 Hiện Đại (1970-nay)": ["DES", "AES", "RSA (không có trong demo này)"]
        }
        
        for period, algorithms in timeline_data.items():
            st.markdown(f"**{period}**")
            for alg in algorithms:
                st.markdown(f"- {alg}")
    
    with tab3:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("""
        **⚠️ Lưu Ý Bảo Mật:**
        
        - 🔴 **Rất Yếu**: Caesar (chỉ 25 khả năng)
        - 🟡 **Yếu**: Playfair, Vigenère đơn giản
        - 🟠 **Trung Bình**: Hill, Polyalphabetic nâng cao  
        - 🟢 **Mạnh (thời kỳ đó)**: DES
        - ⚫ **Lưu Ý**: Tất cả đều đã lỗi thời cho bảo mật thực tế!
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Hướng dẫn sử dụng
    st.markdown('<h2 class="algorithm-header">📖 Hướng Dẫn Sử Dụng</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 🚀 Cách Sử Dụng Ứng Dụng:
    
    1. **Chọn thuật toán** từ sidebar bên trái
    2. **Đọc lý thuyết** và ví dụ minh họa
    3. **Thử nghiệm** với văn bản và khóa của bạn
    4. **So sánh** kết quả mã hóa và giải mã
    5. **Học hỏi** từ các ví dụ có sẵn
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def show_caesar_cipher():
    """Hiển thị Caesar Cipher với demo tương tác"""
    
    st.markdown('<h2 class="algorithm-header">🔤 Caesar Cipher - Mã Hóa Dịch Chuyển</h2>', unsafe_allow_html=True)
    
    # Lý thuyết
    with st.expander("📚 Lý Thuyết & Nguyên Lý", expanded=True):
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Caesar Cipher** là thuật toán mã hóa cổ điển đơn giản nhất, được đặt tên theo hoàng đế La Mã Julius Caesar.
        
        **🔬 Nguyên Lý:**
        - Dịch chuyển mỗi ký tự trong bảng chữ cái một số vị trí cố định (shift/key)
        - Ví dụ: với shift = 3, A → D, B → E, C → F
        - Wrap around: X → A, Y → B, Z → C
        
        **📐 Công Thức Toán Học:**
        - Mã hóa: `E(x) = (x + k) mod 26`
        - Giải mã: `D(x) = (x - k) mod 26`
        
        Trong đó: x = vị trí ký tự (A=0, B=1, ..., Z=25), k = shift value
        
        **🔢 Không gian khóa:** 25 khóa có thể (k = 1, 2, 3, ..., 25)
        **⚡ Độ phức tạp:** O(n) cho mã hóa/giải mã, O(1) cho brute force
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mã giả
    with st.expander("💻 Mã Giả (Pseudocode)"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Thuật toán mã hóa Caesar:**
        ```
        FUNCTION CaesarEncrypt(plaintext, shift):
            ciphertext = ""
            FOR each character c in plaintext:
                IF c is a letter:
                    base = 'A' if c is uppercase else 'a'
                    shifted = (c - base + shift) mod 26
                    ciphertext += char(shifted + base)
                ELSE:
                    ciphertext += c  // Giữ nguyên ký tự không phải chữ cái
            RETURN ciphertext
        ```
        
        **Thuật toán giải mã Caesar:**
        ```
        FUNCTION CaesarDecrypt(ciphertext, shift):
            plaintext = ""
            FOR each character c in ciphertext:
                IF c is a letter:
                    base = 'A' if c is uppercase else 'a'
                    shifted = (c - base - shift + 26) mod 26
                    plaintext += char(shifted + base)
                ELSE:
                    plaintext += c
            RETURN plaintext
        ```
        
        **Tấn công Brute Force:**
        ```
        FUNCTION BruteForceAttack(ciphertext):
            FOR shift = 1 to 25:
                candidate = CaesarDecrypt(ciphertext, shift)
                PRINT "Shift", shift, ":", candidate
                // Người dùng kiểm tra candidate nào có nghĩa
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Ví dụ minh họa
    with st.expander("🎯 Ví Dụ Minh Họa & Tính Toán"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Ví dụ với Shift = 3:**
        ```
        Text gốc:  H  E  L  L  O
        Vị trí:    7  4  11 11 14
        +3:        10 7  14 14 17
        Kết quả:   K  H  O  O  R
        ```
        
        **Bảng Dịch Chuyển đầy đủ:**
        ```
        A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
        D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
        ```
        
        **Chi tiết tính toán cho 'H':**
        1. `ord('H') = 72`
        2. `72 - ord('A') = 72 - 65 = 7` (chuyển về 0-25)
        3. `(7 + 3) mod 26 = 10`
        4. `10 + ord('A') = 10 + 65 = 75`
        5. `chr(75) = 'K'`
        
        **Wrap-around với 'X', 'Y', 'Z':**
        - X (23) + 3 = 26 mod 26 = 0 → A
        - Y (24) + 3 = 27 mod 26 = 1 → B  
        - Z (25) + 3 = 28 mod 26 = 2 → C
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Phân tích bảo mật
    with st.expander("🔒 Phân Tích Bảo Mật & Tấn công"):
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("""
        **⚠️ Điểm yếu của Caesar Cipher:**
        
        **1. Brute Force Attack:**
        - Chỉ 25 khóa có thể → dễ dàng thử hết
        - Thời gian: O(1) - ngay lập tức
        
        **2. Frequency Analysis:**
        - Giữ nguyên tần suất xuất hiện ký tự
        - Ký tự xuất hiện nhiều nhất thường là 'E' → tìm shift
        
        **3. Pattern Recognition:**
        - Các từ ngắn như "THE", "AND" dễ nhận ra
        - Khoảng cách giữa các ký tự không đổi
        
        **4. Statistical Analysis:**
        - Index of Coincidence không đổi
        - Chi-squared test có thể phát hiện Caesar
        
        **Ví dụ Frequency Analysis:**
        ```
        Ciphertext: "KHOOR ZRUOG"
        Frequency: K=1, H=1, O=2, R=2, Z=1, U=1, G=1
        
        Nếu O tương ứng với E (xuất hiện nhiều):
        O = 14, E = 4 → shift = 14 - 4 = 10
        Hoặc shift = (14 - 4 + 26) mod 26 = 10
        
        Nhưng thử shift = 23: K→H, H→E, O→L, ...
        Kết quả: "HELLO WORLD" ✓
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        ```
        Text gốc:  H  E  L  L  O
        Shift +3:  K  H  O  O  R
        Kết quả:   KHOOR
        ```
        
        **Bảng Dịch Chuyển:**
        ```
        A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
        D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Demo tương tác
    st.markdown("### 🎮 Demo Tương Tác")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔐 Mã Hóa")
        plain_text = st.text_area("Nhập văn bản cần mã hóa:", value="HELLO WORLD", height=100)
        shift_encrypt = st.slider("Chọn shift value:", min_value=1, max_value=25, value=3, key="caesar_encrypt")
        
        if st.button("🔒 Mã Hóa Caesar", key="encrypt_caesar"):
            try:
                encrypted = encrypt_caesar(plain_text, shift_encrypt)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả mã hóa:** `{encrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Hiển thị chi tiết quá trình
                st.markdown("**Chi tiết quá trình:**")
                for i, char in enumerate(plain_text.upper()):
                    if char.isalpha():
                        original_pos = ord(char) - ord('A')
                        new_pos = (original_pos + shift_encrypt) % 26
                        new_char = chr(new_pos + ord('A'))
                        st.write(f"{char} (vị trí {original_pos}) → {new_char} (vị trí {new_pos})")
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    with col2:
        st.markdown("#### 🔓 Giải Mã")
        cipher_text = st.text_area("Nhập văn bản cần giải mã:", value="KHOOR ZRUOG", height=100)
        shift_decrypt = st.slider("Chọn shift value:", min_value=1, max_value=25, value=3, key="caesar_decrypt")
        
        if st.button("🔓 Giải Mã Caesar", key="decrypt_caesar"):
            try:
                decrypted = decrypt_caesar(cipher_text, shift_decrypt)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả giải mã:** `{decrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    # Brute Force Attack Demo
    with st.expander("🔥 Demo Tấn Công Brute Force"):
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("""
        **Caesar Cipher rất dễ bị phá vỡ!** Chỉ có 25 khả năng shift, có thể thử tất cả.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        brute_text = st.text_input("Nhập cipher text để tấn công:", value="KHOOR")
        
        if st.button("🔥 Thực Hiện Brute Force"):
            st.markdown("**Tất cả khả năng giải mã:**")
            for shift in range(1, 26):
                result = decrypt_caesar(brute_text, shift)
                st.write(f"Shift {shift:2d}: {result}")

def show_vigenere_cipher():
    """Hiển thị Vigenère Cipher"""
    
    st.markdown('<h2 class="algorithm-header">🗝️ Vigenère Cipher - Mã Hóa Đa Bảng</h2>', unsafe_allow_html=True)
    
    # Lý thuyết
    with st.expander("📚 Lý Thuyết & Nguyên Lý", expanded=True):
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Vigenère Cipher** là phiên bản cải tiến của Caesar Cipher, sử dụng một từ khóa để tạo ra nhiều shift value khác nhau.
        
        **🔬 Nguyên Lý:**
        - Sử dụng một từ khóa (keyword) thay vì một shift cố định
        - Mỗi ký tự trong keyword quyết định shift cho ký tự tương ứng trong plaintext
        - Keyword được lặp lại để khớp với độ dài của plaintext
        - Mỗi ký tự được mã hóa bằng Caesar cipher với shift khác nhau
        
        **📐 Công Thức:**
        - Mã hóa: `C[i] = (P[i] + K[i mod len(K)]) mod 26`
        - Giải mã: `P[i] = (C[i] - K[i mod len(K)] + 26) mod 26`
        
        **🔢 Không gian khóa:** 26^n (n = độ dài keyword)
        **⚡ Độ phức tạp:** O(n) cho mã hóa/giải mã
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mã giả
    with st.expander("💻 Mã Giả (Pseudocode)"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Thuật toán mã hóa Vigenère:**
        ```
        FUNCTION VigenereEncrypt(plaintext, keyword):
            ciphertext = ""
            keyIndex = 0
            
            FOR each character c in plaintext:
                IF c is a letter:
                    base = 'A' if c is uppercase else 'a'
                    keyChar = keyword[keyIndex mod len(keyword)]
                    shift = (keyChar - 'A') if keyChar is uppercase else (keyChar - 'a')
                    
                    encrypted = (c - base + shift) mod 26
                    ciphertext += char(encrypted + base)
                    keyIndex += 1
                ELSE:
                    ciphertext += c  // Giữ nguyên ký tự không phải chữ cái
            
            RETURN ciphertext
        ```
        
        **Thuật toán giải mã Vigenère:**
        ```
        FUNCTION VigenereDecrypt(ciphertext, keyword):
            plaintext = ""
            keyIndex = 0
            
            FOR each character c in ciphertext:
                IF c is a letter:
                    base = 'A' if c is uppercase else 'a'
                    keyChar = keyword[keyIndex mod len(keyword)]
                    shift = (keyChar - 'A') if keyChar is uppercase else (keyChar - 'a')
                    
                    decrypted = (c - base - shift + 26) mod 26
                    plaintext += char(decrypted + base)
                    keyIndex += 1
                ELSE:
                    plaintext += c
            
            RETURN plaintext
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Ví dụ minh họa
    with st.expander("🎯 Ví Dụ Minh Họa & Tính Toán"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Ví dụ với Keyword = "KEY":**
        
        **Bước 1: Lặp lại keyword**
        ```
        Plaintext:  H E L L O
        Keyword:    K E Y K E
        ```
        
        **Bước 2: Chuyển đổi thành số**
        ```
        Plaintext:  7  4  11 11 14
        Keyword:    10 4  24 10 4
        ```
        
        **Bước 3: Cộng và mod 26**
        ```
        Sum:        17 8  35 21 18
        Mod 26:     17 8  9  21 18
        Result:     R  I  J  V  S
        ```
        
        **Chi tiết tính toán cho từng ký tự:**
        - H (7) + K (10) = 17 mod 26 = 17 → R
        - E (4) + E (4) = 8 mod 26 = 8 → I  
        - L (11) + Y (24) = 35 mod 26 = 9 = J
        - L (11) + K (10) = 21 mod 26 = 21 → V
        - O (14) + E (4) = 18 mod 26 = 18 → S
        
        **Vigenère Square (bảng tra cứu):**
        ```
           A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        A  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        B  B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
        C  C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
        ...
        K  K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Phân tích bảo mật
    with st.expander("🔒 Phân Tích Bảo Mật & Phương pháp Tấn công"):
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("""
        **⚠️ Điểm mạnh của Vigenère:**
        
        **1. Chống Frequency Analysis:**
        - Cùng một ký tự có thể được mã hóa thành nhiều ký tự khác nhau
        - Phá vỡ pattern tần suất của Caesar cipher
        
        **2. Không gian khóa lớn:**
        - Với keyword dài n: 26^n khả năng
        - Keyword "SECRET" (6 ký tự): 26^6 = 308,915,776 khả năng
        
        **⚠️ Nhưng vẫn có thể bị tấn công:**
        
        **1. Kasiski Examination:**
        ```
        Tìm các đoạn lặp lại trong ciphertext:
        - "XYZ" xuất hiện ở vị trí 15 và 45
        - Khoảng cách: 45 - 15 = 30
        - Độ dài key có thể là ước của 30: 1,2,3,5,6,10,15,30
        ```
        
        **2. Index of Coincidence:**
        ```
        IC = Σ(fi(fi-1)) / (N(N-1))
        - IC ≈ 0.067 cho tiếng Anh
        - IC ≈ 0.038 cho random text
        - Dùng để xác định độ dài key
        ```
        
        **3. Frequency Analysis cho mỗi Caesar:**
        ```
        Sau khi biết độ dài key = k:
        - Chia ciphertext thành k nhóm
        - Mỗi nhóm là Caesar cipher
        - Áp dụng frequency analysis cho từng nhóm
        ```
        
        **Ví dụ tấn công:**
        ```
        Ciphertext: "RIJVS QYVJN RYBWM..."
        
        1. Tìm pattern lặp: không có → key dài hoặc text ngắn
        2. Thử các độ dài key phổ biến: 3,4,5,6,7,8...
        3. Với key length = 3:
           - Nhóm 1: R, V, Y, ... (vị trí 0,3,6,...)
           - Nhóm 2: I, S, V, ... (vị trí 1,4,7,...)  
           - Nhóm 3: J, Q, J, ... (vị trí 2,5,8,...)
        4. Frequency analysis từng nhóm
        5. Tìm được key: "KEY"
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        ```
        Plaintext:  H E L L O
        Keyword:    K E Y K E
        Shift:      10 4 24 10 4
        Ciphertext: R I J V S Q Y V J N
        ```
        
        **Chi tiết tính toán:**
        - H (7) + K (10) = 17 mod 26 = R
        - E (4) + E (4) = 8 mod 26 = I  
        - L (11) + Y (24) = 35 mod 26 = 9 = J
        - L (11) + K (10) = 21 mod 26 = 21 → V
        - O (14) + E (4) = 18 mod 26 = 18 → S
        
        **Vigenère Square (bảng tra cứu):**
        ```
           A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        A  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        B  B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
        C  C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
        ...
        K  K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Demo tương tác
    st.markdown("### 🎮 Demo Tương Tác")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔐 Mã Hóa")
        vigenere_plain = st.text_area("Nhập văn bản:", value="HELLO WORLD", height=100, key="vigenere_plain")
        vigenere_key = st.text_input("Nhập keyword:", value="KEY", key="vigenere_key_encrypt")
        
        if st.button("🔒 Mã Hóa Vigenère", key="encrypt_vigenere"):
            try:
                encrypted = encrypt_vigenere(vigenere_plain, vigenere_key)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả mã hóa:** `{encrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    with col2:
        st.markdown("#### 🔓 Giải Mã")
        vigenere_cipher = st.text_area("Nhập cipher text:", value="RIJVS QYVJN", height=100, key="vigenere_cipher")
        vigenere_key_decrypt = st.text_input("Nhập keyword:", value="KEY", key="vigenere_key_decrypt")
        
        if st.button("🔓 Giải Mã Vigenère", key="decrypt_vigenere"):
            try:
                decrypted = decrypt_vigenere(vigenere_cipher, vigenere_key_decrypt)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả giải mã:** `{decrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")

def show_playfair_cipher():
    """Hiển thị Playfair Cipher"""
    
    st.markdown('<h2 class="algorithm-header">🎭 Playfair Cipher - Mã Hóa Digraph</h2>', unsafe_allow_html=True)
    
    with st.expander("📚 Lý Thuyết & Nguyên Lý", expanded=True):
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Playfair Cipher** được Charles Wheatstone phát minh năm 1854, phổ biến bởi Lord Playfair. 
        Đây là cipher digraph đầu tiên, mã hóa cặp ký tự thay vì từng ký tự riêng lẻ.
        
        **🔬 Nguyên Lý Hoạt Động:**
        1. **Tạo Key Square 5×5**: Từ keyword, loại bỏ ký tự trùng, I/J coi là một
        2. **Chuẩn bị plaintext**: Chia thành digraphs, chèn 'X' nếu cặp giống nhau
        3. **Áp dụng quy tắc mã hóa** theo vị trí trong ma trận
        
        **📐 Ba Quy Tắc Mã Hóa:**
        - **Cùng hàng**: Dịch phải 1 vị trí (wrap around)
        - **Cùng cột**: Dịch xuống 1 vị trí (wrap around)  
        - **Hình chữ nhật**: Hoán đổi góc đối diện
        
        **⚡ Độ Phức Tạp:**
        - Mã hóa/Giải mã: O(n) với n = độ dài text
        - Key space: 25! ≈ 1.5 × 10^25 (rất lớn)
        - Thực tế: Giảm do cấu trúc ngôn ngữ
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mã giả chi tiết
    with st.expander("💻 Mã Giả & Thuật Toán"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Thuật toán Playfair:**
        ```
        FUNCTION PlayfairEncrypt(plaintext, keyword):
            // Bước 1: Tạo key square 5x5
            key_square = CreateKeySquare(keyword)
            
            // Bước 2: Chuẩn bị plaintext
            digraphs = PrepareText(plaintext)  // Chia thành cặp, xử lý trùng
            
            ciphertext = ""
            FOR each digraph (char1, char2) in digraphs:
                pos1 = FindPosition(char1, key_square)
                pos2 = FindPosition(char2, key_square)
                
                IF pos1.row == pos2.row:  // Cùng hàng
                    cipher1 = key_square[pos1.row][(pos1.col + 1) % 5]
                    cipher2 = key_square[pos2.row][(pos2.col + 1) % 5]
                
                ELSE IF pos1.col == pos2.col:  // Cùng cột
                    cipher1 = key_square[(pos1.row + 1) % 5][pos1.col]
                    cipher2 = key_square[(pos2.row + 1) % 5][pos2.col]
                
                ELSE:  // Hình chữ nhật
                    cipher1 = key_square[pos1.row][pos2.col]
                    cipher2 = key_square[pos2.row][pos1.col]
                
                ciphertext += cipher1 + cipher2
            
            RETURN ciphertext
            
        FUNCTION CreateKeySquare(keyword):
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabet = alphabet.replace('J', '')  // I và J coi là một
            
            key_chars = []
            FOR char in keyword.upper():
                IF char not in key_chars AND char in alphabet:
                    key_chars.append(char)
            
            FOR char in alphabet:
                IF char not in key_chars:
                    key_chars.append(char)
            
            // Tạo ma trận 5x5
            square = [[key_chars[i*5 + j] for j in range(5)] for i in range(5)]
            RETURN square
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Ví dụ chi tiết
    with st.expander("📖 Ví Dụ Chi Tiết"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Ví dụ: Mã hóa "HELLO" với keyword "MONARCHY"**
        
        **Bước 1: Tạo Key Square**
        ```
        Keyword: MONARCHY → M O N A R C H Y (loại trùng)
        Alphabet còn lại: B D E F G I K L P Q S T U V W X Z
        
        Key Square 5×5:
        M  O  N  A  R
        C  H  Y  B  D
        E  F  G  I  K
        L  P  Q  S  T
        U  V  W  X  Z
        ```
        
        **Bước 2: Chuẩn bị plaintext**
        ```
        HELLO → HE, LL, O
        Vì LL trùng → HE, LX, O
        Vì O lẻ → HE, LX, OX
        Digraphs: (H,E), (L,X), (O,X)
        ```
        
        **Bước 3: Mã hóa từng cặp**
        ```
        (H,E): H(1,1), E(2,0) → Hình chữ nhật → C(1,0), F(2,1) = CF
        (L,X): L(3,0), X(4,3) → Hình chữ nhật → S(3,3), V(4,0) = SV  
        (O,X): O(0,1), X(4,3) → Hình chữ nhật → A(0,3), V(4,1) = AV
        ```
        
        **Kết quả: HELLO → CFSVAV**
        
        **Giải mã (tìm K⁻¹):**
        ```
        det(K) = 11, det⁻¹ ≡ 19 (mod 26)  // 11×19 ≡ 1 (mod 26)
        
        K⁻¹ = 19 × [[7, -5],    = [[7×19, -5×19],    ≡ [[133, -95],
                    [-2, 3]]        [-2×19, 3×19]]       [-38, 57]]
                                                       ≡ [[3, 9],
                                                          [14, 5]] (mod 26)
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Phân tích bảo mật
    with st.expander("🔒 Phân Tích Bảo Mật"):
        st.markdown('<div class="security-box">', unsafe_allow_html=True)
        st.markdown("""
        **👍 Ưu Điểm:**
        - **Khắc phục frequency analysis**: Mã hóa digraph làm phức tạp phân tích tần suất
        - **Key space lớn**: 25! khả năng lý thuyết
        - **Đơn giản**: Dễ thực hiện thủ công, không cần máy tính
        - **Lịch sử**: Được quân đội Anh sử dụng trong WWI
        
        **👎 Nhược Điểm:**
        - **Digraph frequency**: Vẫn có thể phân tích tần suất digraph
        - **Key structure**: Key square giảm entropy thực tế
        - **Cấu trúc ngôn ngữ**: Một số digraph phổ biến (TH, HE, IN...)
        - **Cryptanalysis**: Có thể bị phá bằng hill climbing, genetic algorithms
        
        **🎯 Phương Pháp Tấn Công:**
        1. **Frequency Analysis**: Phân tích tần suất digraph
        2. **Known Plaintext**: Biết một phần plaintext
        3. **Brute Force**: Với key ngắn
        4. **Pattern Analysis**: Tìm patterns trong ciphertext
        
        **📊 Đánh Giá:**
        - **Độ bảo mật**: Thấp (theo tiêu chuẩn hiện đại)
        - **Tốc độ**: Nhanh (thủ công hoặc máy tính)
        - **Ứng dụng**: Giáo dục, demo lịch sử
        - **Thay thế**: Sử dụng AES cho ứng dụng thực tế
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Demo tương tác
    st.markdown("### 🎮 Demo Tương Tác")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔐 Mã Hóa")
        playfair_plain = st.text_area("Nhập văn bản:", value="HELLO", height=100, key="playfair_plain")
        playfair_key = st.text_input("Nhập keyword:", value="MONARCHY", key="playfair_key_encrypt")
        
        if st.button("🔒 Mã Hóa Playfair", key="encrypt_playfair"):
            try:
                encrypted = encrypt_playfair(playfair_plain, playfair_key)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả mã hóa:** `{encrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    with col2:
        st.markdown("#### 🔓 Giải Mã")
        playfair_cipher = st.text_area("Nhập cipher text:", height=100, key="playfair_cipher")
        playfair_key_decrypt = st.text_input("Nhập keyword:", value="MONARCHY", key="playfair_key_decrypt")
        
        if st.button("🔓 Giải Mã Playfair", key="decrypt_playfair"):
            try:
                decrypted = decrypt_playfair(playfair_cipher, playfair_key_decrypt)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả giải mã:** `{decrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")

def show_hill_cipher():
    """Hiển thị Hill Cipher"""
    
    st.markdown('<h2 class="algorithm-header">🧮 Hill Cipher - Mã Hóa Ma Trận</h2>', unsafe_allow_html=True)
    
    with st.expander("📚 Lý Thuyết & Nguyên Lý", expanded=True):
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Hill Cipher** được Lester S. Hill phát minh năm 1929, là cipher đầu tiên áp dụng 
        đại số tuyến tính và ma trận vào mã hóa.
        
        **🔬 Nguyên Lý Hoạt Động:**
        - Sử dụng ma trận khóa K kích thước n×n (thường 2×2 hoặc 3×3)
        - Chia plaintext thành các vector có n phần tử
        - **Mã hóa**: C = K × P (mod 26)
        - **Giải mã**: P = K⁻¹ × C (mod 26)
        
        **⚠️ Điều Kiện Ma Trận Khóa:**
        - Ma trận phải khả nghịch trong Z₂₆
        - det(K) ≠ 0 và gcd(det(K), 26) = 1
        - Chỉ có 157,248 ma trận 2×2 hợp lệ trong Z₂₆
        
        **⚡ Độ Phức Tạp:**
        - Mã hóa/Giải mã: O(n³) cho việc tính ma trận nghịch đảo
        - Key space (2×2): ~1.6 × 10⁵ ma trận hợp lệ
        - Vulnerability: Known plaintext attack
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mã giả chi tiết
    with st.expander("💻 Mã Giả & Thuật Toán"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Thuật toán Hill Cipher (2×2):**
        ```
        FUNCTION HillEncrypt(plaintext, key_matrix):
            // Bước 1: Kiểm tra ma trận khóa
            det = Determinant(key_matrix) mod 26
            IF gcd(det, 26) != 1:
                RETURN "Invalid key matrix"
            
            // Bước 2: Chuẩn bị plaintext
            text = plaintext.upper().replace(non_alpha, "")
            IF len(text) % 2 != 0:
                text += 'X'  // Padding
            
            ciphertext = ""
            FOR i = 0 to len(text) step 2:
                // Vector plaintext
                P = [char_to_num(text[i]), char_to_num(text[i+1])]
                
                // Nhân ma trận: C = K × P (mod 26)
                C[0] = (key_matrix[0][0] * P[0] + key_matrix[0][1] * P[1]) % 26
                C[1] = (key_matrix[1][0] * P[0] + key_matrix[1][1] * P[1]) % 26
                
                ciphertext += num_to_char(C[0]) + num_to_char(C[1])
            
            RETURN ciphertext
            
        FUNCTION HillDecrypt(ciphertext, key_matrix):
            // Tìm ma trận nghịch đảo
            inv_matrix = MatrixInverse(key_matrix, 26)
            
            // Sử dụng ma trận nghịch đảo để giải mã
            RETURN HillEncrypt(ciphertext, inv_matrix)
            
        FUNCTION MatrixInverse(matrix, mod):
            det = Determinant(matrix) % mod
            det_inv = ModularInverse(det, mod)
            
            // Với ma trận 2×2: [[a,b],[c,d]]
            // Nghịch đảo: (1/det) * [[d,-b],[-c,a]]
            inv = [[matrix[1][1], -matrix[0][1]], 
                   [-matrix[1][0], matrix[0][0]]]
            
            FOR i, j in range(2):
                inv[i][j] = (inv[i][j] * det_inv) % mod
            
            RETURN inv
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Ví dụ chi tiết
    with st.expander("📖 Ví Dụ Chi Tiết"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Ví dụ: Mã hóa "HELLO" với key matrix [[3,5],[2,7]]**
        
        **Bước 1: Kiểm tra ma trận khóa**
        ```
        K = [[3, 5],     det(K) = 3×7 - 5×2 = 21 - 10 = 11
             [2, 7]]     gcd(11, 26) = 1 ✓ (Hợp lệ)
        ```
        
        **Bước 2: Chuẩn bị plaintext**
        ```
        "HELLO" → HE LL O → HE LL OX (padding)
        H=7, E=4, L=11, L=11, O=14, X=23
        ```
        
        **Bước 3: Mã hóa từng cặp**
        ```
        Cặp 1: HE → [7, 4]
        C = K × P = [[3,5],[2,7]] × [7,4] = [(3×7+5×4), (2×7+7×4)]
                  = [21+20, 14+28] = [41, 42] ≡ [15, 16] (mod 26)
                  = PQ
        
        Cặp 2: LL → [11, 11]
        C = K × P = [[3,5],[2,7]] × [11,11] = [(3×11+5×11), (2×11+7×11)]
                  = [33+55, 22+77] = [88, 99] ≡ [10, 21] (mod 26)
                  = KV
        
        Cặp 3: OX → [14, 23]
        C = K × P = [[3,5],[2,7]] × [14,23] = [(3×14+5×23), (2×14+7×23)]
                  = [42+115, 28+161] = [157, 189] ≡ [1, 7] (mod 26)
                  = BH
        ```
        
        **Kết quả: HELLO → PQKVBH**
        
        **Giải mã (tìm K⁻¹):**
        ```
        det(K) = 11, det⁻¹ ≡ 19 (mod 26)  // 11×19 ≡ 1 (mod 26)
        
        K⁻¹ = 19 × [[7, -5],    = [[7×19, -5×19],    ≡ [[133, -95],
                    [-2, 3]]        [-2×19, 3×19]]       [-38, 57]]
                                                       ≡ [[3, 9],
                                                          [14, 5]] (mod 26)
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Phân tích bảo mật
    with st.expander("🔒 Phân Tích Bảo Mật"):
        st.markdown('<div class="security-box">', unsafe_allow_html=True)
        st.markdown("""
        **👍 Ưu Điểm:**
        - **Toán học chặt chẽ**: Dựa trên đại số tuyến tính
        - **Khó frequency analysis**: Một ký tự có thể mã hóa thành nhiều ký tự khác
        - **Tốc độ**: Nhanh với ma trận nhỏ
        - **Tính khả nghịch**: Đảm bảo giải mã chính xác
        
        **👎 Nhược Điểm:**
        - **Known plaintext attack**: Cần 2n ký tự để phá ma trận n×n
        - **Key space hạn chế**: Chỉ ~157K ma trận 2×2 hợp lệ
        - **Linearity**: Bảo toàn tính tuyến tính của plaintext
        - **Zero divisors**: Các ma trận không khả nghịch
        
        **🎯 Phương Pháp Tấn Công:**
        1. **Known Plaintext**: 
           - Biết 4 ký tự plaintext-ciphertext → Tìm được ma trận khóa
           - P₁C₁ = K, solve for K
        
        2. **Chosen Plaintext**: 
           - Chọn plaintext đặc biệt (như đơn vị ma trận)
           - Dễ dàng xác định ma trận khóa
        
        3. **Brute Force**: 
           - Thử tất cả ma trận khả nghịch
           - Khả thi với ma trận 2×2
        
        4. **Frequency Analysis** (nâng cao):
           - Phân tích n-gram patterns
           - Tìm cấu trúc lặp lại
        
        **📊 Đánh Giá:**
        - **Độ bảo mật**: Thấp - Trung bình (tùy kích thước ma trận)
        - **Tốc độ**: Nhanh (O(n³) cho ma trận n×n)
        - **Ứng dụng**: Giáo dục, demo toán học
        - **Thay thế**: AES, RSA cho ứng dụng thực tế
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Demo tương tác
    st.markdown("### 🎮 Demo Tương Tác")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔐 Mã Hóa")
        hill_plain = st.text_area("Nhập văn bản:", value="HELLO", height=100, key="hill_plain")
        
        st.markdown("**Ma trận khóa 2x2:**")
        col1_1, col1_2 = st.columns(2)
        with col1_1:
            k11 = st.number_input("K[0,0]:", value=3, key="k11")
            k21 = st.number_input("K[1,0]:", value=2, key="k21")
        with col1_2:
            k12 = st.number_input("K[0,1]:", value=5, key="k12")
            k22 = st.number_input("K[1,1]:", value=7, key="k22")
        
        key_matrix = [[k11, k12], [k21, k22]]
        
        if st.button("🔒 Mã Hóa Hill", key="encrypt_hill"):
            try:
                encrypted = encrypt_hill(hill_plain, key_matrix)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả mã hóa:** `{encrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    with col2:
        st.markdown("#### 🔓 Giải Mã")
        hill_cipher = st.text_area("Nhập cipher text:", height=100, key="hill_cipher")
        
        # Sử dụng cùng ma trận khóa
        if st.button("🔓 Giải Mã Hill", key="decrypt_hill"):
            try:
                decrypted = decrypt_hill(hill_cipher, key_matrix)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả giải mã:** `{decrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")

def show_polyalphabetic_cipher():
    """Hiển thị Polyalphabetic Cipher"""
    
    st.markdown('<h2 class="algorithm-header">🔀 Polyalphabetic Cipher - Mã Hóa Đa Bảng Nâng Cao</h2>', unsafe_allow_html=True)
    
    with st.expander("📚 Lý Thuyết & Nguyên Lý", expanded=True):
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Polyalphabetic Cipher** sử dụng nhiều bảng chữ cái thay thế khác nhau, 
        khắc phục nhược điểm frequency analysis của monoalphabetic ciphers.
        
        **🔬 Nguyên Lý Hoạt Động:**
        - Sử dụng nhiều Caesar cipher với các shift khác nhau
        - Keyword xác định sequence các shift
        - Mỗi ký tự plaintext sử dụng shift khác nhau
        - Lặp lại keyword khi hết độ dài
        
        **🎯 Đặc Điểm:**
        - **Multiple substitutions**: Một ký tự có thể mã hóa thành nhiều ký tự khác
        - **Period**: Độ dài keyword quyết định chu kỳ lặp
        - **Frequency flattening**: Làm phẳng phân bố tần suất
        - **Key dependency**: Bảo mật phụ thuộc vào keyword
        
        **⚡ Độ Phức Tạp:**
        - Mã hóa/Giải mã: O(n) với n = độ dài text
        - Key space: 26^k với k = độ dài keyword
        - Cryptanalysis: O(26^k) brute force
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mã giả chi tiết
    with st.expander("💻 Mã Giả & Thuật Toán"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Thuật toán Polyalphabetic:**
        ```
        FUNCTION PolyalphabeticEncrypt(plaintext, keyword):
            ciphertext = ""
            keyword = keyword.upper()
            key_index = 0
            
            FOR each char c in plaintext.upper():
                IF c is alphabetic:
                    // Tính shift từ keyword
                    shift = char_to_num(keyword[key_index % len(keyword)])
                    
                    // Áp dụng Caesar cipher với shift này
                    encrypted_char = ((char_to_num(c) + shift) % 26)
                    ciphertext += num_to_char(encrypted_char)
                    
                    key_index += 1  // Chỉ tăng với ký tự alphabetic
                ELSE:
                    ciphertext += c  // Giữ nguyên ký tự không alphabetic
            
            RETURN ciphertext
            
        FUNCTION PolyalphabeticDecrypt(ciphertext, keyword):
            plaintext = ""
            keyword = keyword.upper()
            key_index = 0
            
            FOR each char c in ciphertext.upper():
                IF c is alphabetic:
                    // Tính shift từ keyword
                    shift = char_to_num(keyword[key_index % len(keyword)])
                    
                    // Áp dụng Caesar decrypt với shift này
                    decrypted_char = ((char_to_num(c) - shift) % 26)
                    plaintext += num_to_char(decrypted_char)
                    
                    key_index += 1
                ELSE:
                    plaintext += c
            
            RETURN plaintext
            
        FUNCTION char_to_num(char):
            RETURN ord(char) - ord('A')  // A=0, B=1, ..., Z=25
            
        FUNCTION num_to_char(num):
            RETURN chr(num + ord('A'))
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Ví dụ chi tiết
    with st.expander("📖 Ví Dụ Chi Tiết"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Ví dụ: Mã hóa "HELLO WORLD" với keyword "SECRET"**
        
        **Bước 1: Chuẩn bị**
        ```
        Plaintext:  H E L L O   W O R L D
        Keyword:    S E C R E   T S E C R  (lặp lại)
        ```
        
        **Bước 2: Tính shift cho từng ký tự**
        ```
        S = 18, E = 4, C = 2, R = 17, E = 4, T = 19
        
        Keyword repeat: S E C R E T S E C R E
        Shifts:        18 4 2 17 4 19 18 4 2 17 4
        ```
        
        **Bước 3: Áp dụng Caesar cho từng ký tự**
        ```
        H (7)  + S (18) = 25 mod 26 = Z
        E (4)  + E (4)  = 8  mod 26 = I
        L (11) + C (2)  = 13 mod 26 = N
        L (11) + R (17) = 28 mod 26 = 2 = C
        O (14) + E (4)  = 18 mod 26 = S
        (space - bỏ qua)
        W (22) + T (19) = 41 mod 26 = 15 = P
        O (14) + S (18) = 32 mod 26 = 6  = G
        R (17) + E (4)  = 21 mod 26 = V
        L (11) + C (2)  = 13 mod 26 = N
        D (3)  + R (17) = 20 mod 26 = U
        ```
        
        **Kết quả: "HELLO WORLD" → "ZINCS PGVNU"**
        
        **So sánh với Caesar đơn giản:**
        ```
        Caesar (shift=1): "HELLO WORLD" → "IFMMP XPSME"
        Polyalphabetic:   "HELLO WORLD" → "ZINCS PGVNU"
        
        → Cùng ký tự 'L' được mã hóa thành 'N' và 'C' khác nhau!
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Phân tích bảo mật
    with st.expander("🔒 Phân Tích Bảo Mật"):
        st.markdown('<div class="security-box">', unsafe_allow_html=True)
        st.markdown("""
        **👍 Ưu Điểm:**
        - **Khắc phục frequency analysis**: Một ký tự mã hóa thành nhiều ký tự khác
        - **Flexibility**: Có thể sử dụng keyword dài để tăng bảo mật
        - **Implementation**: Đơn giản, dựa trên Caesar cipher
        - **Historical success**: Enigma machine sử dụng nguyên lý tương tự
        
        **👎 Nhược Điểm:**
        - **Key repetition**: Keyword lặp lại tạo ra patterns
        - **Kasiski examination**: Phân tích khoảng cách lặp lại
        - **Index of coincidence**: Xác định độ dài keyword
        - **Short keys**: Keyword ngắn dễ bị phá
        
        **🎯 Phương Pháp Tấn Công:**
        
        1. **Kasiski Examination:**
           - Tìm chuỗi lặp lại trong ciphertext
           - Tính khoảng cách giữa các lần lặp
           - GCD của các khoảng cách → độ dài keyword
        
        2. **Index of Coincidence (IC):**
           - Đo độ trùng lặp ký tự trong text
           - IC ≈ 0.065 (tiếng Anh), IC ≈ 0.038 (random)
           - Thử các độ dài key, chọn IC gần 0.065 nhất
        
        3. **Frequency Analysis per position:**
           - Sau khi biết độ dài key
           - Phân tích tần suất cho từng vị trí trong chu kỳ
           - Áp dụng frequency analysis cho từng sub-cipher
        
        4. **Dictionary Attack:**
           - Thử các từ phổ biến làm keyword
           - Kiểm tra plaintext có nghĩa không
        
        **📊 Đánh Giá:**
        - **Độ bảo mật**: Trung bình (phụ thuộc độ dài key)
        - **Tốc độ**: Nhanh O(n)
        - **Ứng dụng**: Giáo dục, demo lịch sử
        - **Cải tiến**: One-time pad, Stream ciphers hiện đại
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Demo tương tác
    st.markdown("### 🎮 Demo Tương Tác")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔐 Mã Hóa")
        poly_plain = st.text_area("Nhập văn bản:", value="HELLO WORLD", height=100, key="poly_plain")
        poly_key = st.text_input("Nhập keyword:", value="SECRET", key="poly_key_encrypt")
        
        if st.button("🔒 Mã Hóa Polyalphabetic", key="encrypt_poly"):
            try:
                encrypted = encrypt_polyalphabetic(poly_plain, poly_key)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả mã hóa:** `{encrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    with col2:
        st.markdown("#### 🔓 Giải Mã")
        poly_cipher = st.text_area("Nhập cipher text:", height=100, key="poly_cipher")
        poly_key_decrypt = st.text_input("Nhập keyword:", value="SECRET", key="poly_key_decrypt")
        
        if st.button("🔓 Giải Mã Polyalphabetic", key="decrypt_poly"):
            try:
                decrypted = decrypt_polyalphabetic(poly_cipher, poly_key_decrypt)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả giải mã:** `{decrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")

def show_permutation_cipher():
    """Hiển thị Permutation Cipher"""
    
    st.markdown('<h2 class="algorithm-header">🔄 Permutation Cipher - Mã Hóa Hoán Vị</h2>', unsafe_allow_html=True)
    
    # Demo tương tác
    st.markdown("### 🎮 Demo Tương Tác")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔐 Mã Hóa")
        perm_plain = st.text_area("Nhập văn bản:", value="HELLO WORLD", height=100, key="perm_plain")
        perm_key = st.text_input("Nhập key (số):", value="3142", key="perm_key_encrypt")
        
        if st.button("🔒 Mã Hóa Permutation", key="encrypt_perm"):
            try:
                encrypted = encrypt_permutation(perm_plain, perm_key)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả mã hóa:** `{encrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    with col2:
        st.markdown("#### 🔓 Giải Mã")
        perm_cipher = st.text_area("Nhập cipher text:", height=100, key="perm_cipher")
        perm_key_decrypt = st.text_input("Nhập key (số):", value="3142", key="perm_key_decrypt")
        
        if st.button("🔓 Giải Mã Permutation", key="decrypt_perm"):
            try:
                decrypted = decrypt_permutation(perm_cipher, perm_key_decrypt)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả giải mã:** `{decrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")

def show_des_cipher():
    """Hiển thị DES Cipher với thông tin chi tiết"""
    
    st.markdown('<h2 class="algorithm-header">🏢 DES - Data Encryption Standard</h2>', unsafe_allow_html=True)
    
    with st.expander("📚 Lý Thuyết & Nguyên Lý", expanded=True):
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **DES (Data Encryption Standard)** là thuật toán mã hóa khối đối xứng được IBM phát triển và NIST công nhận năm 1977.
        
        **🔬 Đặc Điểm Kỹ Thuật:**
        - **Block size**: 64-bit (8 bytes)
        - **Key size**: 56-bit hiệu dụng (64-bit với 8 parity bits)
        - **Structure**: Feistel Network với 16 rounds
        - **Algorithm type**: Symmetric block cipher
        
        **🏗️ Cấu Trúc DES:**
        1. **Initial Permutation (IP)**: Hoán vị đầu vào
        2. **16 Feistel Rounds**: Mỗi round sử dụng hàm F
        3. **Final Permutation (FP)**: Hoán vị cuối cùng (IP⁻¹)
        
        **⚙️ Feistel Network:**
        - Chia 64-bit thành 2 nửa: L₀, R₀ (mỗi nửa 32-bit)
        - Mỗi round: L_{i+1} = R[i], R_{i+1} = L[i] ⊕ F(R[i], K[i])
        
        **🔑 Key Schedule:**
        - Master key 64-bit → 56-bit (loại bỏ parity)
        - Tạo 16 round keys, mỗi key 48-bit
        - Sử dụng PC-1, PC-2 và left circular shifts
        
        **⚡ Độ Phức Tạp:**
        - Mã hóa/Giải mã: O(1) (số rounds cố định)
        - Brute force: 2^56 ≈ 7.2 × 10^16 operations
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mã giả
    with st.expander("💻 Mã Giả & Cấu Trúc Chi Tiết"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Thuật toán DES chính:**
        ```
        FUNCTION DES_Encrypt(plaintext_64bit, key_64bit):
            // Key Schedule
            round_keys = GenerateRoundKeys(key_64bit)  // 16 keys × 48-bit
            
            // Initial Permutation
            data = InitialPermutation(plaintext_64bit)
            L0 = data[0:31]    // Left 32 bits
            R0 = data[32:63]   // Right 32 bits
            
            // 16 Feistel Rounds
            FOR i = 0 to 15:
                L[i+1] = R[i]
                R[i+1] = L[i] XOR F(R[i], K[i])
            
            // Final step
            combined = R16 || L16  // Swap and combine
            ciphertext = FinalPermutation(combined)
            RETURN ciphertext
        ```
        
        **Hàm F (Core Function):**
        ```
        FUNCTION F(right_32bit, round_key_48bit):
            // 1. Expansion: 32-bit → 48-bit
            expanded = Expansion(right_32bit)
            
            // 2. XOR with round key
            xored = expanded XOR round_key_48bit
            
            // 3. S-boxes substitution: 48-bit → 32-bit
            // Chia thành 8 nhóm 6-bit, mỗi nhóm qua 1 S-box
            output_32bit = ""
            FOR i = 0 to 7:
                group_6bit = xored[i*6:(i+1)*6]
                row = group_6bit[0] || group_6bit[5]  // 2-bit
                col = group_6bit[1:4]                 // 4-bit
                s_value = S_BOX[i][row][col]          // 4-bit output
                output_32bit += s_value
            
            // 4. Permutation
            result = Permutation(output_32bit)
            RETURN result
        ```
        
        **Key Schedule:**
        ```
        FUNCTION GenerateRoundKeys(master_key_64bit):
            // 1. PC-1: Remove parity bits (64→56)
            key_56bit = PC1_Permutation(master_key_64bit)
            
            // 2. Split into two 28-bit halves
            C0 = key_56bit[0:27]
            D0 = key_56bit[28:55]
            
            round_keys = []
            FOR i = 0 to 15:
                // 3. Left circular shift
                C[i+1] = LeftShift(C[i], shift_amounts[i])
                D[i+1] = LeftShift(D[i], shift_amounts[i])
                
                // 4. PC-2: Generate 48-bit round key
                combined = C[i+1] || D[i+1]
                round_key = PC2_Permutation(combined)
                round_keys.append(round_key)
            
            RETURN round_keys
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Ví dụ chi tiết
    with st.expander("🎯 Ví Dụ Minh Họa & Tính Toán"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Ví dụ với "HELLO123" và key "MYSECRET":**
        
        **Bước 1: Chuyển đổi sang binary**
        ```
        Plaintext "HELLO123":
        H: 01001000, E: 01100101, L: 01101100, L: 01101100
        O: 01101111, 1: 00110001, 2: 00110010, 3: 00110011
        
        Key "MYSECRET":
        M: 01001101, Y: 01011001, S: 01010011, E: 01100101
        C: 01000011, R: 01010010, E: 01100101, T: 01010100
        ```
        
        **Bước 2: Initial Permutation**
        ```
        Input:  01001000 01100101 01101100 01101100 01101111 00110001 00110010 00110011
        IP:     (hoán vị theo bảng IP)
        Output: L0 (32-bit) || R0 (32-bit)
        ```
        
        **Bước 3: Round 1 Example**
        ```
        R0 (32-bit) → Expansion → 48-bit
        48-bit ⊕ RoundKey1 (48-bit) → 48-bit
        48-bit → 8 S-boxes → 32-bit
        32-bit → Permutation → 32-bit
        
        L1 = R0
        R1 = L0 ⊕ F(R0, K1)
        ```
        
        **Kết quả cuối:**
        ```
        Sau 16 rounds: L16, R16
        Swap: R16 || L16
        Final Permutation → Ciphertext
        Hex format: 051C1F090C637767
        ```
        
        **Các thành phần quan trọng:**
        - **S-boxes**: 8 bảng 4×16, cung cấp tính phi tuyến
        - **Permutations**: Trộn lẫn bits để tăng diffusion
        - **Key schedule**: Đảm bảo mỗi round dùng key khác nhau
        - **Feistel structure**: Cho phép encrypt = decrypt với round keys ngược
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Phân tích bảo mật
    with st.expander("🔒 Phân Tích Bảo Mật & Lịch Sử"):
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("""
        **📈 Lịch Sử DES:**
        
        **1973-1977**: IBM phát triển và NIST chuẩn hóa
        **1977-1999**: Tiêu chuẩn chính thức của Mỹ
        **1998**: DES Challenge III - bị phá trong 56 giờ
        **2001**: AES thay thế DES chính thức
        
        **💪 Điểm Mạnh (thời kỳ 1977-1990):**
        
        **1. Thiết kế vững chắc:**
        - S-boxes được thiết kế chống differential cryptanalysis
        - Feistel structure đảm bảo encrypt/decrypt symmetric
        - Avalanche effect: 1 bit thay đổi → ~50% output thay đổi
        
        **2. Đã được kiểm tra kỹ lưỡng:**
        - Hàng triệu năm nghiên cứu và phân tích
        - Không có backdoor được phát hiện
        - Thiết kế influence nhiều cipher sau này
        
        **⚠️ Điểm Yếu (hiện tại):**
        
        **1. Key size quá nhỏ (56-bit):**
        ```
        1998: EFF DES Cracker - 56 giờ
        2006: COPACOBANA - 9 ngày với $10,000
        2008: Máy tính hiện đại - vài giờ
        2025: Cloud computing - vài phút
        ```
        
        **2. Block size nhỏ (64-bit):**
        - Birthday attack sau 2^32 blocks
        - Không phù hợp cho dữ liệu lớn
        
        **3. Các tấn công đã biết:**
        - **Brute Force**: 2^56 operations (khả thi)
        - **Linear Cryptanalysis**: 2^43 plaintexts
        - **Differential Cryptanalysis**: 2^47 plaintexts
        - **Meet-in-the-middle**: Tấn công 2DES
        
        **🛡️ Biện pháp cải thiện (đã lỗi thời):**
        
        **3DES (Triple DES):**
        ```
        Encrypt(Decrypt(Encrypt(plaintext, K1), K2), K3)
        Key length: 168-bit (hiệu dụng ~112-bit)
        Chậm hơn DES 3 lần
        Vẫn block size 64-bit
        ```
        
        **⚡ Thay thế hiện đại:**
        - **AES**: 128/192/256-bit key, 128-bit block
        - **ChaCha20**: Stream cipher, 256-bit key
        - **Post-quantum**: Chuẩn bị cho tương lai
        
        **📚 Giá trị giáo dục:**
        - Hiểu nguyên lý mã hóa khối
        - Học cấu trúc Feistel
        - Nhận biết tầm quan trọng của key size
        - Lịch sử phát triển cryptography
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Demo tương tác
    st.markdown("### 🎮 Demo Tương Tác")
    
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **🎓 Lưu ý Giáo Dục:** Demo này sử dụng phiên bản đơn giản hóa của DES cho mục đích học tập.
    DES thực tế phức tạp hơn với đầy đủ 16 rounds, S-boxes, và permutations.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔐 Mã Hóa")
        des_plain = st.text_area("Nhập văn bản:", value="HELLO123", height=100, key="des_plain")
        des_key = st.text_input("Nhập key (8 ký tự):", value="MYSECRET", key="des_key_encrypt")
        
        if st.button("🔒 Mã Hóa DES", key="encrypt_des"):
            try:
                encrypted = encrypt_des(des_plain, des_key)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả mã hóa (Hex):** `{encrypted}`")
                
                # Hiển thị thông tin bổ sung
                st.markdown("**Thông tin chi tiết:**")
                st.write(f"- Input length: {len(des_plain)} ký tự")
                st.write(f"- Key length: {len(des_key)} ký tự")
                st.write(f"- Output length: {len(encrypted)} hex chars")
                st.write(f"- Hex → {len(encrypted)//2} bytes")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    with col2:
        st.markdown("#### 🔓 Giải Mã")
        des_cipher = st.text_area("Nhập cipher text (hex):", value="051C1F090C637767", height=100, key="des_cipher")
        des_key_decrypt = st.text_input("Nhập key (8 ký tự):", value="MYSECRET", key="des_key_decrypt")
        
        if st.button("🔓 Giải Mã DES", key="decrypt_des"):
            try:
                decrypted = decrypt_des(des_cipher, des_key_decrypt)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả giải mã:** `{decrypted}`")
                
                # Kiểm tra tính chính xác
                if des_plain and decrypted == des_plain:
                    st.success("✅ Giải mã chính xác!")
                elif des_plain:
                    st.warning("⚠️ Kết quả khác với input ban đầu")
                    
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    # Thống kê so sánh
    with st.expander("📊 So Sánh với Các Thuật Toán Khác"):
        comparison_data = {
            "Thuật Toán": ["Caesar", "Vigenère", "Playfair", "Hill", "DES", "AES"],
            "Năm": ["-50", "1553", "1854", "1929", "1977", "2001"],
            "Key Size": ["5 bit", "Variable", "Variable", "Variable", "56 bit", "128/192/256 bit"],
            "Block Size": ["1 char", "1 char", "2 char", "n char", "64 bit", "128 bit"],
            "Bảo Mật": ["Rất yếu", "Yếu", "Yếu", "Trung bình", "Yếu (hiện tại)", "Mạnh"],
            "Tốc Độ": ["Rất nhanh", "Nhanh", "Trung bình", "Chậm", "Chậm", "Nhanh"],
            "Ứng Dụng": ["Giáo dục", "Lịch sử", "Lịch sử", "Học thuật", "Lịch sử", "Hiện tại"]
        }
        
        import pandas as pd
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    main()
