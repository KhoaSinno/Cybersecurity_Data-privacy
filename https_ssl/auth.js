const express = require('express');
const bcrypt = require('bcrypt');
const session = require('express-session');

const app = express();


app.use(express.urlencoded({ extended: true }));

app.use(session({
    secret: 'secret',
    resave: false,
    saveUninitialized: true,
}));

// Giả lập cơ sở dữ liệu người dùng
const users = [
    { username: 'admin', password: bcrypt.hashSync('admin123', 10), role: 'admin' },
    { username: 'user', password: bcrypt.hashSync('user123', 10), role: 'user' }
];

// route login
app.get('/login', (req, res) => {
    res.send(`
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    `);
});

// route dashboard
app.get('/dashboard', (req, res) => {
    if (req.session.user) {
        res.send(`Welcome ${req.session.user.username}! <a href="/logout">Logout</a>`);
    } else {
        res.redirect('/login');
    }
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username);

    if (user && bcrypt.compareSync(password, user.password)) {
        req.session.user = { username: user.username, role: user.role };
        res.redirect('/dashboard');
    } else {
        res.send('Invalid credentials');
    }
})

app.get('/admin', (req, res) => {
    if (req.session.user && req.session.user.role === 'admin') {
        res.send('Welcome to the admin page');
    } else {
        res.status(403).send('Access denied');
    }
});


app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});