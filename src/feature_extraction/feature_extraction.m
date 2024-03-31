%%
% Retrieved from https://github.com/ziyujia/Signal-feature-extraction_DE-and-PSD

% notes
% 1 sample in the extracted DE feature matrix is 4 seconds of video clips
% for cz_eeg2 (clip 2): 51:00-49:25 = 95 seconds
% 95 seconds / 4 second window = 23.75, same as de_movingAve2 and de_LDS2
% for cz_eeg2: it has 19001 points
% at 1000hz, 95 * 4 = 95000 sample points
% downsample to 200hz, divide by a factor of 1000/200 = 5
% 95000 / 5 ~ 19001 points

%       stft_para.stftn     frequency domain sampling rate
%       stft_para.fStart    start frequency of each frequency band
%       stft_para.fEnd      end frequency of each frequency band
%       stft_para.window    window length of each sample point(seconds)
%       stft_para.f         original frequency

params.stftn = 200;
params.fStart = [1,4,8,14,31];
params.fEnd = [4,8,14,31,50];
params.window = 4;
params.fs = 200;

[psd, de] = STFT(cz_eeg, params);