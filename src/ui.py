import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from file_read import *
from graphing import *
from visualization import visualize_frame
from graphing import *

data = None  # Variable to hold the loaded data
current_trial = 1  # Initial trial number
current_sensor = 1
figures = {'eeg': None, 'heatmap': None}  # Dictionary to hold figure objects


def on_close(info_frame, eeg_frame):
    global figures
    if info_frame is not None:
        for widget in info_frame.winfo_children():
            widget.destroy()
    if eeg_frame is not None:
        for widget in eeg_frame.winfo_children():
            widget.destroy()
    # Close the figures
    for key, fig in figures.items():
        if fig:
            plt.close(fig)
            figures[key] = None
    root.quit()

def upload_data(eeg_frame, info_frame, reset=False):
    global data
    global current_sensor
    global current_trial
    global figures
    if reset:
        data = None
        current_trial = 1
        current_sensor = 1
    # Check if data has been loaded already
    if data is None:
        # Load data if not loaded
        data = read_all()

    # Destroy the previous canvases
    for widget in info_frame.winfo_children():
        widget.destroy()
    for widget in eeg_frame.winfo_children():
        widget.destroy()

    # Close previous figures if they exist
    for key, fig in figures.items():
        if fig:
            plt.close(fig)
            figures[key] = None

    if data is not None:
        # Get the sensor data for the current trial
        sensor_data = np.array(data[next(key for key in data.keys() if key.endswith("_eeg" + str(current_trial)))])

        # Create a label showing the trial number
        trial_label = tk.Label(info_frame, text="Trial Number: " + str(current_trial))
        trial_label.pack()

        sensor_data = high_pass_filter(sensor_data)

        # Get the EEG plot
        fig_eeg = getPlot(sensor_data, current_sensor)
        # Calculate mean over all time values for each sensor
        mean_sensor_data = np.mean(np.abs(sensor_data), axis=1)
        # Create a heatmap of the sensor values
        fig_heatmap = visualize_frame(mean_sensor_data)

        # Create a canvas for the heatmap
        canvas_heatmap = FigureCanvasTkAgg(fig_heatmap, master=info_frame)
        canvas_heatmap.draw()
        canvas_heatmap.get_tk_widget().pack()

        # Create a canvas for the EEG plot
        canvas_eeg = FigureCanvasTkAgg(fig_eeg, master=eeg_frame)
        canvas_eeg.draw()
        canvas_eeg.get_tk_widget().pack()

        # Entry field to input sensor number
        entry_label = tk.Label(eeg_frame, text="Enter Sensor Number:")
        entry_label.pack()
        sensor_entry = tk.Entry(eeg_frame)
        sensor_entry.pack()
        sensor_entry.insert(tk.END, str(current_sensor))

        # Button to change the sensor number
        change_sensor_button = tk.Button(eeg_frame, text="Change Sensor", command=lambda: change_sensor(sensor_entry.get(), eeg_frame, info_frame))
        change_sensor_button.pack()

        # Entry field to input trial number
        entry_label = tk.Label(info_frame, text="Enter Trial Number:")
        entry_label.pack()
        trial_entry = tk.Entry(info_frame)
        trial_entry.pack()
        trial_entry.insert(tk.END, str(current_trial))

        # Button to change the trial number
        change_button = tk.Button(info_frame, text="Change Trial", command=lambda: change_trial(trial_entry.get(), eeg_frame, info_frame))
        change_button.pack()

        # Store the figures
        figures['eeg'] = fig_eeg
        figures['heatmap'] = fig_heatmap

def change_trial(new_trial, eeg_frame, info_frame):
    global current_trial
    global current_sensor
    global data
    try:
        new_trial = int(new_trial)
        if new_trial >= 1 and new_trial <= 24:  # Ensure the trial number is within the range 1 to 24
            current_trial = new_trial
            current_sensor = 1
            upload_data(eeg_frame, info_frame)
        else:
            raise ValueError("Trial number must be between 1 and 24")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def change_sensor(new_sensor, eeg_frame, info_frame):
    global current_sensor
    try:
        new_sensor = int(new_sensor)
        if new_sensor >= 1 and new_sensor <= 62:  # Ensure the sensor number is within the range 1 to 62
            current_sensor = new_sensor
            upload_data(eeg_frame, info_frame)
        else:
            raise ValueError("Sensor number must be between 0 and 61")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def run():
    global data
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Emotion Classification using EEG")
    root.geometry("1920x1080")
    # EEG frame
    eeg_frame = tk.Frame(root, width=550, height=350, bd=1, relief=tk.SUNKEN)
    eeg_frame.pack(side=tk.LEFT, padx=10, pady=10)
    # Info frame
    info_frame = tk.Frame(root, width=600, height=700, bd=1, relief=tk.SUNKEN)
    info_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    # Button frame
    upload_button_frame = tk.Frame(root)
    upload_button_frame.pack(side=tk.TOP, anchor=tk.N, padx=10, pady=10)
    upload_button = tk.Button(upload_button_frame, text="Upload Data", command=lambda: upload_data(eeg_frame, info_frame, reset=True), width=15, height=3)
    upload_button.grid(row=1, column=0, columnspan=2)
    root.protocol("WM_DELETE_WINDOW", lambda: on_close(info_frame, eeg_frame))
    root.mainloop()