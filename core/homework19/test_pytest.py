from homework3.homework3 import probel
from homework4.homework4_for import celye_chisla
from homework4.homework4_while import proiz
import pytest
from pytest import fixture, mark


@fixture
def positive_fixture():
    print("Positive tests")


@fixture
def negative_fixture():
    print("Negative tests")


class TestingProbel:

    @mark.usefixtures("positive_fixture")
    @mark.parametrize('x, result', (['hello', ('hello')],
                                    [' hello ', ('hello')],
                                    [' hello', ('hello')],
                                    ['hello ', ('hello')],
                                    ['  hello  ', ('hello')],
                                    ['hel lo', ('hel lo')]))
    def test_positive(self, x, result):
        res = probel(x)
        assert result == res

    @mark.usefixtures("negative_fixture")
    @mark.parametrize('x, result', ([True, ('Incorrect number')],
                                    [False, ('Incorrect number')],
                                    [123, ('Incorrect number : type error')]))
    def test_negative(self, x, result):
        res = probel(x)
        assert result == res


class TestingCelieChisla():

    @mark.parametrize('num_one, num_two, result', ([2, 5, 14],
                                                   [2, 50000, 1250024999],
                                                   [-5, -2, -14],
                                                   [-2, 2, 0],
                                                   [0.2, 5.3, 'Incorrect type'],
                                                   [0.3, 5, 'Incorrect type'],
                                                   [3, 5.3, 'Incorrect type'],
                                                   [0, 0, 0]))
    def test_pytest(self, num_one, num_two, result):
        res = celye_chisla(num_one, num_two)
        assert result == res


class TestingProiz():

    @mark.usefixtures("positive_fixture")
    @mark.parametrize('x, result', ([2, 2],
                                    [50, 30414093201713378043612608166064768844377641568960512000000000000],
                                    [0, 0],
                                    [1, 1]))
    def test_positive(self, x, result):
        res = proiz(x)
        assert result == res

    @mark.usefixtures("negative_fixture")
    @mark.parametrize('x, result', ([-6, 'Incorrect number : negative'],
                                    [0.2, 'Incorrect number : type error'],
                                    [False, 'Incorrect number : type error']))
    def test_negative(self, x, result):
        res = proiz(x)
        assert result == res
