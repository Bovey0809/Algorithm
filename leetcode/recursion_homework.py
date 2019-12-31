def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)

assert 5050 == recursive_sum(100)

def recursive_nums(n):
    """Recursively print the digits in the num.
    
    Args:
        n: the digits you want to use.
    
    Returns:
        return the str of the digits.
    """
    # base case
    if len(str(n)) == 1:
        return n
    else:
        # strip another digit
        return n%10 + recursive_nums(n//10)
    
print(recursive_nums(1234))

