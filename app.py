import streamlit as st
import os

# Путь к круглой фирменной иконке
favicon_path = "images/android-chrome-512x512.png"

# Настройка вкладки браузера
if os.path.exists(favicon_path):
    st.set_page_config(page_title="Tillo", page_icon=favicon_path, layout="wide")
else:
    st.set_page_config(page_title="Tillo", layout="wide")

# --- НАСТРОЙКА УЛЬТРА-СВЕТЛОГО ПЕРЛАМУТРОВОГО ФОНА И ШРИФТОВ ---
st.markdown("""
    <style>
        /* Импортируем Montserrat с супер-жирным начертанием 900 */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Outfit:wght@300;500&display=swap');

        /* Светлый перламутрово-бирюзовый градиент на весь экран */
        .stApp {
            background: linear-gradient(180deg, #F9FFFE 0%, #F4FDFB 300px, #FFFFFF 100%);
        }

        /* Стили для центрированной шапки */
        .header-wrapper {
            text-align: center;
            padding-top: 25px;
            margin-bottom: 20px;
        }

        /* ИСПРАВЛЕНО: Шрифт Montserrat 900 (Black) — массивный и плотный, как на логотипе */
        .brand-title {
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            font-size: 3.8rem;
            letter-spacing: 3px;
            color: #0EA5B9;
            margin: 10px 0 0 0;
            line-height: 1.0;
            text-transform: uppercase;
        }

        .brand-subtitle {
            font-family: 'Outfit', sans-serif;
            font-weight: 400;
            color: #71717A;
            font-size: 1.1rem;
            margin: 12px 0 0 0;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
    </style>
""", unsafe_allow_html=True)

# --- МИНИМАЛИСТИЧНАЯ ЦЕНТРИРОВАННАЯ ШАПКА ---
st.markdown('<div class="header-wrapper">', unsafe_allow_html=True)

# Логотип по центру
img_cols = st.columns([2.2, 1, 2.2])
with img_cols[1]:
    if os.path.exists(favicon_path):
        st.image(favicon_path, use_container_width=True)

# Текст бренда с новым плотным шрифтом
st.markdown("""
        <h1 class="brand-title">TILLO</h1>
        <p class="brand-subtitle">Коллекционные mini-фигурки</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 50px;'></div>", unsafe_allow_html=True)

# --- 1. БЛОК С МИНИ-ФИГУРКАМИ ---
products = [
    {"title": "Мини котики", "image": "images/Мини котики.jpg"},
    {"title": "Мини капибары", "image": "images/Мини капибары.jpg"},
    {"title": "Мини кабанчик", "image": "images/Мини кабанчик.jpg"},
    {"title": "Мини овечки", "image": "images/Мини овечки.jpg"},
    {"title": "Мини утка Куроми", "image": "images/Мини утка куроми.jpg"},
    {"title": "Мини утки Хеллоу Кити", "image": "images/Мини утки хеллоу кити.jpg"},
    {"title": "Утка-привидение", "image": "images/utkaprividenie.jpg"},
    {"title": "Мини гемы", "image": "images/Мини гемы.jpg"},
    {"title": "Мини дамплинги", "image": "images/Мини дамплинги.jpg"},
    {"title": "Мини какашки", "image": "images/Мини какашки.jpg"},
    {"title": "Мини сердечки", "image": "images/Мини сердечки.jpg"},
    {"title": "Мини Six Seven", "image": "images/Мини six seven.jpg"},
]

cols = st.columns(3)
for index, prod in enumerate(products):
    with cols[index % 3]:
        if os.path.exists(prod["image"]):
            st.image(prod["image"], use_container_width=True)
        else:
            st.warning(f"Нет файла: {prod['image']}")

        st.subheader(prod["title"])
        st.markdown("""
        💵 **300 ₸ за штуку**
        * Набор (10 шт.) без упаковки — **200 ₸**
        * Набор (10 шт.) в упаковке — **300 ₸**
        """)
        st.markdown("<div style='margin: 20px 0; border-bottom: 1px dashed #E0E0E0;'></div>", unsafe_allow_html=True)

# --- 2. БЛОК: 5 УПАКОВОК ---
st.markdown("<h2 style='margin-top: 50px; font-family: sans-serif; font-weight: 600;'>📦 Упаковки</h2>",
            unsafe_allow_html=True)

packs = [
    {"img": "images/Надёжная упаковка.jpg", "title": "Упаковка Гемы"},
    {"img": "images/Надёжная упаковка 2.jpg", "title": "Упаковка 67"},
    {"img": "images/Надёжная упаковка 3.jpg", "title": "Упаковка Какашки"},
    {"img": "images/Надёжная упаковка 4.jpg", "title": "Упаковка Уточки"},
    {"img": "images/Надёжная упаковка 5.jpg", "title": "Упаковка Сердечки"},
]

pack_cols = st.columns(3)
for idx, pack in enumerate(packs):
    with pack_cols[idx % 3]:
        if os.path.exists(pack["img"]):
            st.image(pack["img"], caption=pack["title"], use_container_width=True)

# --- 3. БЛОК: НАБОРЫ ---
st.markdown("<div style='margin-top: 50px; border-bottom: 1px solid #E0E0E0; margin-bottom: 30px;'></div>",
            unsafe_allow_html=True)
st.markdown("<h2 style='font-family: sans-serif; font-weight: 600;'>🎁 Наборы</h2>", unsafe_allow_html=True)

tillo_set_img = "images/Свет против тьмы.jpg"
tillo_set_title = "Набор Tillo (Свет против тьмы)"

set_cols = st.columns(3)
with set_cols[0]:
    if os.path.exists(tillo_set_img):
        st.image(tillo_set_img, caption=tillo_set_title, use_container_width=True)
    else:
        st.warning(f"Нет файла: {tillo_set_img}")