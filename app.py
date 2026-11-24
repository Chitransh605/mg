import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Live Function Simulation", layout="wide")

st.title("🔴 Live Mathematical Simulation")

st.markdown(
    r"### $y=|x|^{2/3}+0.9\sin(kx)\sqrt{3-x^2}$"
)

# Simulation controls
auto_mode = st.toggle("Enable Live Simulation", value=True)

speed = st.slider(
    "Simulation Speed",
    min_value=0.1,
    max_value=5.0,
    value=1.0,
    step=0.1
)

if not auto_mode:
    manual_k = st.slider(
        "Manual k value",
        min_value=0.0,
        max_value=20.0,
        value=2.0,
        step=0.1
    )

# Domain
x = np.linspace(-np.sqrt(3), np.sqrt(3), 1000)

# Live updating area
@st.fragment(run_every="100ms")
def live_simulation():

    if auto_mode:
        k = (time.time() * speed) % 20
    else:
        k = manual_k

    y = (
        np.abs(x)**(2/3)
        + 0.9 * np.sin(k*x) * np.sqrt(3-x**2)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(x, y, color="red", linewidth=2)

    ax.set_title(f"Live Simulation | k = {k:.2f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)

    ax.set_xlim(-np.sqrt(3), np.sqrt(3))
    ax.set_ylim(-1.5, 3.5)

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.metric("Current k", f"{k:.2f}")

live_simulation()
