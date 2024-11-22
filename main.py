import time

def chas(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання '{func.__name__}': {execution_time:.6f} секунд")
        return result
    return wrapper


@chas
def functiya(n):
    total = 0
    for i in range(n):
        total += i
    return total


result = functiya(1000000)
print(f"Результат: {result}")
