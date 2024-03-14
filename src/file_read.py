import numpy
import tkinter as tk
from tkinter import filedialog


def read_npz():
    """
    This function opens up a file manager window and asks the user to
    select an .npz file.
    :return: a NpzFile object containing the .npz file data
    :raise Exception: if the file is not .npz and it cannot be read
    """

    root = tk.Tk()
    root.withdraw()

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
    except Exception as err:
        print("Error reading .npz file:", err)


# For testing purposes
if __name__ == '__main__':
    read_npz()
