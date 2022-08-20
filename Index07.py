def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    k = bool(0)
    if len(s) > n:
        k = s[n]
    else:
        k
    return k
x=main('good', 3)
print(x)
