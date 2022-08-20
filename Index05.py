import string
def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    # 1kld2
    k = 0
    if ord(s[0]) > 47 and ord(s[0]) < 58:
        k+=1
    if ord(s[1]) > 47 and ord(s[1]) < 58:
        k+=1
    if ord(s[2]) > 47 and ord(s[2]) < 58:
        k+=1
    if ord(s[3]) > 47 and ord(s[3]) < 58:
        k+=1
    if ord(s[4]) > 47 and ord(s[4]) < 58:
        k+=1
    
    return k
x=main('1s5d2')
print(x)