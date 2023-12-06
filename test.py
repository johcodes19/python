from saying import square
import pytest

def main():
    test_negative()
    test_positive()
    test_zero()
    
def test_square():
    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print('The square of 2 was not equal to 4')
    # try:
    #     assert square(3) == 9
    # except AssertionError:
    #     print('The square of 3 was not equal to 9')
    assert square(2) == 4
    assert square(3) ==9
    assert square(-4) ==16
    assert square(0) == 0

def test_positive():
    assert square(1) == 1
    assert square(2) ==4

def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square('string')

# if __name__ == '__main__':
#     main()