import pytest
from calculator.calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax
)


def test_calculate_interest():
    """Тест обычных случаев вычисления простого процента."""
    result1 = calculate_simple_interest(3.9, 5.3, 8.30)
    expected1 = 3.9 * 5.3 * 8.30 / 100
    assert result1 == expected1
    
    result2 = calculate_simple_interest(2000, 6.2, 7.30)
    expected2 = 2000 * 6.2 * 7.30 / 100
    assert result2 == expected2


def test_zero_calculate_interest():
    """Тест с нулевыми значениями для простого процента."""
    result1 = calculate_simple_interest(0, 7.2, 6.20)
    assert result1 == 0
    
    result2 = calculate_simple_interest(4.2, 0, 8.50)
    assert result2 == 0
    
    result3 = calculate_simple_interest(7.6, 9.5, 0)
    assert result3 == 0


def test_error_calculate_interest():
    """Тест ошибочных случаев для простого процента."""
    with pytest.raises(ValueError, match='Аргументы должны быть неотрицательными'):
        calculate_simple_interest(-9.3, 8.4, 9.9)
        
    with pytest.raises(ValueError, match='Аргументы должны быть неотрицательными'):
        calculate_simple_interest(8.3, -9.7, 7.40)
        
    with pytest.raises(ValueError, match='Аргументы должны быть неотрицательными'):
        calculate_simple_interest(3.1, 8.0, -7.00)


def test_compound_interest():
    """Тест обычных случаев вычисления сложного процента."""
    result1 = calculate_compound_interest(4.8, 5.2, 9.8, 4)
    expected1 = 4.8 * (1 + 5.2 / (100 * 4)) ** (4 * 9.8)
    assert result1 == expected1
    
    result2 = calculate_compound_interest(6000, 9.7, 7.7, 8)
    expected2 = 6000 * (1 + 9.7 / (100 * 8)) ** (8 * 7.7)
    assert result2 == expected2


def test_zero_compound_interest():
    """Тест с нулевыми значениями для сложного процента."""
    result1 = calculate_compound_interest(0, 8.8, 5.5, 7)
    assert result1 == 0
    
    result2 = calculate_compound_interest(9.5, 0, 3.9, 3)
    assert result2 == 9.5  # Возвращается начальная сумма, когда ставка равна 0
    
    result3 = calculate_compound_interest(8.9, 3.0, 0, 9)
    assert result3 == 8.9  # Возвращается начальная сумма, когда время равно 0


def test_error_compound_interest():
    """Тест ошибочных случаев для сложного процента."""
    with pytest.raises(ValueError, match='Аргументы должны быть неотрицательными.'):
        calculate_compound_interest(-8.5, 9.9, 7.6, 6)
        
    with pytest.raises(ValueError, match='Аргументы должны быть неотрицательными.'):
        calculate_compound_interest(9.1, -5.2, 6.9, 3)
        
    with pytest.raises(ValueError, match='Аргументы должны быть неотрицательными.'):
        calculate_compound_interest(8.8, 7.7, -5.2, 9)
    
    with pytest.raises(ValueError, match='n должно быть положительным целым числом.'):
        calculate_compound_interest(7.8, 5.2, 8.7, 0)


def test_calculate_tax():
    """Тест обычных случаев вычисления налога."""
    result1 = calculate_tax(8.3, 2.6)
    expected1 = 8.3 * 2.6 / 100
    assert result1 == expected1
    
    result2 = calculate_tax(9.9, 7.7)
    expected2 = 9.9 * 7.7 / 100
    assert result2 == expected2


def test_zero_calculate_tax():
    """Тест с нулевыми значениями для налога."""
    result1 = calculate_tax(0, 8.6)
    assert result1 == 0
    
    result2 = calculate_tax(7.3, 0)
    assert result2 == 0
    
    # Тест граничных значений
    result3 = calculate_tax(100, 0)
    assert result3 == 0
    
    result4 = calculate_tax(100, 100)
    assert result4 == 100


def test_error_calculate_tax():
    """Тест ошибочных случаев для налога."""
    with pytest.raises(ValueError, match='Некорректный tax_rate.'):
        calculate_tax(2.8, 101)
        
    with pytest.raises(ValueError, match='Некорректный tax_rate.'):
        calculate_tax(8.5, -1)
            