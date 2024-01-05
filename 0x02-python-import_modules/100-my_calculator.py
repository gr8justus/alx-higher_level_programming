#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

argc = len(argv) - 1

if __name__ == "__main__":
    if argc != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operand_1 = int(argv[1])
    operand_2 = int(argv[3])
    operator = argv[2]

    if operator != "+" and operator != "-" and operator != "*" and \
       operator != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "+":
        operation = add(operand_1, operand_2)
    elif operator == "-":
        operation = sub(operand_1, operand_2)
    elif operator == "*":
        operation = mul(operand_1, operand_2)
    elif operator == "/":
        operation = div(operand_1, operand_2)

    print("{:d} {} {:d} = {:d}".format(operand_1, operator, operand_2,
                                       operation))
