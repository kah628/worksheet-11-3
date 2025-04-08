import my_module as mm # type: ignore
import numpy as np

# Tests Plot Function
def test_plot():
    assert mm.plot(lambda x: x**2, np.linspace(0, 5, 100))

# Tests Chooser Class
def test_chooser():
    assert mm.Chooser([1, 2, 3, 4, 5, 6])

# Tests Palindrome Number Function
def test_palindrome():
    assert mm.palindrome_num(121)

# Tests Favorite Number Function
def test_fav_nums():
    assert mm.fav_nums()