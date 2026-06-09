import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Tillo Shop",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Tillo")

# Данные о товарах со старыми путями и ценой 300 тг
products = [
    {
        "title": "Мини овечки",
        "price": "300 ₸",
        "image": "images/Свет против тьмы.jpg"
    },
    {
        "title": "Мини утка Куроми",
        "price": "300 ₸",
        "image": "images/Мини утка Куроми.jpg"
    },
    {
        "title": "Мини утки Хелло Китти",
        "price": "300 ₸",
        "image": "images/Мини утки Хелло Китти.jpg"
    }
]

# Сетка из 3 колонок
cols = st.columns(3)

for idx, prod in enumerate(products):
    with cols[idx % 3]:
        # Отображение локальной картинки с адаптивной шириной
        st.image(prod["image"], use_container_width=True)

        # Название товара
        st.subheader(prod["title"])

        # Цена
        st.write(f"Цена: {prod["price"]}")

        # Кнопка заказа
        st.button("Заказать", key=f"btn_{idx}", use_container_width=True)