import os
import numpy as np
import math
import scipy.io as sio
from scipy.fftpack import fft, ifft


# Code retrieved from https://github.com/ziyujia/Signal-feature-extraction_DE-and-PSD/tree/master
def DE_PSD(data, stft_para):
    '''
    compute DE and PSD
    --------
    input:  data [n*m]          n electrodes, m time points
            stft_para.stftn     frequency domain sampling rate
            stft_para.fStart    start frequency of each frequency band
            stft_para.fEnd      end frequency of each frequency band
            stft_para.window    window length of each sample point(seconds)
            stft_para.fs        original frequency
    output: psd,DE [n*l*k]        n electrodes, l windows, k frequency bands
    '''
    # initialize the parameters
    stftn = stft_para['stftn']
    f_start = stft_para['fStart']
    f_end = stft_para['fEnd']
    fs = stft_para['fs']
    window = stft_para['window']

    window_points = fs * window

    f_start_num = np.zeros([len(f_start)], dtype=int)
    f_end_num = np.zeros([len(f_end)], dtype=int)
    for i in range(0, len(stft_para['fStart'])):
        f_start_num[i] = int(f_start[i] / fs * stftn)
        f_end_num[i] = int(f_end[i] / fs * stftn)

    # print(fStartNum[0],fEndNum[0])
    n = data.shape[0]
    m = data.shape[1]

    # print(m,n,l)
    l = math.floor(m/window_points)
    psd = np.zeros([n, l, len(f_start)])
    de = np.zeros([n, l, len(f_start)])

    # Hanning window
    h_length = window * fs

    # Hwindow=hanning(Hlength)
    h_window = np.array([0.5 - 0.5 * np.cos(2 * np.pi * n / (h_length + 1)) for n in range(1, h_length + 1)])

    window_points = fs * window  # 200hz * 4 seconds = 800 points in a window
    for i in range(0, l):
        data_now = data[:, window_points*i:window_points*(i+1)]
        for j in range(0, n):  # For loop to extract features in each window
            temp = data_now[j]  # get 800 points for the jth channel
            hdata = temp * h_window
            fft_data = fft(hdata, stftn)
            mag_fft_data = abs(fft_data[0:int(stftn / 2)])
            for p in range(0, len(f_start)):
                e = 0
                # E_log = 0
                for p0 in range(f_start_num[p] - 1, f_end_num[p]):
                    e = e + mag_fft_data[p0] * mag_fft_data[p0]  # For calculating (x^2) for PSD
                    # E_log = E_log + log2(magFFTdata(p0)*magFFTdata(p0)+1)
                e = e / (f_end_num[p] - f_start_num[p] + 1)  # Calculates E(x^2) by dividing the sum
                psd[j][i][p] = e
                de[j][i][p] = math.log(100 * e, 2)
                # de(j,i,p)=log2((1+E)^4)

    return psd, de
