import numpy as np
import pickle
import train_model


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

    # (model) 0 = neutral, 1 = sad, 2 = fear, 3 = happy
    # (SEED V) 0 = disgust, 1 = fear, 2 = sad, 3 = neutral, 4 = happy
    # Dictionary to convert the labels of SEED IV to the proper label for the model
    dict_seedV_to_model = {
        3: 0,  # Neutral
        2: 1,  # Sad
        1: 2,  # Fear
        4: 3,  # Happy
    }

    # Parsing each value of the label through the dictionary
    seedV_labels = apply_dict_to_list(dict_seedV_to_model, seedV_labels)

    # Print score
    print("Testing the model with SEED IV dataset")
    print(clf.score(seedV_data, seedV_labels))
