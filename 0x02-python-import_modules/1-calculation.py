#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    add_sol = add(a, b)
    sub_sol = sub(a, b)
    mul_sol = mul(a, b)
    div_sol = div(a, b)

    print("{} + {} = {}".format(a, b, add_sol))
    print("{} - {} = {}".format(a, b, sub_sol))
    print("{} * {} = {}".format(a, b, mul_sol))
    print("{} / {} = {}".format(a, b, div_sol))

