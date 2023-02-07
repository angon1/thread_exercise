import threading
import multiprocessing

_ARR_SIZE = 10
_arr = list(range(_ARR_SIZE))
_index = 0

def pow_list(lock:threading.Lock) -> list:
    global _index
    while True:
        lock.acquire()
        if _index < len(_arr):
            _arr[_index] = _arr[_index]**2
            _index += 1
            print(threading.current_thread().name, _index)
            lock.release()
        else:
            lock.release()
            return
        
        
    

def power_single_thread() -> list:
    
    global _index 
    _index = 0
    lock = threading.Lock()
    my_thread = threading.Thread(name='pow_list', target=pow_list, args=(lock,))
    my_thread.start()
    my_thread.join()
    return []


def power_multitple_threads() -> list:
    
    global _index 
    _index = 0
    lock = threading.Lock()
    my_threads = [threading.Thread(name=f't{x}', target=pow_list, args=(lock,)) for x in range(3)]
    
    for thread in my_threads:
        print(thread)
        thread.start()
    for thread in my_threads:
        thread.join()     
    return []

def power_multiprocess() -> list:
    return []