"""
Should emit:
B015 - on lines 8, 12, 22, 29
"""

assert 1 == 1

1 == 1

assert 1 in (1, 2)

1 in (1, 2)


if 1 == 2:
    pass


def test():
    assert 1 in (1, 2)

    1 in (1, 2)


data = [x for x in [1, 2, 3] if x in (1, 2)]


class TestClass:
    1 == 1
