# Задание 1.1a: представьте, что ваша программа по трём введённым целым числам определяет,
# может ли существовать треугольник с такими длинами сторон. Допустим, что ваша программа
# выполняется в некоей изолированной идеальной среде, и вам всего-то осталось проверить
# корректность её работы на трёх 8-байтовых знаковых целых числах. Вы используете автоматизацию,
# и компьютер может провести 100 миллионов проверок в секунду. Сколько займёт проверка всех вариантов?
# А задумались ли вы, как подготовить для этого теста проверочные данные (на основе которых можно определить,
# верно ли сработала программа в каждом конкретном случае)?

# Сколько займёт проверка всех вариантов?
# 8-байтовое знаковое целое число - это 64-разрядное число со знаком(long, int64) диапазоне значений
# от -9 223 372 036 854 775 808 до 9 223 372 036 854 775 808 или от -2^63 до +2^63, 
# то есть диапазон значений длины одной стороны для проверки будет в 2 раза больше - 2^64
# Количество комбинации - произведение всех чисел
# Количество секунд в минутах - 365 * 24 * 60 * 60
# Решение: (2^64 * 2^64 * 2^64) / (100_000_000 * 31536000) = 1.9904559029003934436313386045179e^42 лет
# Ответ: около 2e^42 лет

import unittest


def count_time():
    max_int = 2 ** 64
    seconds_in_year = 365 * 24 * 60 * 60
    speed_pc = 100_000_000
    print((max_int ** 3) / (speed_pc * seconds_in_year))

# Расчеты показали нецелесообразность использования исчерпывающего тестирования.
# Так как документация с описание работы модуля недоступна
# смоделируем работу модуля по определению треугольника,
# который будет проверять правильность треугольника по условию -
# всякая сторона треугольника меньше разности двух других сторон: a < b + c, b < a + c, c < a + b,
# где a > 0, b > 0, c > 0, так как длина отрезка не может быть отрицательной или равной 0.
# При тестированиии на вход подаются граничные значения: (0,1,2^63,2^63 + 1)

def is_triangle(a, b, c):
    max_int = 2 ** 63
    if(is_int(a) and is_int(b) and is_int(c)):
        a = int(a)
        b = int(b)
        c = int(c)
        if(a in range(1, max_int + 1, 1) and b in range(1, max_int + 1, 1) and c in range(1, max_int + 1, 1)):
            if(a < b + c and b < a + c and c < a + b):
                # print("Фигура является треугольником.")
                return True
            else:
                return False
                # print("Фигура не является треугольником.")
        else:
            return False
            # print(
            #     f"Введенные данные должны быть целым числом от 1 до {max_int} включительно!")
    else:
        return False
        # print(
        #     f"Введенные данные должны быть целым числом от 1 до {max_int} включительно!")

# Примеры позитивного и негативного теста
class TestModuleIsTriangle(unittest.TestCase):
    def test_possitive_1(self):
        self.assertEqual(is_triangle(3, 4, 5), True)

    def test_negative_1(self):
        self.assertEqual(is_triangle(123, 256, 123), False)
        
 
def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    unittest.main()

# count_time()

# # positive tests
# print(is_triangle(3, 4, 5))
# is_triangle(4, 3, 5)
# is_triangle(5, 3, 4)
# is_triangle(3, 3, 4)
# is_triangle(4, 3, 3)
# is_triangle(3, 4, 3)
# is_triangle(str(pow(2, 63)), str(pow(2, 63)), 1)
# is_triangle(str(pow(2, 63)), str(pow(2, 63)), str(pow(2, 63)))

# # negative tests
# is_triangle(123, 256, 123)
# is_triangle(256, 123, 123)
# is_triangle(123, 123, 256)

# is_triangle(0, 256, 123)
# is_triangle(256, 0, 123)
# is_triangle(256, 123, 0)

# is_triangle(-1, 256, 123)
# is_triangle(256, -1, 123)
# is_triangle(256, 123, -1)

# is_triangle(str(pow(2, 63) + 1), 1, 1)
# is_triangle(1, str(pow(2, 63) + 1), 1)
# is_triangle(str(pow(2, 63) + 1), 1, 1)
# is_triangle(str(pow(2, 63)), 1, 1)
# is_triangle(1, str(pow(2, 63)), 1)
