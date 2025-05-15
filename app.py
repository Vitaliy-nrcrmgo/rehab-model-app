
import streamlit as st
import joblib
import numpy as np

# Завантаження моделі
model = joblib.load("rehab_model.pkl")

st.title("Прогноз потреби у реабілітації у дітей")

st.markdown("Введіть значення для кожної з ознак:")

IMT = st.number_input("IMT – Індекс маси тіла", min_value=10.0, max_value=40.0, step=0.1)
WT = st.number_input("WT – Талія/Зріст (WHtR)", min_value=0.2, max_value=1.0, step=0.01)
ZSU = st.selectbox("ZSU – Перебування на окупованій території", [1, 2])
Eva = st.selectbox("Eva – Евакуація з території", [1, 2])
distress = st.slider("Сприйнятий дистрес", 0, 30, 15)
gsi = st.slider("GSI самоефективність", 0, 30, 15)

if st.button("Прогнозувати"):
    X = np.array([[IMT, WT, ZSU, Eva, distress, gsi]])
    prediction = model.predict(X)[0]
    if prediction == 2:
        st.error("Результат: Дитина ПОТРЕБУЄ реабілітаційних заходів.")
    else:
        st.success("Результат: Дитина НЕ потребує реабілітаційних заходів.")
