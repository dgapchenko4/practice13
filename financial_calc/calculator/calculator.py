def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Вычисляет простые проценты.
    
    Формула: principal * rate * time / 100
    
    Args:
        principal: Основная сумма
        rate: Процентная ставка
        time: Время в годах
    
    Returns:
        Сумма процентов
    
    Raises:
        ValueError: Если аргументы отрицательные
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    
    return principal * rate * time / 100


def calculate_compound_interest(principal: float, rate: float, time: float, n: int = 1) -> float:
    """
    Вычисляет сложные проценты.
    
    Формула: principal * (1 + rate/(100*n))**(n*time)
    
    Args:
        principal: Основная сумма
        rate: Процентная ставка
        time: Время в годах
        n: Количество начислений в год (по умолчанию 1)
    
    Returns:
        Итоговая сумма (основная сумма + проценты)
    
    Raises:
        ValueError: Если аргументы отрицательные или n <= 0
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    
    if n <= 0:
        raise ValueError("n должно быть положительным целым числом")
    
    return principal * (1 + rate / (100 * n)) ** (n * time)


def calculate_tax(amount: float, tax_rate: float) -> float:
    """
    Вычисляет сумму налога.
    
    Формула: amount * tax_rate / 100
    
    Args:
        amount: Сумма
        tax_rate: Процент налога
    
    Returns:
        Сумма налога
    
    Raises:
        ValueError: Если tax_rate не в диапазоне 0-100
    """
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Налоговая ставка должна быть между 0 и 100")
    
    return amount * tax_rate / 100