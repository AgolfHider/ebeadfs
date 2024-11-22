#ЗАВДАННЯ 1 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class WordLengthIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            word_length = len(self.words[self.index])
            self.index += 1
            return word_length
        else:
            raise StopIteration


word_list = ["шо", "хеллоуворлд", "еыфаы", "генн", "йцкпирпд"]
iterator = WordLengthIterator(word_list)

print("Довжини слів:")
for length in iterator:
    print(length)


#ЗАВДАННЯ 3 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def stepin_of_three():
    exponent = 0
    while True:
        yield 3 ** exponent
        exponent += 1


generator = stepin_of_three()

for _ in range(100):
    print(next(generator))


#ЗАВДАННЯ 5 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

