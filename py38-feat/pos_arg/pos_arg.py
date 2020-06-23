# Only takes positional arguments
def incr(x, /):
    return x + 1

# Takes 1 pos argument, then either pos or keyword 
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"

# Takes only keyword arguments
def fahrenheit(*, celcius=30):
    return 32 + celcius * 9/5

# Takes both keyword and positional arguments
# Must be positional first, then either pos/key, then must be key
def headline(text, /, border="~", *, width=50):
    return f" {text} ".center(width, border)
