import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# return a figure to be displayed by the UI
# currentEEG: [1, 24], currentNode:[0, 61]
def getPlot(mat_file, currentEEG, currentNode):
    # get the data for the particular EEG recording and node
    data = mat_file['cz_eeg' + str(currentEEG)][currentNode]

    numNodes = mat['cz_eeg1'].shape[0]
    numSamples = mat['cz_eeg1'].shape[1]
    times = list(range(0, numSamples))

    # plotting
    fig, ax = plt.subplots()
    ax.plot(times, data)
    ax.set_xlim([0, numSamples-1])
    #ax.set_ylim([-300, 300])       # some values are larger than |300| idk what the max is
    ax.grid(True)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Session ' + str(currentEEG) + ' Node ' + str(currentNode) + ' EEG Signal')
    return fig

