import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import sys

numEEG = 0          # num EEG recordings for this patient
numNodes = 0        # num nodes in the EEG recording
numSamples = 0      # num samples for any node in the current EEG recording
currentNode = -1    # current node in range [0, numNodes-1]
currentEEG = -1     # current EEG num for mat keys in range [0, numEEG-1]
times = 0           # array of the timestamps (for x-axis)

mat = 0             # load .mat file here

def uploadData():
    # python moment right here
    global mat
    global numEEG
    global numNodes
    global numSamples
    global currentNode
    global currentEEG
    global times
        
    # replace this line with a file upload by user
    mat = scipy.io.loadmat('1_20160518.mat') ###
    
    numEEG = len(mat.keys()) - 3    # subtract 3 beacause of header, version, and globals
    if(numEEG <= 0):                # error: no EEG data found
        sys.exit(1)
    
    numNodes = mat['cz_eeg1'].shape[0]
    numSamples = mat['cz_eeg1'].shape[1]
    currentNode = 0
    currentEEG = 0
    times = list(range(0, numSamples))

def nextNode():
    global currentNode
    currentNode = (currentNode + 1) % numNodes

def prevNode():
    global currentNode
    currentNode = (currentNode - 1) % numNodes

def EEG_change():
    global currentNode
    global numSamples
    global times

    currentNode = 0
    numSamples = mat['cz_eeg' + str(currentEEG+1)].shape[1]
    times = list(range(0, numSamples))

def nextEEG():
    global currentEEG
    
    currentEEG = (currentEEG + 1) % numEEG
    EEG_change()

def prevEEG():
    global currentEEG
    
    currentEEG = (currentEEG - 1) % numEEG
    EEG_change()

def displayPlot():
    # get the data for the particular EEG recording and node
    data = mat['cz_eeg' + str(currentEEG+1)][currentNode]

    # plotting
    plt.plot(times, data)
    plt.xlim([0, numSamples-1])
    #plt.ylim([-300, 300])       # some values are larger than |300| idk what the max is
    plt.grid(True)
    #plt.set_xlabel('Time')
    #plt.set_ylabel('Amplitude')
    plt.title('Session ' + str(currentEEG+1) + ' Node ' + str(currentNode) + ' EEG Signal')
    plt.show()


uploadData()
displayPlot()
nextNode()
displayPlot()
prevEEG()
displayPlot()

