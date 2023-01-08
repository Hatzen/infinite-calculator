from infiniteMath.calculator import Calculator

def main():
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    calculator = Calculator()
    print("Add:", calculator.add(x,y))
    print("Subtract:", calculator.subtract(x - y))
    print("Divide:", calculator.divide(x, y))
    print("Multiply:", calculator.divide(x, y))

# TODO
def calculate_pi():
    # Verwendung der Leibniz-Formel
    # pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 4/15 + ...
    pass

if __name__ == '__main__':
    main()