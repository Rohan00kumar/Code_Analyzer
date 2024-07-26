# analyzer.py
import ast
import timeit


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self, code):
        self.tree = ast.parse(code)
        self.complexity = 0

    def visit_FunctionDef(self, node):
        print(f"Analyzing function: {node.name}")
        self.generic_visit(node)

    def visit_For(self, node):
        print("Found a for loop.")
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        print("Found a while loop.")
        self.complexity += 1
        self.generic_visit(node)

    def analyze(self):
        self.visit(self.tree)
        return self.complexity


def estimate_execution_time(code, function_name, *args):
    setup_code = f"from __main__ import {function_name}"
    exec_time = timeit.timeit(
        f"{function_name}({', '.join(map(str, args))})", setup=setup_code, number=1000)
    return exec_time


if __name__ == "__main__":
    code = """
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
"""
    analyzer = CodeAnalyzer(code)
    complexity = analyzer.analyze()
    print(f"Estimated Time Complexity: O(n^{complexity})")

    exec_time = estimate_execution_time(code, "example_function", 100)
    print(f"Estimated Execution Time: {exec_time} seconds")
