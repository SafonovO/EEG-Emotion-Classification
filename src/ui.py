import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

root = tk.Tk()
root.title("EEG Signal Viewer")
root.geometry("1000x600")

# EEG frame
eeg_frame = tk.Frame(root, width=300, height=300, bd=1, relief=tk.SUNKEN)
eeg_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Info frame
info_frame = tk.Frame(root, width=300, height=400, bd=1, relief=tk.SUNKEN)
info_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Plot EEG (Implement code to take data from the file)
time = np.linspace(0, 1, 1000)
eeg_signal = np.sin(2 * np.pi * 10 * time) # sample sinusoidal graph
fig, ax = plt.subplots(figsize=(5, 4))
ax.plot(time, eeg_signal, color='b')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('EEG Signal')
ax.grid(True)
ax.set_ylim(-2, 2)
canvas = FigureCanvasTkAgg(fig, master=eeg_frame)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
