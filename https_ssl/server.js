const https = require('https');
const fs = require('fs');
const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello HTTPS!');
});

const options = {
  key: fs.readFileSync('server.key'),
  cert: fs.readFileSync('server.cert'),
//   secureProtocol: 'TLSv1_method', // mặc định dùng TLS mới nhất
};

https.createServer(options, app).listen(3000, () => {
  console.log('HTTPS server running at https://localhost:3000');
});

// Đảm bảo rằng bạn đã tạo các file server.key và server.cert trước khi chạy server này
// Bạn có thể tạo chúng bằng OpenSSL hoặc sử dụng các công cụ khác để tạo chứng