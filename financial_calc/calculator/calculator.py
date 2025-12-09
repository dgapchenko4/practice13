def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Вычисляет простой процент.
    Аргументы:
        principal: Начальная сумма
        rate: Годовая процентная ставка (в процентах)
        time: Время в годах
    Возвращает сумму простого процента
    Выбрасывает ValueError, если какой-либо аргумент отрицательный
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError('Аргументы должны быть неотрицательными')
    
    return principal * rate * time / 100


def calculate_compound_interest(principal: float, rate: float, time: float, n: int = 1) -> float:
    """
    Вычисляет сложный процент.
    Аргументы:
        principal: Начальная сумма
        rate: Годовая процентная ставка (в процентах)
        time: Время в годах
        n: Количество начислений процентов в год
    Возвращает сумму сложного процента (общая сумма включая начальный капитал)
    Выбрасывает ValueError: Если какой-либо аргумент отрицательный или n не положительное
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError('Аргументы должны быть неотрицательными.')
    elif n <= 0:
        raise ValueError('n должно быть положительным целым числом.')
    
    return principal * (1 + rate / (100 * n)) ** (n * time)


def calculate_tax(amount: float, tax_rate: float) -> float:
    """
    Вычисляет сумму налога.
    Аргументы:
        amount: Базовая сумма
        tax_rate: Налоговая ставка (в процентах, 0-100)
    Возвращает сумму налога
    Выбрасывает ValueError, если tax_rate не находится в диапазоне от 0 до 100
    """
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError('Некорректный tax_rate.')
    
    return amount * tax_rate / 100



print(calculate_simple_interest(2.1, 3.5, 12.10))
print(calculate_compound_interest(2.2, 4.3, 8.5, 4))
print(calculate_tax(4.4, 2.8))