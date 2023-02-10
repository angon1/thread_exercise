import os
import dill
from dataclasses import dataclass

_ARR_SIZE = 1000



def init_data(datafile="datafile.pkl"):
    if not os.path.exists(datafile):
        arr = list(range(_ARR_SIZE))
        with open(datafile, "wb") as file:
            dill.dump(arr, file)


def save_data(arr, datafile="datafile.pkl"):
    with open(datafile, "wb") as file:
        dill.dump(arr, file)


def load_data(datafile="datafile.pkl"):
    with open(datafile, "rb") as file:
        arr = dill.load(file)
    return arr


#### second aproach


@dataclass
class MyData:
    arr : list[int]
    index : int
    arr_len : int

def init_namedtuple(datafile="named_tuple.pkl"):
    if not os.path.exists(datafile):
        arr = list(range(_ARR_SIZE))
        index = 0
        arr_len = len(arr)
        arr_tuple = MyData(arr, index, arr_len)
        with open(datafile, "wb") as file:
            dill.dump(arr_tuple, file)


def save_namedtuple(arr_tuple, datafile="named_tuple.pkl"):
    with open(datafile, "wb") as file:
        dill.dump(arr_tuple, file)


def load_namedtuple(datafile="named_tuple.pkl"):
    with open(datafile, "rb") as file:
        arr_tuple = dill.load(file)
    return arr_tuple

if __name__ == "__main__":
    init_data()
    init_namedtuple()
