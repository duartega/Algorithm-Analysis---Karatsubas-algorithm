"""

Authors:        Gabriel Duarte and Elliot Newman
Class:          CS415 Algorithm Analysis
Assignment:     Project 2
Date:           10/18/2018
Description:    Code Karatsuba's Algorithm and Exponentiation Algorithm
                to show efficiency in run time.

"""


def karatsuba(first_num, second_num):
    # Create the arrays for storing digits by 1 digit per index
    fn = []
    sn = []

    # Create n for the power of 10^n and 10^(n/2)
    n = ''
    n2 = ''

    # Base case for one digit multiplications
    if (len(first_num) == 1 and len(second_num) == 1):
        mult = int(first_num) * int(second_num)
        return mult

    # Adds zeros to left for un-matching number lengths
    # For ex: 12 x 4561 would pad 12 as 0012 x 4561
    if (len(first_num) < len(second_num)):
        while (len(first_num) != len(second_num)):
            first_num = '0' + first_num
    if (len(first_num) > len(second_num)):
        while (len(first_num) != len(second_num)):
            second_num = '0' + second_num

    # Original_num will allow us to get the correct n
    # Since we change some numbers from 132 to 1302 temporarily
    # n would change so we set the correct amount of zeros to
    # be added in the end from the 132 and not 1302 which
    # would yield 3 zeros instead of 4 zeros
    original_num = len(first_num)
    num_of_digits = len(first_num)

    # Split the list in half
    split = (num_of_digits // 2)

    # This will add zeros if one or both numbers
    # contain an odd length, then append to the list
    # For ex: 123*415 -> 1203*4105
    i = 0
    j = num_of_digits//2+num_of_digits-1
    while ( i < num_of_digits):
        if ( j-1 == i and num_of_digits %2 == 1):
            first_num = first_num[:i] + '0' + first_num[i:]
            second_num = second_num[:i] + '0' + second_num[i:]
            fn.append('0')
            sn.append('0')
            i += 1
            num_of_digits += 1
            split += 1

        fn.append(first_num[i])
        sn.append(second_num[i])
        i += 1

    # This get the n for 10^n and 10^(n/2)
    padc1 = original_num - split
    padc2 = padc1 * 2

    # Create the necessary amount of zeros for
    # 10^n and 10^(n/2)
    for i in range(padc2):
        n += '0'
    for i in range(padc1):
        n2 += '0'

    # Python syntax to get the indexes from
    # [0:split] and [split:end]
    a1 = fn[:split]
    b1 = sn[:split]
    a0 = fn[split:]
    b0 = sn[split:]

    # Calcualate c2, c1, c0, c
    # "".join(a1) joins elements in the list For ex: ['1','2'] would yield '12'
    c2 = karatsuba("".join(a1), "".join(b1))
    c0 = karatsuba("".join(a0), "".join(b0))
    c1 = karatsuba(str(int("".join(a1)) + int("".join(a0))), str(int("".join(b1)) + int("".join(b0)))) - (c2 + c0)
    c  = int((int(str(c2) + n)) + (int(str(c1) + n2)) + int(c0))
    return c


def Exponentiation(a, n):
    result = a

    for i in range(n - 1):
        result *= a
        print(karatsuba(str(result), str(a)))
        # result *= a
    return result
    #    else
    #       if (n % 2 == 0):
    #          return
    """
    a^n =
    (a^n/2)^2           if n is even and positive,
    (a^(n-1)/2)^2 * a   if n is odd,
    1                   if n = 0.
    """


def main():
    # 5//2 = 2  NOT  3
    x = '0'

    # Loop until the user wants to exit
    while (x != '3'):

        # Ask which Task the user would like to run
        print("\n1: Karatsuba's Algorithm")
        print("2: Exponentiation")
        print("3: Quit\n")
        print("Which option would you like? ")
        x = input()

        # Run Karatsuba's Algorithm
        if (x == '1'):
            # Grab some input from the user
            first_num = str(input("\nPlease enter a number less than or equal to 1000: "))
            second_num = str(input("Please enter another number less than or equal to 1000: "))
            print("\nThe product of", first_num, "and", second_num, "is:", int(int(first_num) * int(second_num)))
            c = karatsuba(first_num, second_num)
            print("Product after karatsuba is: ", c)

        # Run Exponentiation Algorithm
        elif (x == '2'):
            # Grab some input from the user
            a = int(input("\nPlease enter a number less than or equal to 1000 for the constant: "))
            n = int(input("Please enter another number less than or equal to 1000 for the power: "))
            result = Exponentiation(a, n)
            print("Final Value:", result)
        # Exit
        else:
            exit


main()
