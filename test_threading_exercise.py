import pytest
import numpy as np
from threading_exercise import power_multiprocess, power_multitple_threads, power_single_thread

_ARR_SIZE = 100000

@pytest.fixture
def arr_to_test(): return list(range(_ARR_SIZE))

@pytest.fixture
def rand_arr(): return np.random.randn(_ARR_SIZE)
    

def test_setup(arr_to_test, benchmark, rand_arr):
    pass


def test_power_single_thread(benchmark, arr_to_test):
    benchmark(power_single_thread,arr_to_test)
        
def test_power_multitple_threads(benchmark,arr_to_test):
    benchmark(power_multitple_threads,arr_to_test)

def test_power_multiprocess(benchmark, arr_to_test):
    benchmark(power_multiprocess,arr_to_test)
