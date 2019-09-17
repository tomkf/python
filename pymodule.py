import sys

def repeat(s, exclaim):
    """
    this is the docstring, describing what the function does
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

print repeat(sys.argv[1], sys.argv[2])