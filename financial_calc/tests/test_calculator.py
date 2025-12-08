import pytest
from calculator.calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax
)


class TestCalculateSimpleInterest:
    """Тесты для функции calculate_simple_interest"""
    
    def test_correct_calculation(self):
        """Проверка правильности расчёта"""
        # Пример 1
        result = calculate_simple_interest(1000, 5, 2)
        expected = 1000 * 5 * 2 / 100  # 100
        assert result == expected
        
        # Пример 2
        result = calculate_simple_interest(5000, 3.5, 4)
        expected = 5000 * 3.5 * 4 / 100  # 700
        assert result == expected
    
    def test_zero_values(self):
        """Проверка работы с нулевыми значениями"""
        # Нулевая основная сумма
        result = calculate_simple_interest(0, 5, 2)
        assert result == 0
        
        # Нулевая процентная ставка
        result = calculate_simple_interest(1000, 0, 2)
        assert result == 0
        
        # Нулевое время
        result = calculate_simple_interest(1000, 5, 0)
        assert result == 0
    
    def test_negative_values(self):
        """Проверка вызова ValueError при отрицательных значениях"""
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(-1000, 5, 2)
        
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(1000, -5, 2)
        
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(1000, 5, -2)


class TestCalculateCompoundInterest:
    """Тесты для функции calculate_compound_interest"""
    
    def test_correct_calculation(self):
        """Проверка правильности расчёта"""
        # Пример 1: ежегодное начисление (n=1)
        result = calculate_compound_interest(1000, 5, 2)
        expected = 1000 * (1 + 5/(100*1))**(1*2)  # 1102.5
        assert result == expected
        
        # Пример 2: ежеквартальное начисление (n=4)
        result = calculate_compound_interest(1000, 5, 2, n=4)
        expected = 1000 * (1 + 5/(100*4))**(4*2)
        assert result == expected
    
    def test_zero_values(self):
        """Проверка работы с нулевыми значениями"""
        # Нулевая основная сумма
        result = calculate_compound_interest(0, 5, 2)
        assert result == 0
        
        # Нулевая процентная ставка
        result = calculate_compound_interest(1000, 0, 2)
        assert result == 1000  # principal * (1 + 0) ** time = principal
        
        # Нулевое время
        result = calculate_compound_interest(1000, 5, 0)
        assert result == 1000  # principal * (1 + rate)**0 = principal
    
    def test_negative_values(self):
        """Проверка вызова ValueError при отрицательных значениях"""
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_compound_interest(-1000, 5, 2)
        
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_compound_interest(1000, -5, 2)
        
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_compound_interest(1000, 5, -2)
    
    def test_invalid_n(self):
        """Проверка вызова ValueError при некорректном n"""
        with pytest.raises(ValueError, match="n должно быть положительным целым числом"):
            calculate_compound_interest(1000, 5, 2, n=0)
        
        with pytest.raises(ValueError, match="n должно быть положительным целым числом"):
            calculate_compound_interest(1000, 5, 2, n=-1)


class TestCalculateTax:
    """Тесты для функции calculate_tax"""
    
    def test_correct_calculation(self):
        """Проверка правильности расчёта"""
        # Пример 1
        result = calculate_tax(1000, 10)
        expected = 1000 * 10 / 100  # 100
        assert result == expected
        
        # Пример 2
        result = calculate_tax(5000, 20.5)
        expected = 5000 * 20.5 / 100  # 1025
        assert result == expected
    
    def test_zero_values(self):
        """Проверка работы с нулевыми значениями"""
        # Нулевая сумма
        result = calculate_tax(0, 10)
        assert result == 0
        
        # Нулевая налоговая ставка
        result = calculate_tax(1000, 0)
        assert result == 0
    
    def test_invalid_tax_rate(self):
        """Проверка вызова ValueError при некорректной налоговой ставке"""
        with pytest.raises(ValueError, match="Налоговая ставка должна быть между 0 и 100"):
            calculate_tax(1000, -5)
        
        with pytest.raises(ValueError, match="Налоговая ставка должна быть между 0 и 100"):
            calculate_tax(1000, 101)
        
        with pytest.raises(ValueError, match="Налоговая ставка должна быть между 0 и 100"):
            calculate_tax(1000, 150)
    
    def test_edge_cases(self):
        """Проверка граничных значений"""
        # Минимальная ставка (0%)
        result = calculate_tax(1000, 0)
        assert result == 0
        
        # Максимальная ставка (100%)
        result = calculate_tax(1000, 100)
        assert result == 1000


if __name__ == "__main__":
    pytest.main()