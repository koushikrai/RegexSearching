import time

def measure_efficiency(regex, folder_path, search_func):
    """Measure the execution time of a regex search."""
    start_time = time.time()
    results = search_func(regex, folder_path)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, results
