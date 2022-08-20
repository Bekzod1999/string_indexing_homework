def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    k=0
    

    if ord(s[0]) == 42:
        k+=1
    if ord(s[1]) == 42:
        k+=1
    if ord(s[2]) == 42:
        k+=1
    if ord(s[3]) == 42:
        k+=1
    if ord(s[4]) == 42:
        k+=1
    if k == 0:
        k = bool(0)
            
    return k
x=main('*d*fs')
print(x)
        