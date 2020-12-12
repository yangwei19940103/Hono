import pytest
from pythoncode.calculator import Calculator


class Test_calculator():
    def setup_class(self):
        self.cal = Calculator()
        print('开始计算')

    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize('a, b, expected', [
        (10, 20, 30),
        (-5, -10, -15),
        (2000, 3000, 5000)], ids=['int', 'minus', 'bigint']
    )
    def test_add(self, a, b, expected):
        assert expected == self.cal.add(a, b)

    @pytest.mark.parametrize('a, b, expected', [
        (-5, -10 , 5), (-20, -10, -10), (0, 20, -20), (12, 0, 12), (1000, 500, 500), (-1000, -200, -800)], ids=[
        "one", "two", "three", "four", "five", "six"
    ]
                             )
    def test_sub(self, a, b, expected):
        assert expected == self.cal.sub(a, b)

    @pytest.mark.parametrize("a, b, expected", [
        (-2, -3, 6), (10, 50, 500), (20, 0, 0), (0, -15, 0)
    ], ids=["--", "++", "zero1", "zero2"
            ]
                             )
    def test_mul(self, a, b, expected):
        assert expected == self.cal.mul(a, b)

    @pytest.mark.parametrize("a, b, expected", [
        (15, 3, 5), (15, -3, -5), (-20, -4, 5,), (20, 0, 0)
    ], ids=["+++", "+--", "--+", "zero"]
                             )
    def test_div(self, a, b, expected):
        if b != 0:
            assert expected == self.cal.div(a, b)
        else:
            print("0不能作为除数，输入的值有误")
