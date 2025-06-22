mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
primaryColor = \"#1f77b4\"\n\
backgroundColor = \"#ffffff\"\n\
secondaryBackgroundColor = \"#f0f2f6\"\n\
textColor = \"#262730\"\n\
\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = \$PORT\n\
" > ~/.streamlit/config.toml
