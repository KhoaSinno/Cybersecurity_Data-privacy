# 🔐 Cryptography Education Platform

Nền tảng giáo dục web tương tác về các thuật toán mã hóa từ cổ điển đến hiện đại.

## 📋 Tính năng

- **7 thuật toán mã hóa**: Caesar, Vigenère, Playfair, Hill, Polyalphabetic, Permutation, DES
- **Giao diện tương tác**: Demo trực tiếp với input/output thực tế
- **Giải thích chi tiết**: Lý thuyết, công thức, và ví dụ minh họa
- **Tấn công Brute Force**: Demo tấn công Caesar Cipher
- **Responsive design**: Giao diện đẹp, dễ sử dụng

## 🚀 Cách chạy Local

### Bước 1: Cài đặt Python
Đảm bảo Python 3.7+ đã được cài đặt trên máy.

### Bước 2: Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### Bước 3: Chạy ứng dụng
```bash
streamlit run app.py
```

Ứng dụng sẽ mở tại: `http://localhost:8501`

## 🌐 Deploy lên Streamlit Cloud (Miễn phí)

### Bước 1: Tạo repository trên GitHub
1. Đăng nhập GitHub
2. Tạo repository mới (public)
3. Upload tất cả file trong folder này

### Bước 2: Deploy trên Streamlit Cloud
1. Truy cập [share.streamlit.io](https://share.streamlit.io)
2. Đăng nhập bằng GitHub
3. Click "New app"
4. Chọn repository vừa tạo
5. Main file path: `app.py`
6. Click "Deploy"

### Bước 3: Truy cập ứng dụng
Sau vài phút, bạn sẽ có URL public để chia sẻ!

## 📂 Cấu trúc Project

```
├── app.py                 # File chính của Streamlit app
├── requirements.txt       # Danh sách thư viện cần thiết
├── caesar.py             # Thuật toán Caesar Cipher
├── vigenere.py           # Thuật toán Vigenère Cipher
├── playfair.py           # Thuật toán Playfair Cipher
├── hill.py               # Thuật toán Hill Cipher
├── polyalphabetic.py     # Thuật toán Polyalphabetic
├── permutation.py        # Thuật toán Permutation
├── des.py                # Thuật toán DES
└── README.md             # File hướng dẫn này
```

## 🔧 Hướng dẫn Deploy chi tiết

### Option 1: Streamlit Cloud (Khuyên dùng - 100% miễn phí)

1. **Tạo GitHub repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/crypto-education.git
   git push -u origin main
   ```

2. **Deploy:**
   - Vào [share.streamlit.io](https://share.streamlit.io)
   - Connect GitHub account
   - Chọn repository
   - App sẽ tự động deploy

### Option 2: Heroku (Có free tier hạn chế)

1. **Tạo file `Procfile`:**
   ```
   web: sh setup.sh && streamlit run app.py
   ```

2. **Tạo file `setup.sh`:**
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   port = $PORT
   enableCORS = false
   headless = true
   " > ~/.streamlit/config.toml
   ```

3. **Deploy lên Heroku:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 3: Railway (Miễn phí với giới hạn)

1. Vào [railway.app](https://railway.app)
2. Connect GitHub repository
3. Select deployment trigger
4. App tự động deploy

## 🎯 Hướng dẫn sử dụng

1. **Chọn thuật toán** từ sidebar
2. **Đọc lý thuyết** trong phần mở rộng
3. **Thử nghiệm** với văn bản và khóa tùy chỉnh
4. **Quan sát kết quả** mã hóa/giải mã
5. **Học từ ví dụ** được cung cấp

## 🛠️ Customization

Để thêm thuật toán mới:

1. Tạo file `.py` cho thuật toán
2. Implement hàm `encrypt_*` và `decrypt_*`
3. Thêm import vào `app.py`
4. Tạo hàm `show_*_cipher()` trong `app.py`
5. Thêm option vào sidebar

## 📱 Screenshots

[Sẽ được thêm sau khi deploy]

## 🤝 Contributing

Mọi đóng góp đều được chào đón! Hãy tạo pull request hoặc issue.

## 📄 License

MIT License - Xem file LICENSE để biết thêm chi tiết.

## 🙏 Acknowledgments

- Các thuật toán được implement cho mục đích giáo dục
- UI/UX được tối ưu cho việc học tập
- Streamlit framework cho phép tạo web app nhanh chóng
