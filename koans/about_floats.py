from koans_plugs import *


def test_can_sum_up():
    """
        Вещественные числа можно складывать.

        Обратите внимание, что вещественная часть отделяется от дробной точкой.
        Если использовать запятую, всё сломается.
    """

    assert 2.5 + 1.2 == 3.7


def test_can_assign_to_variables():
    """
        Вещественные числа можно записывать в переменные
    """
    a = 2.5
    b = 3.8
    assert b - 1.3 == a


def test_can_remove_real_part():
    """
        У вещественных чисел можно удалять дробную часть и превращать их в целые.
    """
    a = 2.1
    assert int(a) == 2


def test_has_rounding_problems():
    """
        У вещественных чисел есть проблемы с округлением.

        Так работает из-за того, как числа представляются в памяти.
    """
    a = 0.1
    assert a + 0.2 == 0.1 + 0.2  # подсказка: тут будет не 0.3


def test_can_miss_leading_zero():
    """
        Если у вещественного числа чцелая часть – ноль, то её можно не писать.
    """
    assert .5 * 2 == 1.0
