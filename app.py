import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Interactive Function Plotter",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Interactive Function Plotter")
st.write("Explore the effect of parameter k on the graph.")

# Slider
k = st.slider(
    "Change the value of k",
    min_value=0.0,
    max_value=200.0,
    value=2.0,
    step=0.1
)

# Domain
x = np.linspace(-np.sqrt(3), np.sqrt(3), 1000)

# Function
y = np.abs(x)**(2/3) + 0.9 * np.sin(k*x) * np.sqrt(3-x**2)

# Plot
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, color="red", linewidth=2, label=f"k = {k:.1f}")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Interactive Mathematical Function")
ax.grid(True)
ax.legend()

st.pyplot(fig)

plt.close(fig)

st.success(f"Current value of k: {k:.1f}")
