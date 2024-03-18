import numpy
import pickle
import tkinter as tk
from tkinter import filedialog
import scipy.io

# GUI init
root = tk.Tk()
root.withdraw()


def read_mat():
    """
    This function opens up a file manager window and asks the user to
    select an .mat file.
    :return: a dictionary containing the .mat file data
    :raise Exception: if the file is not .mat or it cannot be read
    """
    file_path = filedialog.askopenfilename()

    try:
        mat = scipy.io.loadmat(file_path)
        # print(mat)
        # print(type(mat))
        # data_mat = numpy.array(mat['de_movingAve1'])
        # print(data_mat)

        return mat
    except FileNotFoundError as err:
        print("No file was selected", err)
    except Exception as err:
        print("Error reading .mat files", err)


def read_npz():
    """
    This function opens up a file manager window and asks the user to
    select an .npz file.
    :return: a NpzFile object containing the .npz file data
    :raise Exception: if the file is not .npz or it cannot be read
    """

    file_path = filedialog.askopenfilename()
    # print("Path: " + file_path)
    try:
        data_npz = numpy.load(file_path)
        # print("Load Successful")
        # print(data_npz)
        # print(data_npz.files)

        return data_npz
    except ValueError as err:
        print("Error reading .npz file:", err)
    except TypeError as err:
        print("No file was selected: ", err)
    except Exception as err:
        print("Error reading .npz file:", err)


def read_de_feature(data_npz):
    if data_npz is None:
        print("No object is loaded")
        return None

    data = pickle.loads(data_npz['data'])
    label = pickle.loads(data_npz['label'])

    label_dict = {0: 'Disgust', 1: 'Fear', 2: 'Sad', 3: 'Neutral', 4: 'Happy'}
    for i in range(45):
        print('Session {} -- Trial {} -- EmotionLabel : {}'.format(i // 15 + 1, i % 15 + 1, label_dict[label[i][0]]))


# For testing purposes
if __name__ == '__main__':
    # read_de_feature(read_npz())
    read_mat()
