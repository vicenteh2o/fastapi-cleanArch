"""
Basic functions for testing ruff and pytest pre-commit hooks.
"""


def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
        
    Returns:
        The area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    return length * width


def is_even(number: int) -> bool:
    """
    Check if a number is even.
    
    Args:
        number: The number to check
        
    Returns:
        True if the number is even, False otherwise
    """
    return number % 2 == 0


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


# Test functions
def test_calculate_area():
    """Test the calculate_area function."""
    # Test normal cases
    assert calculate_area(5, 3) == 15
    assert calculate_area(0, 5) == 0
    assert calculate_area(2.5, 4) == 10.0
    
    # Test error cases
    try:
        calculate_area(-1, 5)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        calculate_area(5, -1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_is_even():
    """Test the is_even function."""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False


def test_fibonacci():
    """Test the fibonacci function."""
    # Test base cases
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    
    # Test normal cases
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    
    # Test error case
    try:
        fibonacci(-1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


if __name__ == "__main__":
    # Run basic tests 
    test_calculate_area()
    test_is_even()
    test_fibonacci()
    print("All tests passed!")