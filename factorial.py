
def factorial(number):
    """
        Функция вычисления факториала
        >>> factorial(4)
        24
    """
    if not isinstance(number, int):
        raise TypeError('Число должно быть целым!')
    if number < 0 :
        raise ValueError('Число должно быть неотрицательным')

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

print(factorial(4))
