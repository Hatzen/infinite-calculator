from enum import Enum


class Compare(Enum):
    GREATER = 1
    LOWER = -1
    EQUAL = 0

"""
Calculator which can operate with strings and so is not restricted by length of the numbers.
"""
# TODO: Implement for decimal numbers (with point) and negative numbers.
class Calculator:

    def add(self, a: str, b: str):
        # make strings the same length.
        while len(a) < len(b):
            a = "0" + a
        while len(b) < len(a):
            b = "0" + b
        result = ""
        carry = 0

        # add by number wise.
        for i in range(len(a)):
            x = int(a[i])
            y = int(b[i])
            s = x + y + carry
            result += str(s % 10)
            carry = s // 10

        # add carry if there still is one.
        if carry > 0:
            result += str(carry)

        return result

    def subtract(self, a: str, b: str):
        while len(a) < len(b):
            a = "0" + a
        while len(b) < len(a):
            b = "0" + b
        result = ""
        borrow = 0

        # subtract number wise.
        for i in range(len(a)):
            x = int(a[i])
            y = int(b[i])
            s = x - y - borrow
            if s < 0:
                s += 10
                borrow = 1
            else:
                borrow = 0
            result += str(s)

        # remove leading zeros, as a - a can have |a| zeros and the like.
        result = result.lstrip("0")
        if result == "":
            result = "0"

        return result

    # multiply by multiple addtions.
    def multiply(self, a: str, b: str):
        result = "0"
        counter = "0"
        while(self.compare(counter, a) == Compare.LOWER):
            result = self.add(result, b)
        return result
        

    # Divide by euklides algorithem. 
    def divide(self, a: str, b: str) -> str:
        result = ""
        quotient = ""

        # iterate over every number of a.
        for i in range(len(a)):
            # add number to quotient
            quotient += a[i]
            dividend = 0

            # iterate over every number of b.
            for j in range(len(b)):
                # calculate dividend and add quotient
                dividend = dividend * 10 + int(b[j])
                if dividend <= int(quotient):
                    quotient += str(dividend)
                    result += "0"
                else:
                    quotient += str(dividend)
                    result += "1"

        # remove leading zeros.
        result = result.lstrip("0")
        return result

    def compare(self, a: str, b: str):
        if len(a) > len(b):
            return Compare.GREATER
        elif len(b) > len(a):
            return Compare.LOWER
        else:
            for i in range(len(a)):
                if int(a[i]) > int(b[i]):
                    return Compare.GREATER
                elif int(b[i]) > int(a[i]):
                    return Compare.LOWER
            return Compare.EQUAL
