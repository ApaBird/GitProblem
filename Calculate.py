def addition(a, b):
    try:
        c = a + b
        return c
    except Exception:
        print("Что то не складывается")
        return None


def subtraction(a, b):
    try:
        c = a - b
        return c
    except Exception:
        print("Что то не вычитается")
        return None


def multiplication(a, b):
    try:
        c = a * b
        return c
    except Exception:
        print("Что то не умножается")
        return None


def division(a, b):
    try:
        c = a / b
        return c
    except Exception:
        print("Что то не делится")
        return None


