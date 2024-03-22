import numpy as np
import pickle
import train_model
import scipy.io as sio


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

    # Load in SEED IV dataset
    path = 'SEED_IV/eeg_feature_smooth/1/' + str(1) + '_20160518.mat'
    data_mat = sio.loadmat(path)
    # data = pickle.loads(data_npz['data'])
    # label = pickle.loads(data_npz['label'])

    # (SEED IV) 0 = neutral, 1 = sad, 2 = fear, 3 = happy
    # (Model) 0 = disgust, 1 = fear, 2 = sad, 3 = neutral, 4 = happy
    # Dictionary to convert the labels of SEED IV to the proper label for the model
    dict_seedIV_to_model = {
        0: 3,  # Neutral
        1: 2,  # Sad
        2: 1,  # Fear
        3: 4,  # Happy
    }

    # Labels defined in the ReadMe.txt
    session1_label = [1, 2, 3, 0, 2, 0, 0, 1, 0, 1, 2, 1, 1, 1, 2, 3, 2, 2, 3, 3, 0, 3, 0, 3]
    session2_label = [2, 1, 3, 0, 0, 2, 0, 2, 3, 3, 2, 3, 2, 0, 1, 1, 2, 1, 0, 3, 0, 1, 3, 1]
    session3_label = [1, 2, 2, 1, 3, 3, 3, 1, 1, 2, 1, 0, 2, 3, 3, 0, 2, 3, 0, 0, 2, 0, 1, 0]

    # Parsing each value of the label through the dictionary
    session1_label = apply_dict_to_list(dict_seedIV_to_model, session1_label)

    # List to store data in the right format for the model
    lds_list = []
    lds_labels = []

    # Go through every de_LDS data
    for i in range(24):  # 24 trials
        de_lds_str = "de_LDS"
        lds_data = data_mat[de_lds_str + str(i + 1)]  # Get the lds data
        lds_data = np.swapaxes(lds_data, 0, 1)  # Swap the first axes with the second axes
        lds_data = np.reshape(lds_data, (lds_data.shape[0], 310))  # Convert it from 3d array to 2d array
        for j in range(lds_data.shape[0]):
            lds_list.append(lds_data[j])
            lds_labels.append(session1_label[i])

    # Print score
    print("Testing the model with SEED IV dataset")
    print(clf.score(lds_list, lds_labels))