def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    # 48 - 57
    if len(s) == 2:
        if ord(s[0]) == 45 and ord(s[1]) > 47 and ord(s[1]) < 58:
            k=s
        else:
            k = -1
    elif ord(s) > 47 and ord(s) < 58:
        k = s
    else:
        k = -1
    return k 
x=main('l')
print(x)