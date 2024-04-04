from file_read import *
from de_psd_calulcation import *


def extract_from_raw(eeg_name):
    eeg_mat = read_mat()

    if eeg_mat is None:
        print("No mat file is read.")
        return

    params = {
        "stftn": 200,
        "fStart": [1, 4, 8, 14, 31],
        "fEnd": [4, 8, 14, 31, 50],
        "window": 4,
        "fs": 200
    }

    try:
        return DE_PSD(eeg_mat[eeg_name], params)
    except KeyError as err:
        print("No eeg matrix found. ", err)


if __name__ == '__main__':
    psd, de = extract_from_raw("cz_eeg1")
    print(de)
