def print_formatted(number):
    # your code goes here
    # bin rep of the max no
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)

        print(decimal, octal, hexadecimal, binary)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)