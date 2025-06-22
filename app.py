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
        
        **📐 Công Thức Toán Học:**
        - Mã hóa: `E(x) = (x + k) mod 26`
        - Giải mã: `D(x) = (x - k) mod 26`
        
        Trong đó: x = vị trí ký tự (A=0, B=1, ..., Z=25), k = shift value
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Ví dụ minh họa
    with st.expander("🎯 Ví Dụ Minh Họa"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Ví dụ với Shift = 3:**
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
        
        **📐 Công Thức:**
        - Mã hóa: `C[i] = (P[i] + K[i mod len(K)]) mod 26`
        - Giải mã: `P[i] = (C[i] - K[i mod len(K)]) mod 26`
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Ví dụ minh họa
    with st.expander("🎯 Ví Dụ Minh Họa"):
        st.markdown('<div class="example-box">', unsafe_allow_html=True)
        st.markdown("""
        **Ví dụ với Keyword = "KEY":**
        ```
        Plaintext:  H E L L O W O R L D
        Keyword:    K E Y K E Y K E Y K
        Shift:      10 4 24 10 4 24 10 4 24 10
        Ciphertext: R I J V S Q Y V J N
        ```
        
        **Chi tiết tính toán:**
        - H (7) + K (10) = 17 mod 26 = R
        - E (4) + E (4) = 8 mod 26 = I  
        - L (11) + Y (24) = 35 mod 26 = 9 = J
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
        **Playfair Cipher** mã hóa cặp ký tự (digraph) thay vì từng ký tự đơn lẻ, làm tăng độ bảo mật.
        
        **🔬 Nguyên Lý:**
        1. Tạo ma trận 5x5 từ keyword (loại bỏ ký tự trùng, I/J được coi là một)
        2. Chia plaintext thành các cặp ký tự
        3. Áp dụng quy tắc mã hóa theo vị trí trong ma trận
        
        **📐 Quy Tắc Mã Hóa:**
        - Cùng hàng: Dịch phải 1 vị trí
        - Cùng cột: Dịch xuống 1 vị trí  
        - Khác hàng & cột: Tạo hình chữ nhật, hoán đổi góc
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
        **Hill Cipher** sử dụng đại số tuyến tính và ma trận để mã hóa.
        
        **🔬 Nguyên Lý:**
        - Sử dụng ma trận khóa K kích thước n×n
        - Chia plaintext thành các vector có n phần tử
        - Mã hóa: C = K × P (mod 26)
        - Giải mã: P = K⁻¹ × C (mod 26)
        
        **⚠️ Lưu Ý:**
        - Ma trận khóa phải khả nghịch (determinant ≠ 0 và gcd(det, 26) = 1)
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
    """Hiển thị DES Cipher"""
    
    st.markdown('<h2 class="algorithm-header">🏢 DES - Data Encryption Standard</h2>', unsafe_allow_html=True)
    
    with st.expander("📚 Lý Thuyết & Nguyên Lý", expanded=True):
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **DES (Data Encryption Standard)** là thuật toán mã hóa khối đối xứng được phát triển bởi IBM và được NIST công nhận năm 1977.
        
        **🔬 Đặc Điểm:**
        - Mã hóa khối 64-bit với khóa 56-bit
        - Sử dụng cấu trúc Feistel Network với 16 round
        - Bao gồm các thành phần: S-boxes, P-boxes, và key schedule
        
        **⚠️ Tình Trạng Hiện Tại:**
        - Không còn an toàn do khóa quá ngắn (56-bit)
        - Đã bị thay thế bởi AES từ năm 2001
        - Chỉ sử dụng cho mục đích học tập và hiểu lịch sử mã hóa
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Demo tương tác
    st.markdown("### 🎮 Demo Tương Tác")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔐 Mã Hóa")
        des_plain = st.text_area("Nhập văn bản:", value="HELLO123", height=100, key="des_plain")
        des_key = st.text_input("Nhập key (8 ký tự):", value="MYSECRET", key="des_key_encrypt")
        
        if st.button("🔒 Mã Hóa DES", key="encrypt_des"):
            try:
                encrypted = encrypt_des(des_plain, des_key)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả mã hóa:** `{encrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    
    with col2:
        st.markdown("#### 🔓 Giải Mã")
        des_cipher = st.text_area("Nhập cipher text:", height=100, key="des_cipher")
        des_key_decrypt = st.text_input("Nhập key (8 ký tự):", value="MYSECRET", key="des_key_decrypt")
        
        if st.button("🔓 Giải Mã DES", key="decrypt_des"):
            try:
                decrypted = decrypt_des(des_cipher, des_key_decrypt)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown(f"**Kết quả giải mã:** `{decrypted}`")
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
