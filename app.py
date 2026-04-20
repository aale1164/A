import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="A", layout="wide")

# --- تحويل الصورة إلى Base64 ---
@st.cache_data
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

image_path = "AAAR12.webp"
image_base64 = get_image_base64(image_path)

# --- HTML مع الصورة كخلفية ---
html_code = f"""
<!DOCTYPE html>
<html dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Tajawal', sans-serif;
            background-image: url('data:image/webp;base64,{image_base64}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: #FFFFFF;
            text-shadow: 2px 2px 15px rgba(0,0,0,0.9);
        }}
        h1 {{
            font-size: 15vw;
            font-weight: 900;
            color: #FFD700;
            text-shadow: 0 0 30px rgba(255,215,0,0.7), 2px 2px 15px black;
        }}
        p {{
            font-size: 1.5rem;
            opacity: 0.9;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <h1>A</h1>
    <p>صفحة جديدة تماماً</p>
    <p style="font-size: 1rem; margin-top: 50px;">جاهز للبناء ✦</p>
</body>
</html>
"""

# عرض المكون إذا تم تحميل الصورة بنجاح
if image_base64:
    components.html(html_code, height=800, scrolling=False)
else:
    st.error("الصورة AAAR12.webp غير موجودة في مجلد المشروع.")
