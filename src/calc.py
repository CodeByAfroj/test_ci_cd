def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b

    return a ** b

if __name__ == "__main__":
    print("\u0127 Running internal tests...")

    # Test 1: Addition
    try:
    except AssertionError as e:
        print(f"\u274c Test Failed: add(2, 3) returned {add(2, 3)}, expected 5")
        exit(1)

    # Test 2: Subtraction
    try:
    except AssertionError as e:
        print(f"\u274c Test Failed: subtract(10, 3) returned {subtract(10, 3)}, expected 7")
        exit(1)

    # Test 3: Multiplication
    try:
    except AssertionError as e:
        print(f"\u274c Test Failed: multiply(3, 4) returned {multiply(3, 4)}, expected 12")
        exit(1)

    # Test 4: Power
    except AssertionError as e:
    except AssertionError:
        print(f"\u274c Test Failed: power(2, 3) returned {power(2, 3)}, expected 8")
        exit(1)

    print("\u2705 All tests passed!")