import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="A", layout="wide")

# HTML بسيط مع خلفية سوداء وعنوان
html_code = """
<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #000000;
            color: #FFFFFF;
            font-family: 'Tajawal', sans-serif;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        h1 {
            font-size: 15vw;
            font-weight: 900;
            color: #FFD700;
            text-shadow: 0 0 30px rgba(255,215,0,0.7);
        }
        p {
            font-size: 1.5rem;
            opacity: 0.8;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>A</h1>
    <p>صفحة جديدة تماماً</p>
    <p style="font-size: 1rem; margin-top: 50px;">جاهز للبناء ✦</p>
</body>
</html>
"""

components.html(html_code, height=800, scrolling=False)
