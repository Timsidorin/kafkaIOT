import streamlit as st
import matplotlib.pyplot as plt
import time
import random

# Инициализация данных
timestamps = []
values = []

# Создание фигуры один раз
fig = plt.figure()

# Placeholder для графика
placeholder = st.empty()

# Цикл для имитации обновления данных
for _ in range(1000):  # Ограничение для примера
    timestamps.append(time.time())
    values.append(random.randint(0, 10000))  # Имитация данных IoT

    # Очистка предыдущего графика
    fig.clf()

    # Пересоздание осей после очистки
    ax = fig.add_subplot(111)

    # Обновление данных на графике
    ax.plot(timestamps, values, label='IoT Data')
    ax.set_title('Динамические данные IoT')
    ax.set_xlabel('Время')
    ax.set_ylabel('Значение')
    ax.legend()
    ax.grid(True)

    # Ограничение количества точек для производительности
    if len(timestamps) > 100:
        timestamps.pop(0)
        values.pop(0)

    # Обновление графика в placeholder
    with placeholder.container():
        st.pyplot(fig)

    time.sleep(0.1)  # Обновление каждую секунду
