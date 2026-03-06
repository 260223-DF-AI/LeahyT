from functools import wraps, lru_cache
import time

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
    return wrapper

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)

    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
    return wrapper
import time
from functools import wraps

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    print(f"Attempt {attempts}/{max_attempts} failed with: {e}")
                    if attempts < max_attempts:
                        time.sleep(delay)
                    else:
                        print("All attempts failed.")
                        raise
        return wrapper
    return decorator

# def cache(max_size=128):
#     """
#     Cache function results.
#     Similar to lru_cache but with visible cache inspection.
    
#     Usage:
#         @cache(max_size=100)
#         def expensive_computation(x):
#             return x ** 2
        
#         expensive_computation(5)  # Computes
#         expensive_computation(5)  # Returns cached
        
#         # Inspect cache
#         expensive_computation.cache_info()
#         expensive_computation.cache_clear()
#     """
#     @lru_cache(maxsize=128)
#     def wrapper(*args, **kwargs):

#     return wrapper

