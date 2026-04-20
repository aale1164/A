# -*- coding: utf-8 -*-
# محاكاة خريطة مسطحة (الإسقاط السمتي) - نسخة تعمل قطعاً في كولاب

# أولاً: تثبيت plotly إذا لم يكن موجوداً
!pip install -q plotly

import plotly.graph_objects as go
import numpy as np

# ============================================
# 1. نرسم خريطة مسطحة باستخدام الإسقاط السمتي
# ============================================

# نضيف نقطة وهمية واحدة فقط لتفعيل الخريطة (بدونها قد لا تظهر)
fig = go.Figure()

# هذه هي الطريقة الصحيحة لإظهار الخريطة المسطحة
fig.add_trace(go.Scattergeo(
    lon=[0], lat=[0],   # نقطة صامتة في المحيط
    mode='markers',
    marker=dict(size=0.1, opacity=0),  # مخفية تماماً
    showlegend=False
))

# تعيين نوع الإسقاط إلى سمتي مسطح (مركزه القطب الشمالي)
fig.update_geos(
    projection_type="azimuthal equidistant",
    projection_rotation=dict(lon=0, lat=90, roll=0),
    showcoastlines=True,
    coastlinecolor="DarkBlue",
    showland=True,
    landcolor="LightGreen",
    showocean=True,
    oceancolor="LightBlue",
    showcountries=True,
    countrycolor="gray",
    showlakes=True,
    lakecolor="LightBlue",
    # خطوط الطول والعرض
    lataxis_showgrid=True,
    lonaxis_showgrid=True,
    lataxis_gridcolor="white",
    lonaxis_gridcolor="white",
    lataxis_range=[-90, 90],
    lonaxis_range=[-180, 180]
)

# ============================================
# 2. إضافة الشمس والقمر والنجوم
# ============================================

# الشمس (نقطة كبيرة صفراء)
fig.add_trace(go.Scattergeo(
    lon=[0], lat=[45],
    mode='markers',
    marker=dict(size=20, color='gold', symbol='circle', line=dict(width=2, color='orange')),
    name='الشمس ☀️'
))

# القمر
fig.add_trace(go.Scattergeo(
    lon=[-120], lat=[20],
    mode='markers',
    marker=dict(size=10, color='silver', symbol='circle', line=dict(width=1, color='gray')),
    name='القمر 🌙'
))

# النجوم (100 نقطة عشوائية)
np.random.seed(42)
lons = np.random.uniform(-180, 180, 100)
lats = np.random.uniform(-90, 90, 100)
fig.add_trace(go.Scattergeo(
    lon=lons, lat=lats,
    mode='markers',
    marker=dict(size=3, color='white', opacity=0.7),
    name='النجوم ✨'
))

# ============================================
# 3. تنسيق الشكل
# ============================================
fig.update_layout(
    title=dict(text='🌍 الأرض المسطحة - الإسقاط السمتي متساوي المسافات', x=0.5, font=dict(size=18)),
    geo=dict(bgcolor='black'),
    paper_bgcolor='black',
    height=700,
    margin=dict(l=0, r=0, t=50, b=0),
    legend=dict(font=dict(color='white'), bgcolor='rgba(0,0,0,0.5)')
)

fig.show()
print("✅ إذا ظهرت خريطة فارغة، حرك الفأرة عليها وستظهر القارات والشمس والقمر.")
