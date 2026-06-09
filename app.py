import streamlit as st

# Настройка страницы (адаптивная сетка)
st.set_page_config(
    page_title="Tillo Shop",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Стилизация интерфейса (жестко закрепляем ЧЕРНЫЙ цвет текста, чтобы он не сливался с фоном на смартфонах)
st.markdown("""
    <style>
    .product-title {
        font-size: 16px;
        font-weight: bold;
        color: #1E1E1E !important;
        margin-top: 10px;
        margin-bottom: 5px;
        text-align: left;
    }
    .product-price {
        font-size: 18px;
        font-weight: bold;
        color: #E64A19 !important;
        margin-bottom: 15px;
        text-align: left;
    }
    div[data-testid="stMetricValue"] {
        color: #1E1E1E !important;
    }
    @media (max-width: 768px) {
        .product-title { font-size: 15px; }
        .product-price { font-size: 16px; }
    }
    </style>
""", unsafe_allow_html=True)

# Шапка твоего интернет-магазина
st.title("🛍️ Добро пожаловать в Tillo Shop")
st.write("Качественные товары с быстрой доставкой по Казахстану!")
st.divider()

# База данных твоих товаров (названия картинок должны строго совпадать с файлами в папке images)
products = [
    {
        "title": "Мини овечки (10 шт)",
        "price": "1 500 ₸",
        "image": "images/Свет против тьмы.jpg"
    },
    {
        "title": "Мини утка Куроми (10 шт)",
        "price": "1 800 ₸",
        "image": "images/Мини утка Куроми.jpg"
    },
    {
        "title": "Мини утки Хелло Китти (10 шт)",
        "price": "1 800 ₸",
        "image": "images/Мини утки Хелло Китти.jpg"
    }
]

# Создаем 3 колонки (на ПК будут в ряд, на мобильном автоматически выстроятся красиво вертикально)
cols = st.columns(3)

for idx, prod in enumerate(products):
    with cols[idx % 3]:
        # use_container_width=True автоматически сжимает картинку под размер экрана телефона
        st.image(prod["image"], use_container_width=True)

        # Гарантированно видимый черный текст названия
        st.markdown(f'<div class="product-title">{prod["title"]}</div>', unsafe_allow_html=True)

        # Ценник вместо пустых смайликов
        st.markdown(f'<div class="product-price">💵 Цена: {prod["price"]}</div>', unsafe_allow_html=True)

        # Красивая адаптивная кнопка для заказа
        st.button("Заказать", key=f"btn_{idx}", use_container_width=True)