def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    # 48 - 57

    if ord(s) > 47 and ord(s) < 58:
        k = s
    else:
        k = -1
    return k
x=main('/')
print(x)