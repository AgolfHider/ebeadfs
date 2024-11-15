result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Помилка з ключем {key} та значенням {value}: {e}")

print("Результат:", result)
