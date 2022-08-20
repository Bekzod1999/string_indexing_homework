def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return s[0:len(s):len(s)-1]
x=main('bildsr')
print(x)