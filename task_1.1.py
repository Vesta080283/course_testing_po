def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_triangle():
  a, b, c = input(), input(), input()
  max_int = 2 ** 64
  if(is_int(a)  and is_int(b) and is_int(c)):
    a = int(a)
    b = int(b)
    c = int(c)
    if(a in range(1, max_int, 1) and b in range(1, max_int, 1) and c in range(1, max_int, 1)):
      if(a > b + c or b > a + c or c > a + b):
        print("Фигура является треугольником.")
      else:
        print("Фигура не является треугольником.")
    else:
      print(f"Введенные данные должны быть целым числом от 1 до {max_int}!")
  else:
    print(f"Введенные данные должны быть целым числом от 1 до {max_int}!")

is_triangle()
