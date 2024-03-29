import time

def throttle(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            while time.time() - start_time < seconds:
                print("Throttling...")
                time.sleep(0.1)
            return func(*args, **kwargs)
        return wrapper
    return decorator