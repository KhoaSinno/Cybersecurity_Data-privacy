const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const app = express();
app.use(express.urlencoded({ extended: true }));

const db = new sqlite3.Database(':memory:');

// Tạo bảng và thêm user mẫu, chỉ khởi động server sau khi xong
db.run('CREATE TABLE users (username TEXT, password TEXT)', (err) => {
    if (err) throw err;
    db.run('INSERT INTO users (username, password) VALUES (?, ?)', ['admin', 'admin123'], () => {
        db.run('INSERT INTO users (username, password) VALUES (?, ?)', ['user', 'user123'], () => {
            app.listen(4000, () => {
                console.log('SQL safe server running at http://localhost:4000');
            });
        });
    });
});

// Hàm chống XSS
function sanitize(input) {
    return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

app.get('/login', (req, res) => {
    res.send(`
    <form method="POST" action="/login">
      <input type="text" name="username" placeholder="Username" required>
      <input type="password" name="password" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
  `);
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    db.get('SELECT * FROM users WHERE username = ? AND password = ?', [username, password], (err, user) => {
        if (user) {
            res.send(`Welcome ${sanitize(user.username)}!`);
        } else {
            res.send('Invalid credentials');
        }
    });
});

// app.listen(4000, () => {
//     console.log('SQL safe server running at http://localhost:4000');
// });