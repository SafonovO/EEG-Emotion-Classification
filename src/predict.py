import numpy as np
import pickle
import train_model
import file_read


# Function to use the trained model to predict
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

    # Print score
    print("Testing the model with the provided data")
    prediction = clf.predict(data)
    emotion_prob = np.zeros(5)
    total_data = len(data)
    for i in range(total_data):
        emotion_idx = int(prediction[i])
        emotion_prob[emotion_idx] = emotion_prob[emotion_idx] + 1
    print("Probability distribution for the prediction is:")
    print(emotion_prob/total_data)

    # Dictionary for model
    dict_model = {
        0: "Disgust",
        1: "Fear",
        2: "Sad",
        3: "Neutral",
        4: "Happy"
    }

    predicted_emotion = dict_model.get(int(np.argmax(emotion_prob)))
    print("Predicted emotion is: " + predicted_emotion)

    return predicted_emotion


# Main for testing
if __name__ == '__main__':
    eeg_data_file = file_read.read_all()
    eeg_data = eeg_data_file['de_LDS1']
    eeg_data = np.swapaxes(eeg_data, 0, 1)  # Swap the first axes with the second axes
    eeg_data = np.reshape(eeg_data, (eeg_data.shape[0], 310))  # Convert it from 3d array to 2d array
    predict(eeg_data)
