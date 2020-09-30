import math

#Возвращает введенное число с консоли
def Integer(msg, min=-math.inf, max=math.inf):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print("Повторите попытку.")
        if num < min:
            print(f"Число должно быть не меньше {min}")
        elif num > max:
            print(f"Число должно быть не больше {max}")
        else:
            return num

#Возвращает введенное число с консоли
def Float(msg, min=-math.inf, max=math.inf):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print("Повторите попытку.")
        if num < min:
            print(f"Число должно быть не меньше {min}")
        elif num > max:
            print(f"Число должно быть не больше {max}")
        else:
            return num