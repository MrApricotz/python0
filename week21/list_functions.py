# -*- coding: utf-8 -*-


def skip(f):
    return None


@skip
def head(xs):
    """
    Напишете функция `head`, която взима списък и връща първият елемент на този списък.

    **Не се грижете, ако списъка е празен**

    >>> head([1,2,3])
    1
    >>> head(["Python"])
    "Python"
    """
    pass


@skip
def last(xs):
    """
    Напишете функция `last`, която взима списък и връща последния елемент на този списък

    **Не се грижете, ако списъка е празен**

    >>> last([1, 2, 3])
    3
    >>> last(["Python"])
    "Python"
    """
    pass


@skip
def tail(xs):
    """
    Напишете функция в Python, която взима списък и връща нов списък,
    който се състои от всички елементи **без първия** от първоначалния списъка.

    **Не се грижете, ако списъка е празен**

    >>> tail([1, 2, 3])
    [2, 3]
    >>> tail(["Python"])
    []
    """
    pass


@skip
def equal_lists(xs):
    """
    Напишете функция `equal_lists`, която взима два списъка и връща True, ако двата списъка за еднакви.

    Казваме, че два списъка са еднакви, ако:

    * Имат равна дължина
    * Всеки елемент да индекс `i` в първия е равен (чрез `==`) на елементът на индекс `i` във втория.

    >>> equal_lists([1, 2], [1, 2])
    True
    >>> equal_lists([1, 2], [2, 1])
    False
    >>> equal_lists([], [])
    True
    """
    pass


@skip
def count_item(xs):
    """
    Напишете функция `count_item`, която взима два аргумента - елемент и списък.
    Функцията връща броят на срещанията на дадения елемент в дадения списък.

    >>> count_item(5, [1, 2, 3, 4, 5])
    1
    >>> count_item("winter", ["winter", "winter"])
    2
    >>> count_item(False, [True, True])
    0
    """
    pass


@skip
def take(xs):
    """
    Напишете функция `take,` която взима два аргумента - цяло число и списък.

    Функцията връща нов списък, който се състои от първите `n` елемента, където `n` е цялото число от първия аргумент.

    >>> take(2, [1, 2, 3, 4, 5])
    [1, 2]
    >>> take(3, [3, 4, 5, 6, 7, 8])
    [3, 4, 5]
    >>> take(10, [1])
    [1]
    """
    pass


@skip
def drop(xs):
    """
    Напишете функция `drop`, която взима два аргумента - цяло число `n` и списък.

    Функцията връща нов списък, който представлява стария списък, без първите `n` елемента.

    >>> drop(1, [1, 2, 3])
    [2, 3]
    >>> drop(2, ["Python", "Ruby", "Django", "Rails"])
    ["Django", "Rails"]
    >>> drop(10, [1])
    []
    """
    pass


@skip
def reverse(xs):
    """
    Напишете функция `reverse`, която взима един списък и го връща обърнат.
    Последния елемент става първи, предпоследния втори и т.н.

    >>> reverse(["Speak", "in", "reverse", "you", "must!"])
    ["must!", "you", "reverse", "in", "Speak"]
    >>> reverse([1, 2, 3])
    [3, 2, 1]
    >>> reverse([])
    []
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
