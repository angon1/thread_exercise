import threading
import multiprocessing
# import multiprocessing
from data_ops import MyData, load_namedtuple, save_namedtuple
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def pow_list(lock:threading.Lock) -> list:
    while True:
        lock.acquire()
        data_struct = load_namedtuple()
        if data_struct.index >= data_struct.arr_len:
            lock.release()
            return
        data_struct.arr[data_struct.index] **=2
        data_struct.index+=1
        save_namedtuple(data_struct)
        lock.release()


def power_single_thread() -> list:
    lock = threading.Lock()
    my_thread = threading.Thread(name='pow_list', target=pow_list, args=(lock,))
    my_thread.start()
    my_thread.join()
    return []

def power_multitple_threads() -> list:
    # executor = ThreadPoolExecutor(max_workers=5)
    lock = threading.Lock()
    workers_count = 5
    
    with ThreadPoolExecutor(max_workers=workers_count) as executor:
        executor.map(pow_list, [lock]*workers_count)

    return []

# def power_multitple_threads() -> list:
#     lock = threading.Lock()
#     my_threads = [threading.Thread(name=f't{x}', target=pow_list, args=(lock,)) for x in range(3)]
#     for thread in my_threads:
#         thread.start()
#     for thread in my_threads:
#         thread.join()     
#     return []

def power_multiprocess() -> list:
    # executor = ThreadPoolExecutor(max_workers=5)
    lock = multiprocessing.Lock()
    workers_count = 5
    
    with ProcessPoolExecutor(max_workers=workers_count) as executor:
        executor.map(pow_list, [lock]*workers_count)

    return []