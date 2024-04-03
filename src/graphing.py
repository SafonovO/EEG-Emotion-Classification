import numpy as np
import matplotlib.pyplot as plt

# Return a figure to be displayed by the UI
# mat_file: Dictionary containing all EEG recordings, currentNode: [0, 61]
def getPlot(mat_file, currentNode):
    # Concatenate all EEG recordings for the given node

    numSamples = len(mat_file[currentNode-1])
    times = np.array(range(numSamples))

    # Plotting
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(times, mat_file[currentNode-1])
    ax.set_xlim([0, numSamples-1])
    #ax.set_ylim([-350, 350])       # some values are larger than |300| idk what the max is
    ax.grid(True)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Node ' + str(currentNode) + ' EEG Signal')
    return fig