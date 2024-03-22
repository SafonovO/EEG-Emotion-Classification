% Uses neuroscanio 1.3 files on github
% Uses the multichanplot Matlab addon

filename = 'PATH TO EEG CNT FILE'
eegFile = loadcnt(filename)

data = eegFile.data;
data_dim = size(data);
partData = data(1:data_dim(1,1), 1:100);
partData = permute(partData, [2 1])
dimensions = size(partData);
partData(1, 1:dimensions(1,2))

multichanplot(partData,1/1000*99,'channels', [1:3], 'srate',1000)

% figure(1)
%plot(partData, '-o'); 