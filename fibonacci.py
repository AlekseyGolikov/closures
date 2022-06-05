
def fibonacci():
    """
        Последовательность Фибоначчи – это ряд чисел, каждое следующее число – это сумма двух чисел перед ним.
        Первые два числа, X₀=0 и X₁=1. Значит, X₂ – это сумма X₀ и X₁.

        Реализация алгоритма Фибоначчи методом рекурсии:
        def fib_recursion(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib_recursion(n-1) + fib_recursion(n-2)
        Рекурсия выполняется в 1000 раз медленее замыканий,
        т.к. значения для каждого уровня рекурсии хранятся отдельно.
        У рекурсии ограничена глубина, у замыканий - нет
    """
    x1 = 0
    x2 = 1
    def get_next_number():
        nonlocal x1, x2
        x1, x2 = x2, x1+x2
        return x2
    return get_next_number

fibo = fibonacci()
for i in range(2, 21):
    num = fibo()
    print(f'{i}е число Фибоначчи равно {num}')
