def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    k=0
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    e = int(s[4])
    
    k = a+b+c+d+e
    return k

x=main('12332')
print(x)