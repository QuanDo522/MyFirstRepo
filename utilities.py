import numpy as np
import argparse

class Calculator:
    def __init__(self, num1, num2):
        self.num2 = num2
        self.num1 = num1
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero!")

        return self.num1 / self.num2

    def random_operation(self):
        return self.num1 * self.num2 * np.random.rand(3, 3)

def myargs():
    parser = argparse.ArgumentParser(description = "Perform basic arithmetic operations", 
                                     epilog = "** Verseion 1.0",
                                     prog = "Arithmetic Operator")
    parser.add_argument("-n",
                        "--num1",
                          type = float, 
                          help = "First Number", 
                          default = 2.20)
    
    parser.add_argument("-m",
                        "--num2", 
                        type = float, 
                        help = "Second Number", 
                        default = 2.20)
    parser.add_argument(
                        "-o", 
                        "--operation", 
                        choices = ["add", "subtract", "multiply", "divide"], 
                        help = "Operation to perform", 
                        default = "add")

    return parser.parse_args()