from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_difference_calculate_correct(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_adding_calculate_correct(self):
        assert self.calc.adding(self, 2, 4) == 6

    def test_division_calculate_correct(self):
        assert self.calc.division(self, 10, 5) == 2