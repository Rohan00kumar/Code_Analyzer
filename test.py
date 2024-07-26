# test.py
import unittest
from analyzer import CodeAnalyzer


class TestCodeAnalyzer(unittest.TestCase):
    def test_simple_function(self):
        code = """
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
"""
        analyzer = CodeAnalyzer(code)
        complexity = analyzer.analyze()
        self.assertEqual(complexity, 1)


if __name__ == "__main__":
    unittest.main()
