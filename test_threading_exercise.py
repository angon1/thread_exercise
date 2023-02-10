import pytest
import numpy as np
from threading_exercise import power_multiprocess, power_multitple_threads, power_single_thread

   
def test_power_single_thread(benchmark):
    benchmark(power_single_thread)
        
def test_power_multitple_threads(benchmark):
    benchmark(power_multitple_threads)

def test_power_multiprocess(benchmark):
    benchmark(power_multiprocess)
