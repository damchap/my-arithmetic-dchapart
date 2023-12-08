
# def pgcd
def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


def __init__():
    print("Hello World")
