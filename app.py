import streamlit as st

st.title("Tillo")

# Твой старый массив товаров с ценой 300 тг
products = [
    {
        "title": "Мини овечки",
        "price": "300 тг",
        "image": "images/Свет против тьмы.jpg"
    },
    {
        "title": "Мини утка Куроми",
        "price": "300 тг",
        "image": "images/Мини утка Куроми.jpg"
    },
    {
        "title": "Мини утки Хелло Китти",
        "price": "300 тг",
        "image": "images/Мини утки Хелло Китти.jpg"
    }
]

# Твой старый дизайн отображения в 3 колонки
cols = st.columns(3)

for idx, prod in enumerate(products):
    with cols[idx % 3]:
        st.image(prod["image"])
        st.markdown(f'<span style="color:white">{prod["title"]}</span>', unsafe_allow_html=True)
        st.markdown(f'<span style="color:white">{prod["price"]}</span>', unsafe_allow_html=True)
        st.button("Купить", key=f"btn_{idx}")