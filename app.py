import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.title("Interactive Function Plotter")
window.geometry("900x650")

fig = Figure(figsize=(8, 5), dpi=100)
ax = fig.add_subplot(111)

x = np.linspace(-np.sqrt(3), np.sqrt(3), 1000)


k = 2

y = np.abs(x)**(2/3) + 0.9 * np.sin(k*x) * np.sqrt(3-x**2)

line, = ax.plot(x, y, color="red", linewidth=2)

ax.set_title("y = |x|^(2/3) + 0.9 sin(kx) sqrt(3-x²)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)


canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

def update_graph(value):

    k = float(value)

    y = np.abs(x)**(2/3) + 0.9 * np.sin(k*x) * np.sqrt(3-x**2)

    line.set_ydata(y)

    ax.set_title(f"Function Plot | k = {k:.2f}")

    canvas.draw_idle()



label = tk.Label(window, text="Adjust k value", font=("Arial", 12))
label.pack()

slider = tk.Scale(
    window,
    from_=0,
    to=200,
    resolution=0.1,
    orient=tk.HORIZONTAL,
    length=600,
    command=update_graph
)

slider.set(2)
slider.pack(pady=10)

window.mainloop()