from file_read import *
from de_psd_calulcation import *


def extract_from_raw(eeg_raw):
    params = {
        "stftn": 200,
        "fStart": [1, 4, 8, 14, 31],
        "fEnd": [4, 8, 14, 31, 50],
        "window": 4,
        "fs": 200
    }

    try:
        return DE_PSD(eeg_raw, params)
    except KeyError as err:
        print("No eeg matrix found. ", err)
