import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

# Main
if __name__ == '__main__':
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

    print("Loading data complete!")
    # Split the data to training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=23)
    # Use LinearSVC (for now to test if it works), StandardScaler to normalize value
    clf = make_pipeline(StandardScaler(), LinearSVC(verbose=True))
    # Train the data
    print("Training data now!")
    clf.fit(X_train, y_train)
    # Check the performance using the test data
    print("Training complete!")
    print(clf.score(X_test, y_test))

