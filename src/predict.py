import numpy as np
import pickle
import train_model
import file_read
import feature_extraction


# Function to use the trained model to predict
# Takes in EEG raw data in the format of np.array of size 62x(recordings) where 62 is the EEG channels
# Returns a tuple of the probability distribution of the prediction and the predicted emotion
def predict(data):
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

    # Feature extraction on the EEG recordings
    de_feat = feature_extraction.extract_from_raw(data)[1]

    # Processing the DE features into the format the model is trained on
    de_feat = np.swapaxes(de_feat, 0, 1)  # Swap the first axes with the second axes
    de_feat = np.reshape(de_feat, (de_feat.shape[0], 310))  # Convert it from 3d array to 2d array

    # Print score
    print("Testing the model with the provided data")
    prediction = clf.predict(de_feat)
    emotion_prob = np.zeros(5)
    total_data = len(de_feat)
    for i in range(total_data):
        emotion_idx = int(prediction[i])
        emotion_prob[emotion_idx] = emotion_prob[emotion_idx] + 1
    #print("Probability distribution for the prediction is:")
    prob_dist = emotion_prob/total_data
    #print(prob_dist)

    # Dictionary for model
    dict_model = {
        0: "Disgust",
        1: "Fear",
        2: "Sad",
        3: "Neutral",
        4: "Happy"
    }

    predicted_emotion = dict_model.get(int(np.argmax(emotion_prob)))
    #print("Predicted emotion is: " + predicted_emotion)

    return prob_dist, predicted_emotion


# Main for testing
if __name__ == '__main__':
    eeg_data_file = file_read.read_all()
    eeg_data = eeg_data_file['cz_eeg1']
    dist, pred = predict(eeg_data)
    print(dist)
    print(pred)

