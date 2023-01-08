from infiniteMath.calculator import Calculator
import time

def main():
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    calculator = Calculator()
    print("Add:", calculator.add(x,y))
    print("Subtract:", calculator.subtract(x, y))
    print("Divide:", calculator.divide(x, y))
    print("Multiply:", calculator.multiply(x, y))

# TODO
def calculate_pi():
    # Verwendung der Leibniz-Formel
    # pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 4/15 + ...

    # constants
    four = "4"
    two = "2"

    # needed vars
    result = "0" # Current pi value
    i = "1"
    new_term = "" # 4 / i
    is_minus = False
    calculator = Calculator()
    last_timestamp = time.time()

    while(True):
        new_term = calculator.divide(four, i)
        if (is_minus):
            result = calculator.subtract(result, new_term)
        else:
            result = calculator.add(result, new_term)
        i = calculator.add(i, two)
        is_minus = not is_minus

        # Write result async within file.
        diff = time.time() - last_timestamp
        if (diff > 0.0001):
            print("calculated pi numbers %s which is %s " % (len(result), result))
            last_timestamp = time.time()
    print("Ended pi calculation:", result)

if __name__ == '__main__':
    main()