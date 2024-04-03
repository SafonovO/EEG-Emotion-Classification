import numpy as np
import pickle
import scipy.io as sio
import os

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC


# Function
def train_and_save():
    # Initialize variables
    X = []
    y = []

    # Loading the data for all 16 participants using the provided DE features
    for i in range(16):
        path = 'SEED-V/EEG_DE_features/' + str(i+1) + '_123.npz'
        data_npz = np.load(path)
        data = pickle.loads(data_npz['data'])
        label = pickle.loads(data_npz['label'])

        # Split every trial data individually
        for j in range(45):
            # Separate all DE features in the trial
            for k in range(data[j].shape[0]):
                X.append(data[j][k])
                y.append(label[j][k])

    '''
    # Load in SEED IV dataset
    path = 'SEED_IV/eeg_feature_smooth/'

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
                    X.append(lds_data[j])

                    # Add the correct labels based on the session number
                    if session == 0:
                        y.append(session1_label[i])
                    elif session == 1:
                        y.append(session2_label[i])
                    else:
                        y.append(session3_label[i])
    '''

    print("Loading data complete!")
    # Split the data to training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=23)
    # Use LinearSVC, StandardScaler to normalize value
    clf = make_pipeline(StandardScaler(), LinearSVC(dual=True, verbose=True))
    # Train the data
    print("Training data now!")
    clf.fit(X_train, y_train)
    # Check the performance using the test data
    print("Training complete!")
    print(clf.score(X_test, y_test))

    # Save model
    with open('model.pkl', 'wb') as f:
        pickle.dump(clf, f)
