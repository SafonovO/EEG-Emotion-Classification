import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def high_pass_filter(signal):
    # Filter parameters
    cutoff_freq=35
    sampling_freq=200 
    order=4
    nyquist_freq = 0.5 * sampling_freq
    cutoff = cutoff_freq / nyquist_freq

    # Design high-pass filter
    b, a = butter(order, cutoff, btype='high', analog=False)

    # Apply the filter
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

def getPlot(mat_file, currentNode, cutoff_freq=15):
    signal = mat_file[currentNode-1]

    numSamples = len(signal)
    times = np.array(range(numSamples))
    
    # Plotting
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(times,signal)
    ax.set_xlim([0, numSamples-1])
    ax.grid(True)
    ax.set_xlabel('Time (Sample Number)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Node ' + str(currentNode) + ' EEG Signal (High-pass filtered at ' + str(cutoff_freq) + ' Hz)')
    return fig
