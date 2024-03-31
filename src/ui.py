import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from file_read import *
from visualization import visualize_frame




def on_close(info_frame,eeg_frame):
    
    if info_frame is not None:
        for widget in info_frame.winfo_children():
            widget.destroy()
    if eeg_frame is not None: 
        for widget in eeg_frame.winfo_children():
            widget.destroy()
    root.quit()  

def upload_data(eeg_frame,info_frame):
    data = read_all()
    print(data)
    #destroy the previous canvas
    for widget in info_frame.winfo_children():
        widget.destroy()

    if data is not None:
        # Create a single canvas widget for visualization
        canvas2 = None

        sensor_data =numpy.array(data[next(key for key in data.keys() if key.endswith("_eeg"+"1"))])[:,0] 
        visualization = visualize_frame(sensor_data)
        canvas2 = FigureCanvasTkAgg(visualization, master=info_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack()
        '''
        sensor_data = np.array(data[next(key for key in data.keys() if key.endswith("_eeg1"))])
        # Iterate over the range of time indices
        for i in range(sensor_data.shape[1]):  # Assuming sensor_data is the EEG data
            sensor_data = np.array(data[next(key for key in data.keys() if key.endswith("_eeg1"))])[:, i] 
            visualization = visualize_frame(sensor_data)

            # Update the canvas with the new visualization
            if canvas2 is None:
                canvas2 = FigureCanvasTkAgg(visualization, master=info_frame)
                canvas2_widget = canvas2.get_tk_widget()
                canvas2_widget.pack()
            else:
                canvas2.figure = visualization
                canvas2.draw()

            # Update the Tkinter main loop to reflect changes
            root.update_idletasks()

            root.after(200)  
        '''

def run():
    root = tk.Tk()
    root.resizable(False, False)
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

    # Button frame
    upload_button_frame = tk.Frame(root)
    upload_button_frame.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

    upload_button = tk.Button(upload_button_frame, text="Upload", command= lambda: upload_data(eeg_frame,info_frame))
    upload_button.grid(row=2, column=0, columnspan=2)
    root.protocol("WM_DELETE_WINDOW", lambda: on_close(eeg_frame,info_frame))
    root.mainloop()
