# 🔐 Cryptography Education Web App

Ứng dụng web giáo dục về các thuật toán mã hóa được xây dựng bằng Python/Streamlit.

## 🚀 Demo Live

**Web App**: [Streamlit Cloud URL của bạn]

## 📋 Tính Năng

- 🔤 **Caesar Cipher** - Mã hóa dịch chuyển cổ điển
- 🗝️ **Vigenère Cipher** - Mã hóa đa bảng chữ cái
- 🎭 **Playfair Cipher** - Mã hóa cặp ký tự (digraph)
- 🧮 **Hill Cipher** - Mã hóa ma trận tuyến tính
- 🔀 **Polyalphabetic Cipher** - Mã hóa đa Caesar
- 🔄 **Permutation Cipher** - Mã hóa hoán vị cột
- 🏢 **DES** - Data Encryption Standard

## 🎯 Mục Đích Giáo Dục

### Cho Học Sinh/Sinh Viên

- Hiểu cách hoạt động của thuật toán mã hóa
- Trải nghiệm thực hành với các cipher
- Học phân tích bảo mật và phương pháp tấn công

### Cho Giảng Viên

- Công cụ giảng dạy tương tác
- Demo trực quan cho lớp học
- Nội dung giáo án hoàn chỉnh

## 🛠️ Cài Đặt & Chạy Local

### Yêu Cầu

- Python 3.11+
- pip

### Các Bước

```bash
# Clone repository
git clone [your-repo-url]
cd Cybersecurity_Data-privacy

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
streamlit run app.py
```

Truy cập: `http://localhost:8501`

## 📖 Cách Sử Dụng

1. **Chọn thuật toán** từ sidebar
2. **Đọc lý thuyết** trong expander "Lý Thuyết & Nguyên Lý"
3. **Xem mã giả** trong expander "Mã Giả & Thuật Toán"
4. **Học ví dụ** trong expander "Ví Dụ Chi Tiết"
5. **Phân tích bảo mật** trong expander "Phân Tích Bảo Mật"
6. **Thử demo** với input của riêng bạn

## 🔍 Kiến Thức Được Cung Cấp

### Lý Thuyết

- Nguyên lý hoạt động của từng thuật toán
- Lịch sử và ứng dụng thực tế
- Độ phức tạp tính toán

### Mã Giả

- Thuật toán step-by-step
- Implementation details
- Code examples

### Ví Dụ Thực Tế

- Input/output cụ thể
- Tính toán từng bước
- Giải thích quá trình

### Phân Tích Bảo Mật

- Điểm mạnh và yếu
- Phương pháp tấn công
- Countermeasures
- Đánh giá an toàn

## 🎨 Tính Năng UI/UX

- **Giao diện hiện đại** với CSS tùy chỉnh
- **Responsive design** cho mobile
- **Interactive demos** real-time
- **Color-coded categories** dễ phân biệt
- **Error handling** thân thiện

## 🔧 Cấu Trúc Dự Án

```
├── app.py              # Main Streamlit application
├── caesar.py           # Caesar cipher implementation
├── vigenere.py         # Vigenère cipher implementation
├── playfair.py         # Playfair cipher implementation
├── hill.py             # Hill cipher implementation
├── polyalphabetic.py   # Polyalphabetic cipher implementation
├── permutation.py      # Permutation cipher implementation
├── des.py              # DES implementation
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version for deployment
├── .streamlit/         # Streamlit configuration
└── README.md           # This file
```

## 📚 Thuật Toán Được Triển Khai

| Thuật Toán | Trạng Thái | Mô Tả |
|------------|------------|-------|
| Caesar | ✅ Perfect | Classical shift cipher |
| Vigenère | ✅ Perfect | Polyalphabetic substitution |
| Playfair | ✅ Excellent | Digraph substitution |
| Hill | ✅ Good | Matrix-based linear algebra |
| Polyalphabetic | ✅ Excellent | Multiple Caesar ciphers |
| Permutation | ✅ Good | Columnar transposition |
| DES | ✅ Perfect | Modern block cipher simulation |

## 🎓 Giá Trị Giáo Dục

- **University-level content** - Kiến thức chuyên sâu
- **Hands-on learning** - Thực hành trực tiếp
- **Historical context** - Bối cảnh lịch sử
- **Modern relevance** - Liên kết hiện đại
- **Security awareness** - Ý thức bảo mật

## 🚀 Deployment

Ứng dụng được deploy tự động lên **Streamlit Cloud** khi có thay đổi trên GitHub.

### Deployment Files

- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification
- `.streamlit/config.toml` - Streamlit configuration

## 📄 License

Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 🤝 Đóng Góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request.

## 📞 Liên Hệ

- **Developer**: [Your Name]
- **Email**: [Your Email]
- **GitHub**: [Your GitHub]

---

**🎉 Khám phá thế giới mã hóa và bảo mật thông tin cùng chúng tôi!** 🔐
