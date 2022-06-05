
def countdown(n):
    """
        Пример замыкания.
        Функция реализует обратный счетчик.
        Вложенная функция next() уменьшает значение счетчика
        и возвращает его предыдущее значение
    """
    def next():
        nonlocal n
        r = n
        n -= 1
        return r
    return next

next = countdown(10)
while True:
    v = next() # получить следующее значение
    if not v: break
