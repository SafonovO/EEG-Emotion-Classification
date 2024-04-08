import numpy as np
import pickle
import train_model
import scipy.io as sio
import os

# Function to parse through the list called labels and convert it to the value in the dictionary
def apply_dict_to_list(dictionary, labels):
    for i, k in enumerate(labels):
        labels[i] = dictionary.get(k)
    return labels


# Main
if __name__ == '__main__':
    model_file = "model.pkl"

    # Load the model safely
    try:
        print("Loading model...")
        # Load model if it exists
        with open(model_file, 'rb') as f:
            clf = pickle.load(f)
    except FileNotFoundError:
        print("Model not found! Creating and training model...")
        train_model.train_and_save()  # Call the function defined in train_model.py
        # Load model if it exists
        with open(model_file, 'rb') as f:
            clf = pickle.load(f)
    '''
    # List to store the test data
    seedV_data = []
    seedV_labels = []

    # Load in SEED V dataset
    for i in range(16):
        path = 'SEED-V/EEG_DE_features/' + str(i + 1) + '_123.npz'
        data_npz = np.load(path)
        data = pickle.loads(data_npz['data'])
        label = pickle.loads(data_npz['label'])

        # Split every trial data individually
        for j in range(45):
            # Separate all DE features in the trial
            for k in range(data[j].shape[0]):
                # Skip appending data when label is 0 because the model can't classify it correctly
                if label[j][k] != 0:
                    seedV_data.append(data[j][k])
                    seedV_labels.append(label[j][k])
        '''

    # Load in SEED IV dataset
    path = 'SEED_IV/eeg_feature_smooth/'

    # List to store the test data
    seedIV_data = []
    seedIV_labels = []

    # Labels defined in the ReadMe.txt
    session1_label = [1, 2, 3, 0, 2, 0, 0, 1, 0, 1, 2, 1, 1, 1, 2, 3, 2, 2, 3, 3, 0, 3, 0, 3]
    session2_label = [2, 1, 3, 0, 0, 2, 0, 2, 3, 3, 2, 3, 2, 0, 1, 1, 2, 1, 0, 3, 0, 1, 3, 1]
    session3_label = [1, 2, 2, 1, 3, 3, 3, 1, 1, 2, 1, 0, 2, 3, 3, 0, 2, 3, 0, 0, 2, 0, 1, 0]

    # Loop for every session (total of 3)
    for session in range(3):
        for filename in os.listdir(path + str(session + 1)):
            data_mat = sio.loadmat(path + str(session + 1) + '/' + filename)  # Load the file in the directory

            # Go through every de_LDS data
            for i in range(24):  # 24 trials
                de_lds_str = "de_LDS"
                # de_lds_str = "de_movingAve"
                lds_data = data_mat[de_lds_str + str(i + 1)]  # Get the lds data
                lds_data = np.swapaxes(lds_data, 0, 1)  # Swap the first axes with the second axes
                lds_data = np.reshape(lds_data, (lds_data.shape[0], 310))  # Convert it from 3d array to 2d array
                for j in range(lds_data.shape[0]):
                    seedIV_data.append(lds_data[j])

                    # Add the correct labels based on the session number
                    if session == 0:
                        seedIV_labels.append(session1_label[i])
                    elif session == 1:
                        seedIV_labels.append(session2_label[i])
                    else:
                        seedIV_labels.append(session3_label[i])
    '''
    # (model) 0 = neutral, 1 = sad, 2 = fear, 3 = happy
    # (SEED V) 0 = disgust, 1 = fear, 2 = sad, 3 = neutral, 4 = happy
    # Dictionary to convert the labels of SEED IV to the proper label for the model
    dict_seedV_to_model = {
        3: 0,  # Neutral
        2: 1,  # Sad
        1: 2,  # Fear
        4: 3,  # Happy
    }
    '''

    # (SEED IV) 0 = neutral, 1 = sad, 2 = fear, 3 = happy
    # (model) 0 = disgust, 1 = fear, 2 = sad, 3 = neutral, 4 = happy
    # Dictionary to convert the labels of SEED IV to the proper label for the model
    dict_seedIV_to_model = {
        0: 3,  # Neutral
        1: 2,  # Sad
        2: 1,  # Fear
        3: 4,  # Happy
    }

    # Parsing each value of the label through the dictionary
    seedIV_labels = apply_dict_to_list(dict_seedIV_to_model, seedIV_labels)

    # Print score
    print("Testing the model with SEED IV dataset")
    # print(clf.score(seedV_data, seedV_labels))
    prediction = clf.predict(seedIV_data)
    print("Accuracy for SEED IV dataset", clf.score(seedIV_data, seedIV_labels))

    print("Prediction frequency distribution:")
    emotion_prob = np.zeros(5)
    seedIV_labels_total = np.zeros(5)
    for i in range(len(prediction)):
        emotion_idx = int(prediction[i])
        emotion_prob[emotion_idx] = emotion_prob[emotion_idx] + 1
        seedIV_labels_total[int(seedIV_labels[i])] = seedIV_labels_total[int(seedIV_labels[i])] + 1
    print(emotion_prob)
    print("Ground truth frequency distribution:")
    print(seedIV_labels_total)
